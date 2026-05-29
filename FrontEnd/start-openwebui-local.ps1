$ErrorActionPreference = 'Stop'

$frontEndRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$sourceRoot = Join-Path $frontEndRoot 'OpenWebUI'
$nodeRoot = Join-Path $frontEndRoot '.node\node-v22.13.1-win-x64'
$venvPython = Join-Path $sourceRoot '.venv\Scripts\python.exe'
$envFile = Join-Path $frontEndRoot '.env'
$logsRoot = Join-Path $frontEndRoot 'logs'
$frontendBuild = Join-Path $sourceRoot 'build\index.html'

if (-not (Test-Path -LiteralPath $sourceRoot)) {
    throw "Open WebUI source directory not found: $sourceRoot"
}

if (-not (Test-Path -LiteralPath $nodeRoot)) {
    throw "Project-local Node.js not found: $nodeRoot"
}

if (-not (Test-Path -LiteralPath $venvPython)) {
    throw "Open WebUI Python virtual environment not found: $venvPython"
}

if (-not (Test-Path -LiteralPath $frontendBuild)) {
    throw "Open WebUI frontend build not found: $frontendBuild. Run npm run build inside FrontEnd\OpenWebUI first."
}

New-Item -ItemType Directory -Force -Path $logsRoot | Out-Null

function Import-DotEnv {
    param([string] $Path)

    if (-not (Test-Path -LiteralPath $Path)) {
        return
    }

    Get-Content -LiteralPath $Path | ForEach-Object {
        $line = $_.Trim()
        if ($line.Length -eq 0 -or $line.StartsWith('#')) {
            return
        }

        $idx = $line.IndexOf('=')
        if ($idx -le 0) {
            return
        }

        $name = $line.Substring(0, $idx).Trim()
        $value = $line.Substring($idx + 1).Trim()
        $value = $value.Trim('"').Trim("'")
        [Environment]::SetEnvironmentVariable($name, $value, 'Process')
    }
}

Import-DotEnv -Path $envFile

if (-not $env:DIFY_MODEL_ID) {
    $env:DIFY_MODEL_ID = 'unity-rag-assistant'
}

if ($env:DIFY_OPENAI_BASE_URL) {
    $env:OPENAI_API_BASE_URL = $env:DIFY_OPENAI_BASE_URL
    $env:OPENAI_API_BASE_URLS = $env:DIFY_OPENAI_BASE_URL
}

if ($env:DIFY_OPENAI_API_KEY) {
    $env:OPENAI_API_KEY = $env:DIFY_OPENAI_API_KEY
    $env:OPENAI_API_KEYS = $env:DIFY_OPENAI_API_KEY
}

if ($env:DIFY_MODEL_ID) {
    $env:DEFAULT_MODELS = $env:DIFY_MODEL_ID
    $env:DEFAULT_PINNED_MODELS = $env:DIFY_MODEL_ID
    $env:TASK_MODEL_EXTERNAL = $env:DIFY_MODEL_ID
    $env:OPENWEBUI_LOCKED_MODEL_ID = $env:DIFY_MODEL_ID
}

$env:ENABLE_OPENAI_API = 'true'
$env:ENABLE_DIRECT_CONNECTIONS = 'false'
$env:ENABLE_PERSISTENT_CONFIG = 'false'
$env:ENABLE_OLLAMA_API = 'false'
$env:ENABLE_CALENDAR = 'false'
$env:ENABLE_AUTOMATIONS = 'false'
$env:ENABLE_EVALUATION_ARENA_MODELS = 'false'
$env:ENABLE_COMMUNITY_SHARING = 'false'
$env:ENABLE_VERSION_UPDATE_CHECK = 'false'
$env:USER_PERMISSIONS_CHAT_MULTIPLE_MODELS = 'false'
$env:USER_PERMISSIONS_FEATURES_DIRECT_TOOL_SERVERS = 'false'
$env:BYPASS_MODEL_ACCESS_CONTROL = 'true'
$env:WEBUI_BANNERS = '[]'
$env:OPEN_WEBUI_PORT = if ($env:OPEN_WEBUI_PORT) { $env:OPEN_WEBUI_PORT } else { '3000' }
$env:WEBUI_URL = "http://localhost:$env:OPEN_WEBUI_PORT"
$env:FRONTEND_BUILD_DIR = Join-Path $sourceRoot 'build'
$env:CORS_ALLOW_ORIGIN = "http://localhost:$env:OPEN_WEBUI_PORT"
$env:PORT = $env:OPEN_WEBUI_PORT
$env:HOST = '127.0.0.1'
$env:PYTHONPATH = Join-Path $sourceRoot 'backend'
$env:PATH = "$nodeRoot;$env:PATH"

$backendOutLog = Join-Path $logsRoot 'openwebui-backend.out.log'
$backendErrLog = Join-Path $logsRoot 'openwebui-backend.err.log'

$backendArgs = @(
    '-NoProfile',
    '-ExecutionPolicy', 'Bypass',
    '-Command',
    "Set-Location -LiteralPath '$sourceRoot\backend'; & '$venvPython' -m uvicorn open_webui.main:app --host 127.0.0.1 --port $env:OPEN_WEBUI_PORT"
)

Start-Process -FilePath 'powershell' -ArgumentList $backendArgs -WindowStyle Hidden -RedirectStandardOutput $backendOutLog -RedirectStandardError $backendErrLog

Write-Host 'Open WebUI local source deployment is starting from the backend service.'
Write-Host "WebUI:    http://localhost:$env:OPEN_WEBUI_PORT"
Write-Host "Backend:  http://localhost:$env:OPEN_WEBUI_PORT"
Write-Host "Logs:     $logsRoot"
