import React from 'react';
import ReactDOM from 'react-dom';
import { ICellHeader } from '@jupyterlab/cells';
import { CommandRegistry } from '@lumino/commands';
import { v4 as uuidv4 } from 'uuid';
import { notebookActions } from '../NotebookRedux';
import { LuminoReactPortal } from '../../../lumino/LuminoReactPortal';

const CELL_HEADER_CLASS = 'jp-CellHeader';
const CELL_HEADER_DIV_CLASS = 'dla-cellHeaderContainer';

export class CellSidebar extends LuminoReactPortal implements ICellHeader {
  private readonly commands: CommandRegistry;
  constructor(sidebarReact: any, commands: CommandRegistry, injectableStore: any) {
    super();
    this.commands = commands;
    this.addClass(CELL_HEADER_CLASS);
    this.id = uuidv4();
    const sidebar = React.createElement(
      sidebarReact,
      {
        command: this.commands,
        id: this.id
      }
    );
    const portal = ReactDOM.createPortal(
      <div className={CELL_HEADER_DIV_CLASS}>
        {sidebar}
      </div>
      ,
      this.node
    );
    injectableStore.dispatch(notebookActions.portal.started(portal) as never);
  }
}
