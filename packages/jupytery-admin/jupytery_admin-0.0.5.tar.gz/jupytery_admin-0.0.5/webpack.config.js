const HtmlWebpackPlugin = require("html-webpack-plugin");
const webpack = require("webpack");
const path = require("path");

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
let publicPath = "http://localhost:2003/";
if (IS_PRODUCTION) {
  publicPath = "./jupytery-admin-static/js/";
}
/*
let outputPath = path.resolve(__dirname, "dist", "jupytery-admin-static", "js");
if (IS_PRODUCTION) {
  outputPath = path.resolve(__dirname, "dist");
}
*/
module.exports = {
  entry: "./src/JupyterAdminView",
  mode: mode,
  watchOptions: {
    aggregateTimeout: 300,
    poll: 2000, // Seems to stabilise HMR file change detection
    ignored: "/node_modules/"
  },
  devServer: {
    static: path.join(__dirname, "dist"),
    port: 2003,
    historyApiFallback: true,
    proxy: {
      '/hub': 'http://localhost:8686',
    },
//    before: (app, server) => {
//      var user_data = JSON.parse('[{"kind":"user","name":"foo","admin":true,"groups":[],"server":"/user/foo/","pending":null,"created":"2020-12-07T18:46:27.112695Z","last_activity":"2020-12-07T21:00:33.336354Z","servers":{"":{"name":"","last_activity":"2020-12-07T20:58:02.437408Z","started":"2020-12-07T20:58:01.508266Z","pending":null,"ready":true,"state":{"pid":28085},"url":"/user/foo/","user_options":{},"progress_url":"/hub/api/users/foo/server/progress"}}},{"kind":"user","name":"bar","admin":false,"groups":[],"server":null,"pending":null,"created":"2020-12-07T18:46:27.115528Z","last_activity":"2020-12-07T20:43:51.013613Z","servers":{}}]')
//      var group_data = JSON.parse('[{"kind":"group","name":"testgroup","users":[]}, {"kind":"group","name":"testgroup2","users":["foo", "bar"]}]')
//      app.use(express.json())
//      app.get("/hub/api/users", (req, res) => { res.set("Content-Type", "application/json").send(JSON.stringify(user_data)) })
//      app.get("/hub/api/groups", (req, res) => { res.set("Content-Type", "application/json").send(JSON.stringify(group_data)) })
//      app.post("/hub/api/groups/*/users", (req, res) => { console.log(req.url, req.body); res.status(200).end() })
//      app.delete("/hub/api/groups/*", (req, res) => { console.log(req.url, req.body); res.status(200).end() })
//      app.post("/hub/api/users", (req, res) => { console.log(req.url, req.body); res.status(200).end() })
//      app.delete("/hub/api/users", (req, res) => { console.log(req.url, req.body); res.status(200).end() })
//      app.post("/hub/api/users/*/server", (req, res) => { console.log(req.url, req.body); res.status(200).end() })
//      app.delete("/hub/api/users/*/server", (req, res) => { console.log(req.url, req.body); res.status(200).end() })
//      app.post("/hub/api/shutdown", (req, res) => { console.log(req.url, req.body); res.status(200).end() })
//    }
  },
  devtool: devtool,
  optimization: {
    minimize: minimize,
  },
  output: {
//    path: outputPath,
    publicPath: publicPath,
    filename: 'jupytery-admin.js',
  },
  resolve: {
    extensions: [".ts", ".tsx", ".js", ".jsx"],
    alias: { 
      path: "path-browserify"
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
            "@babel/preset-react",
            "@babel/preset-typescript"
          ],
          cacheDirectory: true
        }
      },
      {
        test: /\.jsx?$/,
        loader: "babel-loader",
        options: {
          plugins: [
            "@babel/plugin-proposal-class-properties",
          ],
          presets: [
            "@babel/preset-react"
          ],
          cacheDirectory: true
        }
      },
      {
        test: /\.s[ac]ss(\?v=\d+\.\d+\.\d+)?$/i,
        use: ['style-loader', 'css-loader', 'sass-loader'],
      },
      {
        test: /\.css?$/i,
        use: ['style-loader', 'css-loader'],
      },
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
        test: /\.svg(\?v=\d+\.\d+\.\d+)?$/,
        issuer: /\.tsx$/,
        use: [
          '@svgr/webpack'
        ],
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
        test: /\.(png|jpg|jpeg|gif|ttf|woff|woff2|eot)(\?v=[0-9]\.[0-9]\.[0-9])?$/,
        use: [{ loader: 'url-loader', options: { limit: 10000 } }],
      },
     ]
  },
  plugins: [
    new webpack.DefinePlugin({
      "process.env": "{}"
    }),
    new HtmlWebpackPlugin({
      template: "./public/index.html",
    }),
  ],
};
