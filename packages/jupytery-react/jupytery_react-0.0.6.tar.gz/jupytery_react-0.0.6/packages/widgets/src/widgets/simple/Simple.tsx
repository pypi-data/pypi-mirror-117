import LuminoAttached from '../../lumino/LuminoAttached';
import SimpleLumino from './SimpleLumino';

import '@lumino/default-theme/style/index.css';

import './Simple.css'

const Simple = () => {
    const simpleLumino = new SimpleLumino();
    return <LuminoAttached>{simpleLumino.panel}</LuminoAttached>
  }
  
export default Simple;
