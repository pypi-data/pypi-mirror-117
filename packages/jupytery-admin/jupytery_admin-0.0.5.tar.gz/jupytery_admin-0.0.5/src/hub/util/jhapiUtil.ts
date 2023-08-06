export const jhapiRequest = (endpoint: string, method: string, data?: any) => {
  return fetch("/hub/api" + endpoint, {
    method: method,
    headers: {
      "Content-Type": "application/json",
      "Authorization": `Bearer ${(window as any).jupyterhub_api_token}`
    },
    body: data ? JSON.stringify(data) : null,
  });
};
