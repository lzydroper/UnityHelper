$ErrorActionPreference = 'SilentlyContinue'

$ports = @(3000, 5300, 5173, 8080)

foreach ($port in $ports) {
    Get-NetTCPConnection -LocalPort $port -ErrorAction SilentlyContinue | ForEach-Object {
        Stop-Process -Id $_.OwningProcess -Force
    }
}

Write-Host 'Stopped local Open WebUI processes on ports 3000, 5300, 5173, and 8080.'
