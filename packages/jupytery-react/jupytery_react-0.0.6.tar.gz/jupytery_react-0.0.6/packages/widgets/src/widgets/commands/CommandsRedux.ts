/* State */

export type ICommand = number;

export interface ICommandState {
  outputs: ICommand;
}

export const commandsInitialState: ICommandState = {
  outputs: 0
}

/* Selectors */

import { useSelector } from "react-redux";

export const selectCommands = (): ICommandState =>
  useSelector((state: ICommandState) => {
    if ((state as any).commands) {
      return (state as any).commands;
    }
    return {outputs: 0};
  });

/* Actions */

import actionCreatorFactory from "typescript-fsa";

export enum ActionType {
  OUTPUTS = "commands/OUTPUTS",
  EXECUTE = "commands/EXECUTE",
}

const actionCreator = actionCreatorFactory('jupyterWidgets');

export const commandsActions = {
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
import CommandLumino from './CommandsLumino';

export const commandsEpics = (commandsLumino: CommandLumino) => {

  const outputsEpic: Epic<
    AnyAction,
    Action<Success<number, number>>,
    ICommandState
  > = action$ =>
    action$.pipe(
      ofAction(commandsActions.outputs.started),
      map(action => {
        return commandsActions.outputs.done({
          params: action.payload,
          result: action.payload
        });
      })
    );

  const executeEpic: Epic<
    AnyAction,
    Action<Success<number, number>>,
    ICommandState
  > = action$ =>
    action$.pipe(
      ofAction(commandsActions.execute.started),
//      tap(action => commandsLumino.execute()),
      ignoreElements()
  );

  const loggingEpic: Epic<
    AnyAction,
    AnyAction,
    ICommandState
  > = action$ =>
    action$
      .pipe(
        ofAction(commandsActions.outputs.started),
  //      tap(action => commands.log(action.type)),
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

export const commandsReducer = reducerWithInitialState(commandsInitialState)
  .case(commandsActions.outputs.done, (state: ICommandState, success: Success<number, number>) => {
    return {
      ...state,
      outputs: success.result
    }
  }
);
