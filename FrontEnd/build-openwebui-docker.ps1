[CmdletBinding()]
param(
    [string] $ImageTag = 'unity-open-webui:local',
    [switch] $OverlayOfficialImage,
    [string] $BaseImage = 'ghcr.io/open-webui/open-webui:v0.9.5',
    [switch] $NoCache,
    [switch] $FullModelCache,
    [switch] $SaveTar,
    [string] $TarPath,
    [string] $Platform,
    [string[]] $BuildArg = @()
)

$ErrorActionPreference = 'Stop'

$frontEndRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$sourceRoot = Join-Path $frontEndRoot 'OpenWebUI'
$dockerfile = Join-Path $sourceRoot 'Dockerfile'
$dockerfileForBuild = $dockerfile
$contextRoot = $sourceRoot

if (-not (Test-Path -LiteralPath $sourceRoot)) {
    throw "Open WebUI source directory not found: $sourceRoot"
}

if (-not $OverlayOfficialImage -and -not (Test-Path -LiteralPath $dockerfile)) {
    throw "Open WebUI Dockerfile not found: $dockerfile"
}

$tempBuildRoot = Join-Path $frontEndRoot '.docker-build'

if ($OverlayOfficialImage) {
    $frontendBuild = Join-Path $sourceRoot 'build\index.html'
    if (-not (Test-Path -LiteralPath $frontendBuild)) {
        throw "Local frontend build not found: $frontendBuild. Run npm run build locally before using -OverlayOfficialImage."
    }

    $contextRoot = Join-Path $tempBuildRoot 'overlay-context'
    if (Test-Path -LiteralPath $contextRoot) {
        Remove-Item -LiteralPath $contextRoot -Recurse -Force
    }

    New-Item -ItemType Directory -Force -Path $contextRoot | Out-Null
    Copy-Item -LiteralPath (Join-Path $sourceRoot 'build') -Destination (Join-Path $contextRoot 'build') -Recurse -Force
    Copy-Item -LiteralPath (Join-Path $sourceRoot 'backend') -Destination (Join-Path $contextRoot 'backend') -Recurse -Force
    Copy-Item -LiteralPath (Join-Path $sourceRoot 'package.json') -Destination (Join-Path $contextRoot 'package.json') -Force
    Copy-Item -LiteralPath (Join-Path $sourceRoot 'CHANGELOG.md') -Destination (Join-Path $contextRoot 'CHANGELOG.md') -Force

    $backendData = Join-Path $contextRoot 'backend\data'
    if (Test-Path -LiteralPath $backendData) {
        Remove-Item -LiteralPath $backendData -Recurse -Force
    }

    $dockerfileForBuild = Join-Path $contextRoot 'Dockerfile'
    $overlayDockerfileLines = @(
        "FROM $BaseImage",
        'USER root',
        'WORKDIR /app/backend',
        'COPY ./build /app/build',
        'COPY ./CHANGELOG.md /app/CHANGELOG.md',
        'COPY ./package.json /app/package.json',
        'COPY ./backend /app/backend'
    )

    $utf8NoBom = New-Object System.Text.UTF8Encoding($false)
    [System.IO.File]::WriteAllLines($dockerfileForBuild, [string[]] $overlayDockerfileLines, $utf8NoBom)
} else {
    $firstDockerfileLine = Get-Content -LiteralPath $dockerfile -TotalCount 1
    if ($firstDockerfileLine -match '^\s*#\s*syntax=') {
        $tempDockerfile = Join-Path $tempBuildRoot 'Dockerfile.no-syntax'
        New-Item -ItemType Directory -Force -Path $tempBuildRoot | Out-Null

        $dockerfileLines = Get-Content -LiteralPath $dockerfile | Select-Object -Skip 1
        $utf8NoBom = New-Object System.Text.UTF8Encoding($false)
        [System.IO.File]::WriteAllLines($tempDockerfile, [string[]] $dockerfileLines, $utf8NoBom)
        $dockerfileForBuild = $tempDockerfile
    }
}

if (-not (Get-Command docker -ErrorAction SilentlyContinue)) {
    throw 'Docker CLI was not found. Install and start Docker Desktop first.'
}

& docker version | Out-Null
if ($LASTEXITCODE -ne 0) {
    throw 'Docker is not running or the current user cannot access Docker.'
}

$buildHash = "local-$(Get-Date -Format 'yyyyMMddHHmmss')"
try {
    $gitHash = & git -C $frontEndRoot rev-parse --short HEAD 2>$null
    if ($LASTEXITCODE -eq 0 -and -not [string]::IsNullOrWhiteSpace($gitHash)) {
        $buildHash = $gitHash.Trim()
    }
} catch {
    # Git is optional for local packaging; the timestamp hash above is enough.
}

$useSlim = if ($FullModelCache) { 'false' } else { 'true' }

$dockerArgs = @(
    'build',
    '--file', $dockerfileForBuild,
    '--tag', $ImageTag,
    '--build-arg', "BUILD_HASH=$buildHash",
    '--build-arg', "USE_SLIM=$useSlim"
)

if ($NoCache) {
    $dockerArgs += '--no-cache'
}

if (-not [string]::IsNullOrWhiteSpace($Platform)) {
    $dockerArgs += @('--platform', $Platform)
}

foreach ($arg in $BuildArg) {
    if (-not [string]::IsNullOrWhiteSpace($arg)) {
        $dockerArgs += @('--build-arg', $arg)
    }
}

$dockerArgs += $contextRoot

Write-Host "Building Docker image: $ImageTag"
Write-Host "Build hash: $buildHash"
Write-Host "Context:    $contextRoot"
Write-Host "Dockerfile: $dockerfileForBuild"
if ($OverlayOfficialImage) {
    Write-Host "Base image: $BaseImage"
    Write-Host 'Mode:       overlay official image with local build'
}
Write-Host "Slim mode:  $useSlim"

& docker @dockerArgs
if ($LASTEXITCODE -ne 0) {
    throw "Docker build failed for image: $ImageTag"
}

if ($SaveTar) {
    if ([string]::IsNullOrWhiteSpace($TarPath)) {
        $distRoot = Join-Path $frontEndRoot 'docker-dist'
        New-Item -ItemType Directory -Force -Path $distRoot | Out-Null
        $safeTag = $ImageTag -replace '[^\w.-]+', '_'
        $TarPath = Join-Path $distRoot "$safeTag.tar"
    } else {
        $tarParent = Split-Path -Parent $TarPath
        if (-not [string]::IsNullOrWhiteSpace($tarParent)) {
            New-Item -ItemType Directory -Force -Path $tarParent | Out-Null
        }
    }

    Write-Host "Saving Docker image tar: $TarPath"
    & docker save --output $TarPath $ImageTag
    if ($LASTEXITCODE -ne 0) {
        throw "Docker save failed for image: $ImageTag"
    }
}

Write-Host 'Docker image packaging completed.'
Write-Host "Run locally: .\start-openwebui-docker.ps1 -ImageTag $ImageTag"
if ($SaveTar) {
    Write-Host "Teammate import: docker load -i `"$TarPath`""
}
