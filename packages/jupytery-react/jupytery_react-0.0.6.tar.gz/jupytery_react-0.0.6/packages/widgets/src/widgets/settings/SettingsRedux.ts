/* State */

export type ISettings = number;

export interface ISettingsState {
  outputs: ISettings;
}

export const settingsInitialState: ISettingsState = {
  outputs: 0
}

/* Selectors */

import { useSelector } from "react-redux";

export const selectSettings = (): ISettingsState =>
  useSelector((state: ISettingsState) => {
    if ((state as any).settings) {
      return (state as any).settings;
    }
    return {outputs: 0};
  });

/* Actions */

import actionCreatorFactory from "typescript-fsa";

export enum ActionType {
  OUTPUTS = "settings/OUTPUTS",
  EXECUTE = "settings/EXECUTE",
}

const actionCreator = actionCreatorFactory('jupyterWidgets');

export const settingsActions = {
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
import SettingsLumino from './SettingsLumino';

export const settingsEpics = (settingsLumino: SettingsLumino) => {

  const outputsEpic: Epic<
    AnyAction,
    Action<Success<number, number>>,
    ISettingsState
  > = action$ =>
    action$.pipe(
      ofAction(settingsActions.outputs.started),
      map(action => {
        return settingsActions.outputs.done({
          params: action.payload,
          result: action.payload
        });
      })
    );

  const executeEpic: Epic<
    AnyAction,
    Action<Success<number, number>>,
    ISettingsState
  > = action$ =>
    action$.pipe(
      ofAction(settingsActions.execute.started),
//      tap(action => settingsLumino.execute()),
      ignoreElements()
  );

  const loggingEpic: Epic<
    AnyAction,
    AnyAction,
    ISettingsState
  > = action$ =>
    action$
      .pipe(
        ofAction(settingsActions.outputs.started),
  //      tap(action => settings.log(action.type)),
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

export const settingsReducer = reducerWithInitialState(settingsInitialState)
  .case(settingsActions.outputs.done, (state: ISettingsState, success: Success<number, number>) => {
    return {
      ...state,
      outputs: success.result
    }
  }
);
