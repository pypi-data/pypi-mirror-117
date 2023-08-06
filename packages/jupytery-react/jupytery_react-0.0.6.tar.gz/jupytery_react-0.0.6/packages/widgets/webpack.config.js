const webpack = require("webpack");
const path = require('path');

const HtmlWebpackPlugin = require('html-webpack-plugin');
const HtmlWebpackTagsPlugin = require('html-webpack-tags-plugin');

const ModuleFederationPlugin = require("webpack").container.ModuleFederationPlugin;

const IS_PRODUCTION = process.argv.indexOf('--mode=production') > -1;
let mode = "development";
if (IS_PRODUCTION) {
  mode = "production";
}
let devtool = "inline-source-map";
if (IS_PRODUCTION) {
  devtool = false;
}
let minimize = false;
if (IS_PRODUCTION) {
  minimize = true;
}

module.exports = {
  entry: ['./src/Example'],
  mode: mode,
  watchOptions: {
    aggregateTimeout: 300,
    poll: 2000, // Seems to stabilise HMR file change detection.
    ignored: "/node_modules/"
  },
  devServer: {
    port: 3208,
    proxy: {
      '/example': {
        target: 'http://localhost:8686',
        ws: true
      },
      '/plotly.js': {
        target: 'http://localhost:8686/example/jupytery_react',
        ws: false
      },
    },
  },
  devtool: devtool,
  optimization: {
    minimize: minimize,
  },
  output: {
    publicPath: "http://localhost:3208/",
    filename: '[name].[contenthash].jupyterWidgets.js',
  },
  resolve: {
    extensions: [ '.tsx', '.ts', 'jsx', '.js' ],
    alias: { 
      "stream": "stream-browserify",
    },
  },
  module: {
    rules: [
      {
        test: /bootstrap\.tsx$/,
        loader: "bundle-loader",
        options: {
          lazy: true,
        },
      },
      {
        test: /\.tsx?$/,
        loader: "babel-loader",
        options: {
          plugins: [
            "@babel/plugin-proposal-class-properties",
          ],
          presets: [
            ["@babel/preset-react", {
                runtime: 'automatic',
                importSource: '@emotion/react'
              },
            ],
            "@babel/preset-typescript",
          ],
          cacheDirectory: true
        },
        exclude: /node_modules/,
      },
      { test: /\.css$/, use: ['style-loader', 'css-loader'] },
      { test: /\.md$/, use: 'raw-loader' },
      { test: /\.js.map$/, use: 'file-loader' },
      {
        // In .css files, svg is loaded as a data URI.
        test: /\.svg(\?v=\d+\.\d+\.\d+)?$/,
        issuer: /\.css$/,
        use: {
          loader: 'svg-url-loader',
          options: { encoding: 'none', limit: 10000 }
        }
      },
      {
        // In .ts and .tsx files (both of which compile to .js), svg files
        // must be loaded as a raw string instead of data URIs.
        test: /\.svg(\?v=\d+\.\d+\.\d+)?$/,
        issuer: /\.js$/,
        use: {
          loader: 'raw-loader'
        }
      },
      {
        test: /\.(png|jpg|gif|ttf|woff|woff2|eot)(\?v=[0-9]\.[0-9]\.[0-9])?$/,
        use: [{ loader: 'url-loader', options: { limit: 10000 } }]
      },
      {
        test: /\.m?js/,
        resolve: {
          fullySpecified: false
        }
      },
      {
        test: /\.c?js/,
        resolve: {
          fullySpecified: false
        }
      }
    ]
  },
  plugins: [
    new webpack.ProvidePlugin({
      process: 'process/browser'
    }),
    new ModuleFederationPlugin({
      name: "jupyterWidgets",
      filename: "jupyterWidgets.js",
      exposes: {
        "./Index": "./src/index",
      },
      shared: {
//        ...deps,
        react: {
          eager: false,
          singleton: true,
          requiredVersion: false
        },
        "react-dom": {
          eager: false,
          singleton: true,
          requiredVersion: false,
        },
        "react-router-dom": {
          eager: false,
          singleton: true,
          requiredVersion: false,
        },
        '@material-ui/core': { 
          eager: false,
          singleton: true,
          requiredVersion: false,
        },
        '@material-ui/styles': { 
          eager: false,
          singleton: true,
          requiredVersion: false,
        },
        "@material-ui/private-theming": {
          eager: false,
          singleton: true,
          requiredVersion: false,
        },
        '@emotion/core': {
          eager: false,
          singleton: true,
          requiredVersion: false,
        },
        '@emotion/react': {
          eager: false,
          singleton: true,
          requiredVersion: false,
        },
        '@emotion/styled': {
          eager: false,
          singleton: true,
          requiredVersion: false,
        },
      },
    }),
    new HtmlWebpackPlugin({
      title: 'Jupytery React Widgets',
      template : 'public/index.html'
    }),
    new HtmlWebpackTagsPlugin({
      links: [
        'http://maxcdn.bootstrapcdn.com/font-awesome/4.2.0/css/font-awesome.min.css',
        'https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap',
      ],
      tags: [
        'https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.4/require.min.js'
      ],
      append: false, 
      publicPath: false
    }),
  ]
};
