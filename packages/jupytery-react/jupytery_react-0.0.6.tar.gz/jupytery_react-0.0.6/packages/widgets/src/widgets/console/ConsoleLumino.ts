import { RenderMimeRegistry, standardRendererFactories as initialFactories } from '@jupyterlab/rendermime';
import { CommandRegistry } from '@lumino/commands';
import { BoxPanel } from '@lumino/widgets';
import { ServiceManager } from '@jupyterlab/services';
import { editorServices } from '@jupyterlab/codemirror';
import { ConsolePanel } from '@jupyterlab/console';

class ConsoleLumino {
  private consolePanel: BoxPanel;

  constructor() {

    this.consolePanel = new BoxPanel();
    this.consolePanel.direction = 'top-to-bottom';
    this.consolePanel.spacing = 0;
    this.consolePanel.id = 'dla-jlab-console'

    const manager = new ServiceManager();
    void manager.ready.then(() => {
      start('console-path', manager, this.consolePanel);
    });
    
    function start(
      path: string,
      manager: ServiceManager.IManager,
      panel: BoxPanel
    ) {

      const commands = new CommandRegistry();    

      document.addEventListener('keydown', event => {
        commands.processKeydownEvent(event);
      });

      const rendermime = new RenderMimeRegistry({ initialFactories });
      const editorFactory = editorServices.factoryService.newInlineEditor;
      const contentFactory = new ConsolePanel.ContentFactory({ editorFactory });
      const console = new ConsolePanel({
        rendermime,
        manager,
        path,
        contentFactory,
        mimeTypeService: editorServices.mimeTypeService
      });
      console.title.label = 'Console';

      BoxPanel.setStretch(console, 1);
      panel.addWidget(console);

      window.addEventListener('resize', () => {
        panel.update();
      });

      const selector = '.jp-ConsolePanel';
      let command: string;

      command = 'console:clear';
      commands.addCommand(command, {
        label: 'Clear',
        execute: () => {
          console.console.clear();
        }
      });

      command = 'console:execute';
      commands.addCommand(command, {
        label: 'Execute Prompt',
        execute: () => {
          return console.console.execute();
        }
      });
      commands.addKeyBinding({ command, selector, keys: ['Enter'] });

      command = 'console:execute-forced';
      commands.addCommand(command, {
        label: 'Execute Cell (forced)',
        execute: () => {
          return console.console.execute(true);
        }
      });
      commands.addKeyBinding({ command, selector, keys: ['Shift Enter'] });

      command = 'console:linebreak';
      commands.addCommand(command, {
        label: 'Insert Line Break',
        execute: () => {
          console.console.insertLinebreak();
        }
      });
      commands.addKeyBinding({ command, selector, keys: ['Ctrl Enter'] });    

    }
    
  }

  get panel(): BoxPanel {
    return this.consolePanel;
  }

}

export default ConsoleLumino;
