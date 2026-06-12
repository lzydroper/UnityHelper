# Open WebUI Frontend

`FrontEnd` contains a local Open WebUI source deployment for frontend customization. The source checkout lives in `OpenWebUI`, and the helper scripts in this directory can run the customized app either from local source or from a project-built Docker image. The backend serves both the API and the built frontend.

## Prerequisites

For local source deployment:

- Project-local Node.js in `.node`.
- A uv-created Python virtual environment in `OpenWebUI/.venv`.

For Docker image deployment:

- Docker Desktop.
- A built `unity-open-webui:local` image, or a tar exported by `build-openwebui-docker.ps1 -SaveTar`.

For both deployment paths:

- A published Dify app.
- The Dify `OpenAI Compatible Dify App` plugin endpoint, with a URL like `https://dify.example.com/e/<hash>`.

## Configure

Create or edit the local environment file:

```powershell
Copy-Item .env.example .env
```

Edit `.env` and set:

- `DIFY_OPENAI_BASE_URL`: the Dify OpenAI-compatible endpoint base URL, without `/chat/completions`.
- `DIFY_OPENAI_API_KEY`: the API key configured in the Dify OpenAI-compatible plugin.
- `DIFY_MODEL_ID`: a local model id shown in Open WebUI, for example `unity-rag-assistant`.
- `WEBUI_SECRET_KEY`: a stable random secret. Generate one with:

```powershell
python -c "import secrets; print(secrets.token_hex(32))"
```

`FrontEnd/.env` is ignored by Git because it contains secrets.

## Local Source Deployment

Start the local source deployment:

```powershell
.\start-openwebui-local.ps1
```

Open:

```text
http://localhost:3000
```

The startup script:

- Loads Dify settings from `FrontEnd/.env`.
- Maps `DIFY_OPENAI_BASE_URL` to `OPENAI_API_BASE_URL`.
- Maps `DIFY_OPENAI_API_KEY` to `OPENAI_API_KEY`.
- Locks the visible and requested model to `DIFY_MODEL_ID`, defaulting to `unity-rag-assistant`.
- Disables direct user-managed connections.
- Disables the Calendar, Automations, Playground, update, release, and external help entry points in the customized UI.
- Serves `FrontEnd/OpenWebUI/build` through the backend service.
- Starts the backend from `FrontEnd/OpenWebUI/backend` using `OpenWebUI/.venv`.

Stop the local source deployment:

```powershell
.\stop-openwebui-local.ps1
```

Logs are written to:

```text
FrontEnd/logs
```

The local WebUI uses port `3000`. Do not open the Vite development port directly; Open WebUI shows an unsupported frontend-only warning when served that way.

After changing frontend source files under `OpenWebUI/src`, rebuild the static frontend and restart the backend service:

```powershell
$nodeBin = ".\.node\node-v22.13.1-win-x64"
$env:PATH = "$nodeBin;$env:PATH"
Set-Location .\OpenWebUI
npm run build
Set-Location ..
.\stop-openwebui-local.ps1
.\start-openwebui-local.ps1
```

## Local Docker Image Deployment

Use this path when you want to package the customized Open WebUI source into a Docker image for teammates. The build machine needs Docker and network access to download base images and npm/Python dependencies. Teammates who receive the exported tar only need Docker Desktop and `FrontEnd/.env`; they do not need local Node.js, npm dependencies, Python venv, or `npm run build`.

Build the customized image:

```powershell
.\build-openwebui-docker.ps1 -ImageTag unity-open-webui:local
```

Build and export a tar for teammates:

```powershell
.\build-openwebui-docker.ps1 -ImageTag unity-open-webui:local -SaveTar
```

If the source build fails while downloading Pyodide, PyPI, npm, or Python packages, use the faster overlay mode. It packages the existing local `OpenWebUI/build` and customized backend on top of the official Open WebUI image:

```powershell
.\build-openwebui-docker.ps1 -ImageTag unity-open-webui:local -SaveTar -OverlayOfficialImage
```

The default tar is written under:

```text
FrontEnd/docker-dist
```

On a teammate machine, import the tar:

```powershell
docker load -i .\docker-dist\unity-open-webui_local.tar
```

Start the Docker deployment:

```powershell
.\start-openwebui-docker.ps1 -ImageTag unity-open-webui:local
```

Or build and start in one step on a machine that can build images:

```powershell
.\start-openwebui-docker.ps1 -ImageTag unity-open-webui:local -Build
```

The Docker deployment uses `docker-compose.local-image.yml`, routes Open WebUI's OpenAI-compatible calls through the in-container Dify adapter at `http://127.0.0.1:8080/api/v1/dify-adapter`, and keeps the visible model locked to `DIFY_MODEL_ID`.

## Docker Image Fallback

The previous Docker image setup is still available for quick demos, but it is not the main path for frontend customization.

If Docker reports `short read`, `unexpected EOF`, or a partial GHCR download, retry the image pull first:

```powershell
docker compose --env-file .env pull open-webui
docker compose --env-file .env up -d
```

This is usually a registry or network interruption. Cloning Open WebUI source locally and building it with Docker is not recommended for this project setup because the build still needs to download base images and frontend/backend dependencies.

If repeated retries fail, set `OPEN_WEBUI_IMAGE` in `.env` to a smaller official image tag, then pull again:

```text
OPEN_WEBUI_IMAGE=ghcr.io/open-webui/open-webui:main-slim
```

The `main-slim` image is smaller, but it may download optional models or assets later on first use. For stable acceptance demos, switch back to a version-pinned tag after the network is reliable.

## Dify Connection

Open WebUI reads the Dify connection only from `FrontEnd/.env`. The customized frontend hides user-managed OpenAI/Ollama connections, and the backend rejects connection edits while `OPENWEBUI_LOCKED_MODEL_ID` is set by the startup script.

The visible model and outgoing chat payload are fixed to `DIFY_MODEL_ID`. Leave it as:

```text
DIFY_MODEL_ID=unity-rag-assistant
```

Dify's OpenAI-compatible plugin supports `/chat/completions`, but does not support `/models`. The local backend supplies the locked model id to Open WebUI, so no manual `Model IDs Filter` setup is required.

## Acceptance Test

Use the questions from `Docs/Plan/5.前后端接通与验收计划.md`:

- `Rigidbody.AddForce 怎么用？`
- `NullReferenceException 是什么原因？`
- `旧版 Input.GetAxis 怎么迁移到新输入系统？`
- Paste a C# snippet and ask for the bug.
- Continue with `那我应该怎么改？`

Then run a 10-turn conversation and record screenshots or notes for project acceptance.

## Stop

For the local source deployment:

```powershell
.\stop-openwebui-local.ps1
```

For the Docker fallback:

```powershell
docker compose down
```

For the local Docker image deployment:

```powershell
docker compose --env-file .env -f docker-compose.local-image.yml down
```
