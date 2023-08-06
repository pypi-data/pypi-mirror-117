import { useJupyter } from '../../jupyter/JupyterContext';

const HelloJupyter = () => {
  const { variant, setVariant } = useJupyter();
  return (
    <div style={{ backgroundColor: variant }}>
      <select value={variant} onChange={e => setVariant(e.currentTarget.value)}>
          <option value="white">White</option>
          <option value="lightblue">Blue</option>
          <option value="lightgreen">Green</option>
      </select>
      <div>Hello Jupyter {variant}!</div>
    </div>
  );
};
  
export default HelloJupyter;
