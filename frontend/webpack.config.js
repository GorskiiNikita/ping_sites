const path = require('path');

module.exports = {
  module: {
    rules: [
      {
        test: /\.jsx?$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader"
        }
      }
    ]
  },
  entry: {
      main: './src/index.js',
      login: './src/login.js',
  },
    output: {
      filename: '[name].js',
      path: path.resolve(__dirname, 'static/frontend'),
    },
};

