/* State */

export type IConsole = number;

export interface IConsoleState {
  outputs: IConsole;
}

export const consoleInitialState: IConsoleState = {
  outputs: 0
}

/* Selectors */

import { useSelector } from "react-redux";

export const selectConsole = (): IConsoleState =>
  useSelector((state: IConsoleState) => {
    if ((state as any).console) {
      return (state as any).console;
    }
    return {outputs: 0};
  });

/* Actions */

import actionCreatorFactory from "typescript-fsa";

export enum ActionType {
  OUTPUTS = "console/OUTPUTS",
  EXECUTE = "console/EXECUTE",
}

const actionCreator = actionCreatorFactory('jupyterWidgets');

export const consoleActions = {
  outputs: actionCreator.async<number, number, {}>(
    ActionType.OUTPUTS
  ),
  execute: actionCreator.async<void, void, {}>(
    ActionType.EXECUTE
  ),
}

/* Epics */

import { combineEpics, Epic } from "redux-observable";
import { AnyAction, Action, Success } from "typescript-fsa";
import { map, ignoreElements } from "rxjs/operators";
import { ofAction } from "@datalayer/typescript-fsa-redux-observable";
import ConsoleLumino from './ConsoleLumino';

export const consoleEpics = (consoleLumino: ConsoleLumino) => {

  const outputsEpic: Epic<
    AnyAction,
    Action<Success<number, number>>,
    IConsoleState
  > = action$ =>
    action$.pipe(
      ofAction(consoleActions.outputs.started),
      map(action => {
        return consoleActions.outputs.done({
          params: action.payload,
          result: action.payload
        });
      })
    );

  const executeEpic: Epic<
    AnyAction,
    Action<Success<number, number>>,
    IConsoleState
  > = action$ =>
    action$.pipe(
      ofAction(consoleActions.execute.started),
//      tap(action => consoleLumino.execute()),
      ignoreElements()
  );

  const loggingEpic: Epic<
    AnyAction,
    AnyAction,
    IConsoleState
  > = action$ =>
    action$
      .pipe(
        ofAction(consoleActions.outputs.started),
  //      tap(action => console.log(action.type)),
        ignoreElements()
      );

  return combineEpics(
    loggingEpic,
    outputsEpic,
    executeEpic,
  );
}

/* Reducers */

import { reducerWithInitialState } from "typescript-fsa-reducers";

export const consoleReducer = reducerWithInitialState(consoleInitialState)
  .case(consoleActions.outputs.done, (state: IConsoleState, success: Success<number, number>) => {
    return {
      ...state,
      outputs: success.result
    }
  }
);
