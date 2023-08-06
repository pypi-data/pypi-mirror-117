import ConsoleLumino from './ConsoleLumino';
import LuminoAttached from '../../lumino/LuminoAttached';

import '@jupyterlab/console/style/index.css';
import '@jupyterlab/theme-light-extension/style/theme.css';
import '@jupyterlab/theme-light-extension/style/variables.css';

import './Console.css';

const Console = () => {
  const consoleLumino = new ConsoleLumino();
  return <LuminoAttached>{consoleLumino.panel}</LuminoAttached>
}

export default Console;
