import { Dialog as JPDialog } from '@jupyterlab/apputils';

class DialogLumino {
  public dialog: JPDialog<any>;
  public constructor() {
    this.dialog = new JPDialog({
      title: 'Dialog Title',
      body: 'This is the body of the dialog...',
      buttons: [
        JPDialog.cancelButton(),
        JPDialog.okButton(),
      ]
    });
  }
}

export default DialogLumino;
