import React, { useEffect } from "react";
import { Provider } from "react-redux";
import { createStore } from "redux";
import { BrowserRouter, Routes, Route } from "react-router-dom";

import { initialState, reducers } from "../redux/Store";
import { jhapiRequest } from "./util/jhapiUtil";

import ServerDashboard from "./components/ServerDashboard/ServerDashboard";
import Groups from "./components/Groups/Groups";
import GroupEdit from "./components/GroupEdit/GroupEdit";
import CreateGroup from "./components/CreateGroup/CreateGroup";
import AddUser from "./components/AddUser/AddUser";
import EditUser from "./components/EditUser/EditUser";

import "./JupyterHubAdmin.css";

const store = createStore(reducers, initialState);

const JupyterHubAdmin = () => {
  useEffect(() => {
    let { limit, user_page, groups_page } = initialState;
    jhapiRequest(`/users?offset=${user_page * limit}&limit=${limit}`, "GET")
      .then((data) => data.json())
      .then((data) =>
        store.dispatch({ type: "USER_PAGE", value: { data: data, page: 0 } })
      )
      .catch((err) => console.log(err));
    jhapiRequest(`/groups?offset=${groups_page * limit}&limit=${limit}`, "GET")
      .then((data) => data.json())
      .then((data) =>
        store.dispatch({ type: "GROUPS_PAGE", value: { data: data, page: 0 } })
      )
      .catch((err) => console.log(err));
  });
  return (
    <div className="resets">
      <Provider store={store}>
        <BrowserRouter>
          <Routes>
          <Route
              path="/"
              element={<ServerDashboard/>}
            />
            <Route
              path="/hub/jupytery-admin-ui"
              element={<ServerDashboard/>}
            />
            <Route 
              path="/groups" 
              element={<Groups/>} />
            <Route
              path="/group-edit"
              element={<GroupEdit/>}
            />
            <Route
              path="/create-group"
              element={<CreateGroup/>}
            />
            <Route
              path="/add-users"
              element={<AddUser/>}
            />
            <Route
              path="/edit-user"
              element={<EditUser/>}
            />
          </Routes>
        </BrowserRouter>
      </Provider>
    </div>
  );
};

export default JupyterHubAdmin;
