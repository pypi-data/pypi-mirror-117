import CommandLumino from './CommandsLumino';
import LuminoAttached from '../../lumino/LuminoAttached';

import '@lumino/default-theme/style/index.css';

import './Commands.css';

const Command = () => {
  const commandLumino = new CommandLumino();
  return <LuminoAttached>{commandLumino.panel}</LuminoAttached>
}

export default Command;
