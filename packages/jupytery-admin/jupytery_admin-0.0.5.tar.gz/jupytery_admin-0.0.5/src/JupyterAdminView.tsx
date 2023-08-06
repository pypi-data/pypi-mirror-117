import React from 'react';
import { render } from 'react-dom';
import JupyterHubAdmin from './hub/JupyterHubAdmin';

render(
  <>
    <JupyterHubAdmin/>
  </>
  ,
  document.getElementById('jupytery-admin')
);
