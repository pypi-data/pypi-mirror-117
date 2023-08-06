import React from "react";
import { useDispatch } from "react-redux";
import Button from '@material-ui/core/Button';
import PlayCircleOutline from '@material-ui/icons/PlayCircleOutline';
import SaveOutlined from '@material-ui/icons/SaveOutlined';
import Typography from '@material-ui/core/Typography';
import { notebookActions } from './NotebookRedux';

const NotebookControl: React.FC = () => {
  const dispatch = useDispatch();
  return (
    <>
      <Typography variant="h5" gutterBottom>
        Notebook Control
      </Typography>
      <>
        <Button
          variant="outlined"
          color="secondary"
          startIcon={<PlayCircleOutline />}
          onClick={() => dispatch(notebookActions.run.started())}
          >
            Execute
        </Button>
      </>
      <Button 
        variant="outlined"
        color="secondary"
        startIcon={<SaveOutlined />}
        onClick={() => dispatch(notebookActions.save.started())}
        >
          Save
      </Button>
      <Typography variant="subtitle1" gutterBottom>
        {/* Notebook: {notebook.notebookChange.cellsChange} */}
      </Typography>
    </>
  );
}

export default NotebookControl;
