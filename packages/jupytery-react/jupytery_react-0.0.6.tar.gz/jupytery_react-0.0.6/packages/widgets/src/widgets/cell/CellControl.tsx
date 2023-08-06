import React from "react";
import { useDispatch } from "react-redux";
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';
import { selectCell, cellActions } from './CellRedux';

const CellControl: React.FC = () => {
  const cell = selectCell();
  const dispatch = useDispatch();
  return (
    <>
      <Typography variant="h5" gutterBottom>
        Cell Control
      </Typography>
      <div>
        <Button
          variant="contained"
          color="primary"
          onClick={() => dispatch(cellActions.execute.started())}
          >
            Execute
        </Button>
        <Button
          variant="outlined"
          color="secondary"
          onClick={() => dispatch(cellActions.outputsCount.started(0))}
          >
            Reset outputs count
        </Button>
      </div>
      <Typography variant="subtitle1" gutterBottom>
        Outputs count: {cell.outputsCount}
      </Typography>
    </>
  );
}

export default CellControl;
