/* State */

export type IFileBrowser = number;

export interface IFileBrowserState {
  outputs: IFileBrowser;
}

export const fileBrowserInitialState: IFileBrowserState = {
  outputs: 0
}

/* Selectors */

import { useSelector } from "react-redux";

export const selectFileBrowser = (): IFileBrowserState =>
  useSelector((state: IFileBrowserState) => {
    if ((state as any).fileBrowser) {
      return (state as any).fileBrowser;
    }
    return {outputs: 0};
  });

/* Actions */

import actionCreatorFactory from "typescript-fsa";

export enum ActionType {
  OUTPUTS = "fileBrowser/OUTPUTS",
  EXECUTE = "fileBrowser/EXECUTE",
}

const actionCreator = actionCreatorFactory('jupyterWidgets');

export const fileBrowserActions = {
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
import FileBrowserLumino from './FileBrowserLumino';

export const fileBrowserEpics = (fileBrowserLumino: FileBrowserLumino) => {

  const outputsEpic: Epic<
    AnyAction,
    Action<Success<number, number>>,
    IFileBrowserState
  > = action$ =>
    action$.pipe(
      ofAction(fileBrowserActions.outputs.started),
      map(action => {
        return fileBrowserActions.outputs.done({
          params: action.payload,
          result: action.payload
        });
      })
    );

  const executeEpic: Epic<
    AnyAction,
    Action<Success<number, number>>,
    IFileBrowserState
  > = action$ =>
    action$.pipe(
      ofAction(fileBrowserActions.execute.started),
//      tap(action => fileBrowserLumino.execute()),
      ignoreElements()
  );

  const loggingEpic: Epic<
    AnyAction,
    AnyAction,
    IFileBrowserState
  > = action$ =>
    action$
      .pipe(
        ofAction(fileBrowserActions.outputs.started),
  //      tap(action => fileBrowser.log(action.type)),
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

export const fileBrowserReducer = reducerWithInitialState(fileBrowserInitialState)
  .case(fileBrowserActions.outputs.done, (state: IFileBrowserState, success: Success<number, number>) => {
    return {
      ...state,
      outputs: success.result
    }
  }
);
