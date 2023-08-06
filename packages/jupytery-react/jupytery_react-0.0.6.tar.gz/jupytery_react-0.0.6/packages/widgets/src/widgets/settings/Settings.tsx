import SettingsLumino from './SettingsLumino';
import LuminoAttached from '../../lumino/LuminoAttached';
import Typography from '@material-ui/core/Typography';

import '@jupyterlab/theme-light-extension/style/theme.css';
import '@jupyterlab/theme-light-extension/style/variables.css';

import './Settings.css';

const Settings = () => {
  const settingsLumino = new SettingsLumino();
  return <>
    <Typography variant="h5" gutterBottom>
    </Typography>
    <LuminoAttached>{settingsLumino.panel}</LuminoAttached>
  </>
}

export default Settings;
