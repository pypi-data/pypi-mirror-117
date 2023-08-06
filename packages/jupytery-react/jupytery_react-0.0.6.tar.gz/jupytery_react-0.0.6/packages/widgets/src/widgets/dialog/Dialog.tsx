import { useState, useEffect } from 'react';
import LuminoDetached from '../../lumino/LuminoDetached';
import DialogLumino from './DialogLumino';

import './Dialog.css';
import '@jupyterlab/apputils/style/index.css';
import '@jupyterlab/theme-light-extension/style/theme.css';
import '@jupyterlab/theme-light-extension/style/variables.css';
 
const Dialog = () => {
  const [dialogLumino, _] = useState(new DialogLumino());
  useEffect(() => {
    dialogLumino.dialog.launch().then(success => success)
  }, []);
  return <LuminoDetached>{dialogLumino.dialog}</LuminoDetached>
}

export default Dialog;
