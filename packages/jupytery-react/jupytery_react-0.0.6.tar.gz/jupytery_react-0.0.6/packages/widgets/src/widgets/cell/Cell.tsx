import { useState, useEffect } from 'react';
import { useDispatch, useStore } from "react-redux";
import { CodeCell } from '@jupyterlab/cells';
import { KernelMessage } from '@jupyterlab/services';
// import { map } from "rxjs/operators";
// import KernelModel from './KernelModel';
import { cellEpics, cellActions, cellReducer } from './CellRedux';
import CellLumino from './CellLumino';
import LuminoAttached from '../../lumino/LuminoAttached';
import { asObservable } from '../../lumino/LuminoObservable';

import '@jupyterlab/cells/style/index.css';
// This should be only index.css, looks like jupyterlab has a regression here...
import '@jupyterlab/theme-light-extension/style/theme.css';
import '@jupyterlab/theme-light-extension/style/variables.css';

import './Cell.css';

export type ICellProps = {
  source?: string;
  autoStart?: boolean;
}

const Cell = (props: ICellProps) => {
  const [cellLumino, _] = useState(new CellLumino(props.source!));
  const dispatch = useDispatch();
  const injectableStore = useStore();  
  useEffect(() => {
    cellLumino.codeCell.model.value.changed.connect((sender, changedArgs) => {
      dispatch(cellActions.source.started(sender.text));
    });
    const outputs$ = asObservable(cellLumino.codeCell.outputArea.outputLengthChanged);
    outputs$.subscribe(
      outputsCount => { dispatch(cellActions.outputsCount.started(outputsCount)); }
    );
    /*
    // TODO Check if this works fine...
    outputs$.pipe(
      map(output => {
        console.log('---- output', output);
      })
    );
    */  
    (injectableStore as any).injectReducer('cell', cellReducer);
    (injectableStore as any).injectEpic(cellEpics(cellLumino));
    dispatch(cellActions.source.started(props.source!));
    // Kickoff the fire!
    cellLumino.sessionContext.initialize().then(() => {
//      const kernelModel = new KernelModel(cellLumino.sessionContext);
//      kernelModel.execute(props.source!);
      if (props.autoStart) {
        const executePromise =  CodeCell.execute(cellLumino.codeCell, cellLumino.sessionContext);
        executePromise.then((msg: void | KernelMessage.IExecuteReplyMsg) => {
          dispatch(cellActions.update.started({
            kernelAvailable: true,
          }));
        });  
      }
    });
  }, []);
  return <LuminoAttached>{cellLumino.panel}</LuminoAttached>
}

const defaultSource = `from IPython.display import display

for i in range(10):
    display('String {} added to the DOM in separated DIV.'.format(i))`

Cell.defaultProps = {
  source: defaultSource,
  autoStart: true,
} as Partial<ICellProps>;

export default Cell;
