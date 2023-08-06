[![Datalayer](https://raw.githubusercontent.com/datalayer/datalayer/main/res/logo/datalayer-25.svg?sanitize=true)](https://datalayer.io)

# 🛡️ Jupytery Auth

The `Jupytery Auth` library provides integrated authentication and autorization to [Jupyter Server](https://github.com/jupyter-server/jupyter_server).

It depends on a Jupyter Server [open draft WIP pull request](https://github.com/jupyter-server/jupyter_server/pull/391).

## GitHub Auth

To use it with GitHub authentication, you need to create a [GitHub OAuth application](https://docs.github.com/en/developers/apps/creating-an-oauth-app) in your GitHub profile and export in your shell environment the GitHub client id and secret as the callback url as variable.

```bash
export GITHUB_CLIENT_ID=<oauth-app-client-id>
export GITHUB_CLIENT_SECRET=<oauth-app-client-secret>
export GITHUB_OAUTH_CALLBACK_URL=<oauth-calllback-url> # http://localhost:8686/example/login
```

Set the Callback URL to `http://localhost:8686/example/ogin`, assuming you are running the Jupyter Server on port 8686.

![](https://raw.githubusercontent.com/datalayer/jupyter/auth/main/docs/images/oauth-app-example.png)

## Environment

```bash
# Setup your development environment.
conda deactivate && \
  make env-rm # If you want to reset your env.
# Create your conda environment.
make env && \
  conda activate jupytery-auth
```

```bash
# Clean, install and build jupytery_auth.
make clean && \
  make install && \
  make build
```

```bash
# Start both jupyterlab in watch mode and start the extension compilation in watch mode.
echo open http://localhost:8686/example
make start
```

![](https://raw.githubusercontent.com/datalayer/datalayer/tree/main/src/jupyter/auth/docs/images/auth-user.png)
