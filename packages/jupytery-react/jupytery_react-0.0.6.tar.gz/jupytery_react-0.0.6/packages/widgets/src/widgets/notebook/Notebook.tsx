import { useDispatch, useStore } from "react-redux";
import NotebookLumino from './NotebookLumino';
import LuminoAttached from '../../lumino/LuminoAttached';
import { notebookEpics, notebookActions, notebookReducer, selectNotebook } from './NotebookRedux';
import CellSidebarDefault from './extension/CellSidebarDefault';
import { asObservable } from '../../lumino/LuminoObservable'

import '@jupyterlab/notebook/style/index.css';
import '@jupyterlab/theme-light-extension/style/theme.css';
import '@jupyterlab/theme-light-extension/style/variables.css';

import './Notebook.css';

export type INotebookProps = {
  path: string;
  ipywidgets?: 'classic' | 'modern';
  sidebarComponent: (props: any) => JSX.Element;
  sidebarMargin: number;
}

/**
 * The React portals created by the Notebook component.
 */
const Portals = () => {
  const notebook = selectNotebook();
  const portals = notebook.portals;
  return <>{portals.map((portal: React.ReactPortal) => portal)}</>
}

/**
 * This components creates a Notebook as a collection of cells 
 * with sidebars.
 * 
 * @param props The notebook properties.
 * @returns A Notebook React.js component.
 */
const Notebook = (props: INotebookProps) => {
  const injectableStore = useStore();
  const notebookLumino = new NotebookLumino(props, injectableStore);
  const dispatch = useDispatch();
  notebookLumino.manager.ready.then(() => {
    notebookLumino.createApp(props.path);
    const notebookChange$ = asObservable(notebookLumino.notebookPanel.model!.sharedModel.changed);
    notebookChange$.subscribe(
      notebookChange => {
        dispatch(notebookActions.notebookChange.started(notebookChange)); 
      }
    );
    const activeCellChanged$ = asObservable(notebookLumino.notebookPanel.content.activeCellChanged);
    activeCellChanged$.subscribe(
      activeCellChanged => {
        dispatch(notebookActions.activeCellChange.started(activeCellChanged)); 
      }
    );
    const kernelStatusChanged$ = asObservable(notebookLumino.notebookPanel.sessionContext.statusChanged);
    kernelStatusChanged$.subscribe(
      kernelStatusChanged => {
        dispatch(notebookActions.kernelStatusChanged.started(kernelStatusChanged)); 
      }
    );
    (injectableStore as any).injectReducer('notebook', notebookReducer);
    (injectableStore as any).injectEpic(notebookEpics(notebookLumino));
  });
  return (
    <div
      css={{
        '& .jp-Toolbar': {
          display: 'none',
        },
        '& .jp-Cell': {
          width: `calc(100% - ${props.sidebarMargin}px)`,
        },
        '& .jp-Cell .jp-CellHeader': {
          height: 'auto',
          position: 'absolute',
          top: '-5px',
          left: `${props.sidebarMargin + 10}px`,
        },
        '& .jp-Cell .dla-cellHeaderContainer': {
          padding: '4px 8px',
          width: `${props.sidebarMargin + 10}px`,
          cursor: 'pointer',
          userSelect: 'none',
          marginLeft: 'auto',
          zIndex: 100,
        },
      }}
    >
      <Portals/>
      <LuminoAttached>{notebookLumino.panel}</LuminoAttached>
    </div>
  )
}

Notebook.defaultProps = {
  ipywidgets: 'modern',
  sidebarComponent: CellSidebarDefault,
  sidebarMargin: 100,
} as Partial<INotebookProps>;

export default Notebook;
