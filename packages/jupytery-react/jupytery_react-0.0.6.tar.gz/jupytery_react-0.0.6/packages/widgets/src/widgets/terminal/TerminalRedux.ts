/* State */

export type ITerminal = boolean;

export interface ITerminalState {
  dark: ITerminal;
}

export const terminalInitialState: ITerminalState = {
  dark: false
}

/* Selectors */

import { useSelector } from "react-redux";

export const selectTerminal = (): ITerminalState =>
  useSelector((state: ITerminalState) => {
    if ((state as any).terminal) {
      return (state as any).terminal;
    }
    return {dark: false};
  });

/* Actions */

import actionCreatorFactory from "typescript-fsa";

export enum ActionType {
  DARK = "terminal/DARK",
}

const actionCreator = actionCreatorFactory('jupyterWidgets');

export const terminalActions = {
  dark: actionCreator.async<boolean, boolean, {}>(
    ActionType.DARK
  ),
}

/* Epics */

import { combineEpics, Epic } from "redux-observable";
import { AnyAction, Action, Success } from "typescript-fsa";
import { map } from "rxjs/operators";
import { ofAction } from "@datalayer/typescript-fsa-redux-observable";
import TerminalLumino from './TerminalLumino';

export const terminalEpics = (terminalLumino: TerminalLumino) => {

  const themeEpic: Epic<
    AnyAction,
    Action<Success<boolean, boolean>>,
    ITerminalState
  > = action$ =>
    action$.pipe(
      ofAction(terminalActions.dark.started),
      map(action => {
        (action.payload) ?
          terminalLumino.setTheme('dark')
          :
          terminalLumino.setTheme('light')
        return terminalActions.dark.done({
          params: action.payload,
          result: action.payload
        });
      })
    );

  return combineEpics(
    themeEpic,
  );
}

/* Reducers */

import { reducerWithInitialState } from "typescript-fsa-reducers";

export const terminalReducer = reducerWithInitialState(terminalInitialState)
  .case(terminalActions.dark.done, (state: ITerminalState, success: Success<boolean, boolean>) => {
    return {
      ...state,
      dark: success.result
    }
  }
);
