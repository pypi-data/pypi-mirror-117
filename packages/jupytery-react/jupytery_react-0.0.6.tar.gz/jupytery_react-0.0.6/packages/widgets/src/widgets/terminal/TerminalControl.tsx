import React from 'react';
import { useDispatch } from "react-redux";
import Switch from '@material-ui/core/Switch';
import Typography from '@material-ui/core/Typography';
import FormGroup from '@material-ui/core/FormGroup';
import FormControlLabel from '@material-ui/core/FormControlLabel';
import { terminalActions } from './TerminalRedux';

const TerminalControl: React.FC = () => {
  const dispatch = useDispatch();
  const [state, setState] = React.useState({
    dark: false,
  });
  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    dispatch(terminalActions.dark.started(event.target.checked));
    setState({ ...state, [event.target.name]: event.target.checked });
  };
  return (
    <>
      <Typography variant="h5" gutterBottom>
        Terminal Control
      </Typography>
      <FormGroup row>
        <FormControlLabel
          control={<Switch checked={state.dark} onChange={handleChange} name="dark" />}
          label="Dark mode"
        />
      </FormGroup>
    </>
  );
}

export default TerminalControl;
