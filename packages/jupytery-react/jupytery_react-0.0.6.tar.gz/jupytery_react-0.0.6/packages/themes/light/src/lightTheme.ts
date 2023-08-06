import { createTheme } from '@material-ui/core/styles';
import { Direction, ThemeOptions, Theme } from '@material-ui/system';
import { createBreakpoints, Breakpoints } from '@material-ui/system';
import createMixins, { Mixins } from '@material-ui/core/styles/createMixins';
import createPalette, { Palette } from '@material-ui/core/styles/createPalette';
import createTypography, { Typography } from '@material-ui/core/styles/createTypography';
import shadows from '@material-ui/core/styles/shadows';
import { ShapeOptions } from '@material-ui/system';
import { createSpacing, Spacing } from '@material-ui/system';
import { Transitions } from '@material-ui/core/styles';
import { ZIndex } from '@material-ui/core/styles/zIndex';

// import green from '@material-ui/core/colors/green';
// import blue from '@material-ui/core/colors/blue';
import yellow from '@material-ui/core/colors/yellow';
// import red from '@material-ui/core/colors/red';

const white = '#fff';

const direction: Direction = 'ltr';

const breakpoints: Breakpoints = createBreakpoints({
  unit: 'px',
  step: 2,
});

const palette: Palette = createPalette({
//  mode: "dark",
/*
  primary: {
    light: blue.A200,
    main: blue.A400,
    dark: white,
    contrastText: yellow.A400,
  },
*/
  primary: {
    light: '#00acc1',
    main: '#00acc1',
    dark: white,
    contrastText: yellow.A400,
  },
/*
  secondary: {
    light: white,
    main: green.A400,
    dark: white,
    contrastText: blue.A700,
  },
*/
  secondary: {
    light: white,
    main: '#4caf50',
    dark: white,
    contrastText: yellow.A400,
  },
/*
  error: {
    light: white,
    main: red.A400,
    dark: white,
    contrastText: yellow.A400
  },
*/
  error: {
    light: white,
    main: '#f44336',
    dark: white,
    contrastText: yellow.A400
  },
  background: {
    default: white,
    paper: white
  },
});

// const shadows: Shadow = [];

const shape: ShapeOptions = {
  borderRadius: 3,
};

const spacing: Spacing = createSpacing(1);

const transitions: Partial<Transitions> = {};

const typography: Partial<Typography> = createTypography(palette, {
  fontFamily: '"Roboto", "Helvetica", "Arial", sans-serif',
  fontSize: 13, // px
  fontWeightLight: 300,
  fontWeightRegular: 400,
  fontWeightMedium: 500,
  fontWeightBold: 700,
  // Tell Material-UI what's the font-size on the html element.
  // 16px is the default font-size used by browsers.
  htmlFontSize: 16,
  // Apply the CSS properties to all the variants.
  allVariants: {
    textTransform: 'inherit',
  }
});

const zIndex: Partial<ZIndex> = {};

const mixins: Mixins = createMixins(breakpoints, spacing, {});

const components = {
  MuiButtonBase: {
    defaultProps: {
      disableRipple: true, // 'ondulation'
//      borderRadius: 0,
    },
    styleOverrides: {
      root: {
//        borderRadius: 0,
      },
    },
  },
  MuiButton: {
    defaultProps: {
      size: 'small',
    },
    styleOverrides: {
//      root: {
//        borderRadius: 0,
//      },
//      sizeSmall: {
//        // https://github.com/mui-org/material-ui/pull/24253
//        backgroundColor: "red"
//      },
    },
  },
  MuiSwitch: {
    defaultProps: {
      size: 'small',
    },
  },
  MuiSlider: {
    defaultProps: {
      size: 'small',
    },
  },
/*
  containedPrimary: {
    color: blue.A700,
    backgroundColor: white,
    '&:hover': {
      backgroundColor: white,
      // Reset on touch devices, it doesn't add specificity
      '@media (hover: none)': {
        backgroundColor: white,
      },
    }
  }
*/
};

const themeOptions: ThemeOptions = {
  shape: shape,
  breakpoints: breakpoints,
  direction: direction,
  mixins: mixins,
  palette: palette,
  shadows: shadows,
  spacing: spacing,
  transitions: transitions,
  components: components,
  typography: typography,
  zIndex: zIndex,
};

const lightTheme: Theme = createTheme(
  themeOptions as any,
);

export default lightTheme;
