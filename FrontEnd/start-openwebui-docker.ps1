[CmdletBinding()]
param(
    [string] $ImageTag = 'unity-open-webui:local',
    [switch] $Build,
    [switch] $Foreground
)

$ErrorActionPreference = 'Stop'

$frontEndRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$envFile = Join-Path $frontEndRoot '.env'
$composeFile = Join-Path $frontEndRoot 'docker-compose.local-image.yml'
$buildScript = Join-Path $frontEndRoot 'build-openwebui-docker.ps1'

if (-not (Test-Path -LiteralPath $envFile)) {
    throw "FrontEnd\.env not found. Copy FrontEnd\.env.example to FrontEnd\.env and fill Dify settings first."
}

if (-not (Test-Path -LiteralPath $composeFile)) {
    throw "Docker compose file not found: $composeFile"
}

if (-not (Get-Command docker -ErrorAction SilentlyContinue)) {
    throw 'Docker CLI was not found. Install and start Docker Desktop first.'
}

& docker version | Out-Null
if ($LASTEXITCODE -ne 0) {
    throw 'Docker is not running or the current user cannot access Docker.'
}

if ($Build) {
    & $buildScript -ImageTag $ImageTag
    if ($LASTEXITCODE -ne 0) {
        throw "Docker build failed for image: $ImageTag"
    }
} else {
    & docker image inspect $ImageTag | Out-Null
    if ($LASTEXITCODE -ne 0) {
        throw "Docker image '$ImageTag' was not found. Run .\build-openwebui-docker.ps1 or docker load a packaged tar first."
    }
}

$env:LOCAL_OPEN_WEBUI_IMAGE = $ImageTag
$openWebUiPort = '3000'

Get-Content -LiteralPath $envFile | ForEach-Object {
    $line = $_.Trim()
    if ($line.Length -eq 0 -or $line.StartsWith('#')) {
        return
    }

    $idx = $line.IndexOf('=')
    if ($idx -le 0) {
        return
    }

    $name = $line.Substring(0, $idx).Trim()
    $value = $line.Substring($idx + 1).Trim().Trim('"').Trim("'")
    if ($name -eq 'OPEN_WEBUI_PORT' -and -not [string]::IsNullOrWhiteSpace($value)) {
        $openWebUiPort = $value
    }
}

$composeArgs = @(
    'compose',
    '--env-file', $envFile,
    '-f', $composeFile,
    'up'
)

if (-not $Foreground) {
    $composeArgs += '-d'
}

& docker @composeArgs
if ($LASTEXITCODE -ne 0) {
    throw "Docker compose startup failed for image: $ImageTag"
}

Write-Host "Open WebUI Docker deployment is starting from image: $ImageTag"
Write-Host "WebUI: http://localhost:$openWebUiPort"
Write-Host 'Stop:  docker compose --env-file .env -f docker-compose.local-image.yml down'
