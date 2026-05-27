# Open WebUI Frontend

`FrontEnd` uses the official Open WebUI Docker image as the chat frontend for the Unity development assistant. It connects to the Dify RAG app through Dify's OpenAI-compatible endpoint.

## Prerequisites

- Docker and Docker Compose.
- A published Dify app.
- The Dify `OpenAI Compatible Dify App` plugin endpoint, with a URL like `https://dify.example.com/e/<hash>`.

## Configure

Create a local environment file:

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

## Start

Validate the Compose file:

```powershell
docker compose --env-file .env config
```

Start Open WebUI:

```powershell
docker compose --env-file .env up -d
```

Check the service:

```powershell
docker compose ps
docker compose logs --tail=100 open-webui
```

Open `http://localhost:3000`. The first registered user becomes the administrator.

## Pull Troubleshooting

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

## Connect Dify

Open WebUI reads `OPENAI_API_BASE_URL` and `OPENAI_API_KEY` from `.env`, mapped from the Dify settings. If the connection does not appear automatically or needs adjustment:

1. Open `Admin Settings`.
2. Go to `Connections` > `OpenAI`.
3. Add or edit the OpenAI-compatible connection.
4. Set the URL to the value of `DIFY_OPENAI_BASE_URL`.
5. Set the API key to the value of `DIFY_OPENAI_API_KEY`.
6. Add `DIFY_MODEL_ID` to `Model IDs (Filter)`.
7. Save the connection.

Dify's OpenAI-compatible plugin supports `/chat/completions`, but does not support `/models`. Open WebUI may report a model discovery or verification issue; keep the manual `Model IDs (Filter)` entry and verify chat completion directly.

## Acceptance Test

Use the questions from `Docs/Plan/5.前后端接通与验收计划.md`:

- `Rigidbody.AddForce 怎么用？`
- `NullReferenceException 是什么原因？`
- `旧版 Input.GetAxis 怎么迁移到新输入系统？`
- Paste a C# snippet and ask for the bug.
- Continue with `那我应该怎么改？`

Then run a 10-turn conversation and record screenshots or notes for project acceptance.

## Stop

```powershell
docker compose down
```

To remove local Open WebUI data, use:

```powershell
docker compose down -v
```
