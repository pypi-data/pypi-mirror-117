
import { render } from "react-dom";

import SlateExample from "./examples/Simple1";

import './index.css';

const div = document.createElement('div');
document.body.appendChild(div);

render(
  <>
    {
      [...Array(1).keys()].map(n => {
        return <div key={n}>
          <SlateExample />
        </div>
      })
    }
  </>
  , 
  div
);
