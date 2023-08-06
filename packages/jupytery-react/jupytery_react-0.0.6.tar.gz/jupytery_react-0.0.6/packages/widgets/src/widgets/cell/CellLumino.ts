import { BoxPanel } from '@lumino/widgets';
import { SessionContext, Toolbar, ToolbarButton } from '@jupyterlab/apputils';
import { CodeCellModel, CodeCell } from '@jupyterlab/cells';
import { CodeMirrorMimeTypeService } from '@jupyterlab/codemirror';
import { runIcon } from '@jupyterlab/ui-components';
import { CompleterModel, Completer, CompletionHandler, KernelConnector } from '@jupyterlab/completer';
import { RenderMimeRegistry, standardRendererFactories as initialFactories } from '@jupyterlab/rendermime';
import { SessionManager, KernelManager, KernelSpecManager } from '@jupyterlab/services';
import { ServerConnection } from '@jupyterlab/services';
import { CommandRegistry } from '@lumino/commands';

class CellLumino {
  private _codeCell: CodeCell;
  private _cellPanel: BoxPanel;
  private _sessionContext: SessionContext;

  constructor(source: string) {
    this._cellPanel = new BoxPanel();
    this._cellPanel.direction = 'top-to-bottom';
    this._cellPanel.spacing = 0;
    this._cellPanel.addClass('dla-JupyterCell');
    const serverSettings = ServerConnection.makeSettings();
    const kernelManager = new KernelManager({
      serverSettings
    });
    const specsManager = new KernelSpecManager({
      serverSettings
    });
    const sessionManager = new SessionManager({
      serverSettings,
      kernelManager
    });
    this._sessionContext = new SessionContext({
      sessionManager,
      specsManager,
      name: 'Datalayer'
    });
    const mimeService = new CodeMirrorMimeTypeService();
    // Initialize the command registry with the bindings.
    const commands = new CommandRegistry();
    const useCapture = true;
    // Setup the keydown listener for the document.
    document.addEventListener(
      'keydown',
      event => {
        commands.processKeydownEvent(event);
      },
      useCapture
    );
    // Create the cell widget with a default rendermime instance.
    const rendermime = new RenderMimeRegistry({ initialFactories });
    const codeCell = new CodeCell({
      rendermime,
      model: new CodeCellModel({
        cell: {
          cell_type: 'code',
          source: source,
          metadata: {
          }
        }
      })
    });
    this._codeCell = codeCell.initializeState();
    // Handle the mimeType for the current kernel asynchronously.
    this._sessionContext.kernelChanged.connect(() => {
      void this._sessionContext.session?.kernel?.info.then(info => {
        const lang = info.language_info;
        const mimeType = mimeService.getMimeTypeByLanguage(lang);
        this._codeCell.model.mimeType = mimeType;
      });
    });
    // Use the default kernel.
    this._sessionContext.kernelPreference = { autoStartDefault: true };
    // Set up a completer.
    const editor = this._codeCell.editor;
    const model = new CompleterModel();
    const completer = new Completer({ editor, model });
    const connector = new KernelConnector({ session: this._sessionContext.session });
    const handler = new CompletionHandler({ completer, connector });
    // Set the handler's editor.
    handler.editor = editor;
    // Hide the widget when it first loads.
    completer.hide();
    // Create a toolbar for the cell.
    const toolbar = new Toolbar();
    toolbar.addItem('spacer', Toolbar.createSpacerItem());
    const runButton = new ToolbarButton({
      icon: runIcon,
      onClick: () => {
        CodeCell.execute(this._codeCell, this._sessionContext);
      },
      tooltip: 'Run'
    });
    toolbar.addItem('run', runButton);
    toolbar.addItem('interrupt', Toolbar.createInterruptButton(this._sessionContext));
    toolbar.addItem('restart', Toolbar.createRestartButton(this._sessionContext));
    // toolbar.addItem('name', Toolbar.createKernelNameItem(this._sessionContext));
    toolbar.addItem('status', Toolbar.createKernelStatusItem(this._sessionContext));
    this._cellPanel.addWidget(completer);
    this._cellPanel.addWidget(toolbar);
    BoxPanel.setStretch(toolbar, 0);
    this._cellPanel.addWidget(this._codeCell);
    BoxPanel.setStretch(this._codeCell, 1);
    // Handle widget state.
    window.addEventListener('resize', () => {
      this._cellPanel.update();
    });
    this._codeCell.outputsScrolled = false;
    this._codeCell.activate();
    // Add the commands.
    commands.addCommand('invoke:completer', {
      execute: () => {
        handler.invoke();
      }
    });
    commands.addCommand('run:cell', {
      execute: () => CodeCell.execute(this._codeCell, this._sessionContext)
    });
    // Add the key bindings.
    commands.addKeyBinding({
      selector: '.jp-InputArea-editor.jp-mod-completer-enabled',
      keys: ['Tab'],
      command: 'invoke:completer'
    });
    commands.addKeyBinding({
      selector: '.jp-InputArea-editor',
      keys: ['Shift Enter'],
      command: 'run:cell'
    });
  }

  get panel(): BoxPanel {
    return this._cellPanel;
  }

  get codeCell(): CodeCell {
    return this._codeCell;
  }

  get sessionContext(): SessionContext {
    return this._sessionContext;
  }

  execute = () => {
    CodeCell.execute(this._codeCell, this._sessionContext);
  }

}

export default CellLumino;
