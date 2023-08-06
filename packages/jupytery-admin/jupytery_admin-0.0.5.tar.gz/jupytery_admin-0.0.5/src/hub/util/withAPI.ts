import { jhapiRequest } from "./jhapiUtil";

const withAPI = {
  updateUsers: (offset: number, limit: number) =>
    jhapiRequest(`/users?offset=${offset}&limit=${limit}`, "GET").then((data) =>
      data.json()
    ),
  updateGroups: (offset: number, limit: number) =>
    jhapiRequest(
      `/groups?offset=${offset}&limit=${limit}`,
      "GET"
    ).then((data) => data.json()),
  shutdownHub: () => jhapiRequest("/shutdown", "POST"),
  startServer: (name: string) => jhapiRequest("/users/" + name + "/server", "POST"),
  stopServer: (name: string) => jhapiRequest("/users/" + name + "/server", "DELETE"),
  startAll: (names: string[]) =>
    names.map((e) => jhapiRequest("/users/" + e + "/server", "POST")),
  stopAll: (names: string[]) =>
    names.map((e) => jhapiRequest("/users/" + e + "/server", "DELETE")),
  addToGroup: (users: string, groupname: string) =>
    jhapiRequest("/groups/" + groupname + "/users", "POST", { users }),
  removeFromGroup: (users: string[], groupname: string) =>
    jhapiRequest("/groups/" + groupname + "/users", "DELETE", { users }),
  createGroup: (groupName: string) => jhapiRequest("/groups/" + groupName, "POST"),
  deleteGroup: (name: string) => jhapiRequest("/groups/" + name, "DELETE"),
  addUsers: (usernames: string[], admin: string) =>
    jhapiRequest("/users", "POST", { usernames, admin }),
  editUser: (username: string, updated_username: string, admin: string) =>
    jhapiRequest("/users/" + username, "PATCH", {
      name: updated_username,
      admin,
    }),
  deleteUser: (username: string) => jhapiRequest("/users/" + username, "DELETE"),
  findUser: (username: string) => jhapiRequest("/users/" + username, "GET"),
  validateUser: (username: string) =>
    jhapiRequest("/users/" + username, "GET")
      .then((data) => data.status)
      .then((data) => (data > 200 ? false : true)),
  failRegexEvent: () =>
    alert(
      "Cannot change username - either contains special characters or is too short."
    ),
  noChangeEvent: () => {
    return;
  },
  refreshGroupsData: () =>
    jhapiRequest("/groups", "GET").then((data) => data.json()),
  refreshUserData: () =>
    jhapiRequest("/users", "GET").then((data) => data.json()),
};

export default withAPI;
