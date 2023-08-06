import React from 'react';
import { render } from 'react-dom';
import { StylesProvider } from '@material-ui/styles';
import Stack from '@material-ui/core/Stack';
import Button from '@material-ui/core/Button';
import Box from '@material-ui/core/Box';
import Slider from '@material-ui/core/Slider';
import VolumeDown from '@material-ui/icons/VolumeDown';
import VolumeUp from '@material-ui/icons/VolumeUp';
import Switch from '@material-ui/core/Switch';
import { ThemeProvider } from '@material-ui/core/styles';
import Typography from '@material-ui/core/Typography';
import { CacheProvider } from '@emotion/react';
import lightTheme from './lightTheme';
import setupMui from './MuiSetup';

const TypographyExample = () => {
  return (<Box sx={{ width: '100%', maxWidth: 500 }}>
    <Typography variant="h1" component="div" gutterBottom>
      h1. Heading
    </Typography>
    <Typography variant="h2" gutterBottom component="div">
      h2. Heading
    </Typography>
  </Box>
  );
}

const label = { inputProps: { 'aria-label': 'Switch demo' } };

const BasicSwitchesExample = () => {
  return (
    <div>
      <Switch {...label} defaultChecked />
      <Switch {...label} />
      <Switch {...label} disabled defaultChecked />
      <Switch {...label} disabled />
    </div>
  );
}

const ContinuousSliderExample = () => {
  const [value, setValue] = React.useState(30);
  const handleChange = (event: any, newValue: any) => {
    setValue(newValue);
  };
  return (
    <Box sx={{ width: 200 }}>
      <Stack spacing={2} direction="row" sx={{ mb: 1 }} alignItems="center">
        <VolumeDown />
        <Slider aria-label="Volume" value={value} onChange={handleChange} />
        <VolumeUp />
      </Stack>
      <Slider disabled defaultValue={30} aria-label="Disabled slider" />
    </Box>
  );
}

const ButtonExample = () => <Stack spacing={2} direction="row">
  <Button variant="text" color="primary">Text Primary</Button>
  <Button variant="contained" color="primary">Contained  Primary</Button>
  <Button variant="outlined" color="primary">Outlined Primary</Button>
  <Button variant="text" color="secondary">Text Secondary</Button>
  <Button variant="contained" color="secondary">Contained Secondary</Button>
  <Button variant="outlined" color="secondary">Outlined Secondary</Button>
  <Button variant="text" color="error">Text Error</Button>
  <Button variant="contained" color="error">Contained Error</Button>
  <Button variant="outlined" color="error">Outlined Error</Button>
</Stack>

const { jss, cache } = setupMui('datalayer-jss-insertion-point');


const Example = () => <CacheProvider value={cache}>
  <StylesProvider jss={jss}>
    <ThemeProvider theme={lightTheme}>
      <TypographyExample/>
      <BasicSwitchesExample/>
      <ContinuousSliderExample/>
      <ButtonExample/>
    </ThemeProvider>
  </StylesProvider>
</CacheProvider>

const div = document.createElement('div');
document.body.appendChild(div);

render(
  <>
    <Example/>    
  </>
  ,
  div
);

export default Example;
