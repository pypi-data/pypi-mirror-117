import React, { useState, useEffect, useContext, createContext } from "react";
import { Provider as ReduxProvider } from "react-redux";
import { getJupyterServerHttpUrl} from './JupyterConfig';
import { requestAPI } from './Handlers';

/**
 * The type for the Jupyter context.
 */
export type JupyterContextType = {
  variant: string;
  setVariant: (value: string) => void;
  injectableStore: any;
};

/**
 * The instance for the Jupyter context.
 */
export const JupyterContext = createContext<JupyterContextType | undefined>(undefined);

export function useJupyter() {
  const context = useContext(JupyterContext);
  if (!context) throw new Error("useContext must be inside a Provider with a value.");
  return context;
}

/**
 * The type for the Jupyter context consumer.
 */
export const JupyterContextConsumer = JupyterContext.Consumer;

/**
 * The type for the Jupyter context provider.
 */
 const JupyterProvider = JupyterContext.Provider;

 /**
  * Utiliy method to ensure the Jupyter context is authenticated
  * with the Jupyter server.
  */
export const ensureJupyterAuth = (): Promise<boolean> => {
  return requestAPI<any>(
    'jupytery_auth', 
    'users',
  )
  .then(data => {
    return true;
  })
  .catch(reason => {
    console.log('The jupytery_auth server API has failed with reason', reason);
    return false;
  });
}

/**
 * The type for the properties of the Jupyter context.
 */
type JupyterContextProps = {
  children: React.ReactNode;
  initialVariant: string;
  injectableStore: any;
};

/**
 * The Jupyter context provider.
 */
export const JupyterContextProvider: React.FC<{ 
  children: React.ReactNode,
  initialVariant: string,
  injectableStore: any
}> = ({ children, initialVariant, injectableStore }: JupyterContextProps) => {
  const [variant, setVariant] = useState('');
  useEffect(() => {
    ensureJupyterAuth().then(isAuth => {
      if (!isAuth) {
        const loginUrl = getJupyterServerHttpUrl() + '/login?next=' + window.location
        console.log('Redirecting to jupyter login url: ', loginUrl);
        window.location.replace(loginUrl);
      }
    });
    setVariant(initialVariant);
  }, [initialVariant]);
  return (
    <ReduxProvider store={injectableStore}>
      <JupyterProvider value={{ variant, setVariant, injectableStore }}>
        { children }
      </JupyterProvider>
    </ReduxProvider>
  )
}
