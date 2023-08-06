import { useEffect } from 'react';
import { render } from 'react-dom';
import { Jupyter } from './jupyter/Jupyter';
import Cell from './widgets/cell/Cell';
import CellControl from './widgets/cell/CellControl';
import Commands from './widgets/commands/Commands';
import CommandsControl from './widgets/commands/CommandsControl';
import Console from './widgets/console/Console';
import ConsoleControl from './widgets/console/ConsoleControl';
// import Dialog from './widgets/dialog/Dialog';
import DialogControl from './widgets/dialog/DialogControl';
import FileBrowser from './widgets/filebrowser/FileBrowser';
import FileBrowserControl from './widgets/filebrowser/FileBrowserControl';
import Notebook from './widgets/notebook/Notebook';
import NotebookControl from './widgets/notebook/NotebookControl';
import Settings from './widgets/settings/Settings';
import SettingsControl from './widgets/settings/SettingsControl';
import Simple from './widgets/simple/Simple';
import SimpleControl from './widgets/simple/SimpleControl';
import Terminal from './widgets/terminal/Terminal';
import TerminalControl from './widgets/terminal/TerminalControl';

/**
 * The source to be shown in the Cell example.
 */
const source = `from IPython.display import display
for i in range(3):
    display('😃 String {} added to the DOM in separated DIV.'.format(i))
    
import numpy as np
import matplotlib.pyplot as plt
x1 = np.linspace(0.0, 5.0)
x2 = np.linspace(0.0, 2.0)
y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
y2 = np.cos(2 * np.pi * x2)
fig, (ax1, ax2) = plt.subplots(2, 1)
fig.suptitle('A tale of 2 subplots')
ax1.plot(x1, y1, 'o-')
ax1.set_ylabel('Damped oscillation')
ax2.plot(x2, y2, '.-')
ax2.set_xlabel('time (s)')
ax2.set_ylabel('Undamped')
plt.show()`;

/**
 * A simple example for Jupytery React Widgets.
 */
const Example = () => {
  useEffect(() => {
    window.scrollTo(0, 0);
  }, []);
  return <Jupyter collaborative={true} terminals={true}>
    <CellControl />
    <Cell source={source} />
    <CommandsControl />
    <Commands />
    <ConsoleControl />
    <Console />
    <DialogControl />
{/*
    <Dialog />
*/}
    <FileBrowserControl />
    <FileBrowser />
    <NotebookControl />
    <Notebook path='ping.ipynb' ipywidgets="modern" />
    <SettingsControl />
    <Settings />
    <SimpleControl />
    <Simple />
    <TerminalControl />
    <Terminal />
  </Jupyter>
}

const div = document.createElement('div');
document.body.appendChild(div);

render(
  <Example/>
  ,
  div
);
