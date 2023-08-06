import { combineReducers } from "redux";
import { combineEpics } from "redux-observable";
import { AnyAction } from "typescript-fsa";
import { initReducer, initInitialState, IInitState, initEpics } from "../widgets/init/InitRedux";

/* State */

export interface IState {
  counter: IInitState;
}

export const initialState: IState = {
  counter: initInitialState
}

/* Actions */


/* Epics */

export const epics = combineEpics<AnyAction, AnyAction, any>(
  initEpics
);

/* Reducers */

export const reducers = combineReducers<IState>({
  counter: initReducer
});
