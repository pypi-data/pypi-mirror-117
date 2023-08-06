import { useEffect } from 'react';
import { useStore } from "react-redux";
import TerminalLumino from './TerminalLumino';
import LuminoAttached from '../../lumino/LuminoAttached';
import { terminalEpics, terminalReducer } from './TerminalRedux';

import '@jupyterlab/terminal/style/index.css';
import '@jupyterlab/theme-light-extension/style/theme.css';
import '@jupyterlab/theme-light-extension/style/variables.css';

import './Terminal.css';

const Terminal = () => {
  const terminalLumino = new TerminalLumino();
  const injectableStore = useStore();
  useEffect(() => {
    (injectableStore as any).injectReducer('terminal', terminalReducer);
    (injectableStore as any).injectEpic(terminalEpics(terminalLumino));
  }, []); 
  return <LuminoAttached>{terminalLumino.panel}</LuminoAttached>
}

export default Terminal;
