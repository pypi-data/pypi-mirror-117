[![Datalayer](https://raw.githubusercontent.com/datalayer/datalayer/main/res/logo/datalayer-25.svg?sanitize=true)](https://datalayer.io)

# 🛂 Jupyter Admin

> Jupyter Admin is a UI (Web User Interface) and CLI (Command Line Interface) to manage the Datalayer Jupyter components.

```bash
# Setup your development environment.
conda deactivate && \
  make env-rm # If you want to reset your env.
make env && \
  conda activate jupytery-admin
```

```bash
# Install a `rbac` enabled jupyterhub.
make jupyterhub-rbac
```

```bash
# Clean and install and build.
make clean
make install
make build
```

```bash
# Build and copy the javascript to the shared jupyterhub folder.
make jupyterhub-js
```

```bash
# Create an access token for your current ${USER}.
# !!! Update in `./public/index.html` the `window.jupyterhub_api_token = <token>` with the returned token value.
make jupyterhub-token
```

```bash
# Start the frontend webpack server and jupyterhub server.
echo open http://localhost:2003
echo open http://localhost:8686/hub/jupytery-admin
make start
```

```bash
# Connect to the jupyterhub local sqlite database and run e.g.
# .schema
# .tables
# .schema api_tokens
# select * from api_tokens;
make  jupyterhub-sqlite
```
