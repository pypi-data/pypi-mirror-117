import { useState } from 'react';
import { useDispatch } from 'react-redux';
import PlayArrow from '@material-ui/icons/PlayArrowOutlined';
import Delete from '@material-ui/icons/DeleteOutline';
import Typography from '@material-ui/core/Typography';
import ArrowUpwardIcon from '@material-ui/icons/ArrowUpward';
import ArrowDownwardIcon from '@material-ui/icons/ArrowDownward';
import { PanelLayout } from '@lumino/widgets';
import { selectNotebook, notebookActions } from '../NotebookRedux';

const CELL_HEADER_DIV_CLASS = 'dla-cellHeaderContainer';

const CellSidebarDefault = (props: any) => {
  const [visible, setVisible] = useState(false);
  const dispatch = useDispatch();
  const paperBook = selectNotebook();
  const layout = (paperBook.activeCell?.layout)
  if (layout) {
    const selectedCellSidebar = (paperBook.activeCell?.layout as PanelLayout).widgets[0];
    if (!visible && (selectedCellSidebar.id === props.id)) {
      setVisible(true);
    }
    if (visible && (selectedCellSidebar.id !== props.id)) {
      setVisible(false);
    }
  }
  if (!visible) {
    return <div></div>
  }
  return (
    <div className={CELL_HEADER_DIV_CLASS}>
      <div
        onClick={event => {
          dispatch(notebookActions.run.started());
        }}
      >
        <span style={{ display: "flex" }}>
          <PlayArrow fontSize="small" />
          <Typography variant="body2" color="textSecondary">Render</Typography>
        </span>
      </div>
      <div
        onClick={event => {
          dispatch(notebookActions.insertAbove.started());
        }}
      >
        <span style={{ display: "flex" }}>
          <ArrowUpwardIcon fontSize="small" />
          <Typography variant="body2" color="textSecondary">Add above</Typography>
        </span>
      </div>
      <div
        onClick={event => {
          dispatch(notebookActions.insertBelow.started());
        }}
      >
        <span style={{ display: "flex" }}>
          <ArrowDownwardIcon fontSize="small" />
          <Typography variant="body2" color="textSecondary">Add below</Typography>
        </span>
      </div>
      <div
        onClick={event => {
          dispatch(notebookActions.delete.started(undefined));
        }}
      >
        <span style={{ display: "flex" }}>
          <Delete fontSize="small" />
          <Typography variant="body2" color="textSecondary">Delete</Typography>
        </span>
      </div>
    </div>
  );
}

export default CellSidebarDefault;
