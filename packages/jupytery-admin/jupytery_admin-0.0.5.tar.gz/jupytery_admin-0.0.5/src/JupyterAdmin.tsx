import React from 'react';
import { Theme } from '@material-ui/core/styles';
import { makeStyles } from '@material-ui/styles';
import Paper from '@material-ui/core/Paper';
import Tabs from '@material-ui/core/Tabs';
import Tab from '@material-ui/core/Tab';
import Typography from '@material-ui/core/Typography';
import Box from '@material-ui/core/Box';
import { JupyterAuth } from '@datalayer-jupyter/auth';
import { JupyterContent } from '@datalayer-jupyter/content';
import { JupyterFederation } from '@datalayer-jupyter/federation';
import { Jupyterpool } from '@datalayer-jupyter/pool';

import './JupyterAdmin.css';

interface TabPanelProps {
  children?: React.ReactNode;
  index: any;
  value: any;
}

function TabPanel(props: TabPanelProps) {
  const { children, value, index, ...other } = props;
  return (
    <div
      role="tabpanel"
      hidden={value !== index}
      id={`simple-tabpanel-${index}`}
      aria-labelledby={`simple-tab-${index}`}
      {...other}
    >
      {value === index && (
        <Box p={3}>
          <Typography>{children}</Typography>
        </Box>
      )}
    </div>
  );
}

function a11yProps(index: any) {
  return {
    id: `simple-tab-${index}`,
    'aria-controls': `simple-tabpanel-${index}`,
  };
}

const useStyles = makeStyles((theme: Theme) => ({
  root: {
    flexGrow: 1,
    backgroundColor: theme.palette.background.paper,
  },
}));

const JupyterAdmin = () => {
  const classes = useStyles();
  const [value, setValue] = React.useState(0);

  const handleChange = (event: React.ChangeEvent<{}>, newValue: number) => {
    setValue(newValue);
  };

  return (
    <div className={classes.root}>
      <Paper square>
        <Tabs value={value} onChange={handleChange} aria-label="simple tabs example">
          <Tab label="Auth" {...a11yProps(0)} />
          <Tab label="Content" {...a11yProps(1)} />
          <Tab label="Pool" {...a11yProps(2)} />
          <Tab label="Federation" {...a11yProps(3)} />
        </Tabs>
      </Paper>
      <TabPanel value={value} index={0}>
        <JupyterAuth />
      </TabPanel>
      <TabPanel value={value} index={1}>
        <JupyterContent />
      </TabPanel>
      <TabPanel value={value} index={2}>
        <Jupyterpool />
      </TabPanel>
      <TabPanel value={value} index={3}>
        <JupyterFederation />
      </TabPanel>
    </div>
  );
}

export default JupyterAdmin;
