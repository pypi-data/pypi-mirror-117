import React from "react";
import Typography from '@material-ui/core/Typography';
// import { useDispatch } from "react-redux";
// import Button from '@material-ui/core/Button';
// import { selectCommands, commandsActions } from './CommandsRedux';

const CommandControl: React.FC = () => {
//  const commands = selectCommands();
//  const dispatch = useDispatch();
  return (
    <>
      <Typography variant="h5" gutterBottom>
        Commands Control
      </Typography>
{/*
      <div>
        <Button 
          variant="outlined"
          color="primary"
          onClick={() => dispatch(commandsActions.execute.started())}
          >
            Execute
        </Button>
        <Button 
          variant="outlined"
          color="secondary"
          onClick={() => dispatch(commandsActions.outputs.started(0))}
          >
            Reset Outputs
        </Button>
      </div>
      <Typography variant="subtitle1" gutterBottom>
        Commands: {commands.outputs}
      </Typography>
*/}
    </>
  );
}

export default CommandControl;
