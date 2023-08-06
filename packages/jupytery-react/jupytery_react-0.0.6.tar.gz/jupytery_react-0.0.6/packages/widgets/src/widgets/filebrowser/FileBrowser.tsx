import FileBrowserLumino from './FileBrowserLumino';
import LuminoAttached from '../../lumino/LuminoAttached';

import '@jupyterlab/codemirror/style/index.css';
import '@jupyterlab/filebrowser/style/index.css';
import '@jupyterlab/theme-light-extension/style/theme.css';
import '@jupyterlab/theme-light-extension/style/variables.css';

import './FileBrowser.css';

const FileBrowser = () => {
  const fileBrowserLumino = new FileBrowserLumino();
  return <LuminoAttached>{fileBrowserLumino.panel}</LuminoAttached>
}

export default FileBrowser;
