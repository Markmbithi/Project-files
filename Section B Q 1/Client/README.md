# Polymer Client Side

### 1. Setup

##### Prerequisites

First, install [Polymer CLI](https://github.com/Polymer/polymer-cli) using
[npm](https://www.npmjs.com) (we assume you have pre-installed [node.js](https://nodejs.org)).

    npm install -g polymer-cli

Second, install [Bower](https://bower.io/) using [npm](https://www.npmjs.com)

    npm install -g bower

### 2. Navigate to the project folder from the command line
cd "Section B Q 1\client"

### 3. Start the server

This command serves the app at `http://127.0.0.1:8081` and provides basic URL
routing for the app:

    polymer serve

```
"builds": [
  {
    "preset": "es5-bundled"
  },
  {
    "preset": "es6-bundled"
  },
  {
    "preset": "es6-unbundled"
  }
]
```
