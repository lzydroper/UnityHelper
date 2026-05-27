# OpenWebUI 本地源码部署

Date: 2026-05-27
Code: 26052703
Type: Feature

## Summary

将 `FrontEnd` 从仅使用 OpenWebUI 官方 Docker 镜像扩展为本地源码部署，便于后续直接修改前端代码并保留本地开发启动脚本。

## Changes

- 在 `FrontEnd/OpenWebUI` 拉取 OpenWebUI `v0.9.5` 源码，用作后续前端定制基础。
- 使用项目本地 Node.js `22.13.1` 安装前端依赖，避免修改系统 Node。
- 使用 `uv` 安装 CPython `3.12.13` 并创建 `OpenWebUI/.venv`，安装 OpenWebUI 后端依赖。
- 新增 `start-openwebui-local.ps1` 和 `stop-openwebui-local.ps1`，用于通过后端服务启动和停止本地源码版 OpenWebUI。
- 更新 `README.md`，将本地源码部署作为主路径，Docker 镜像作为备用演示路径。
- 更新 `.gitignore`，忽略本地 Node、uv 缓存和运行日志。

## Files

- `FrontEnd/OpenWebUI`
- `FrontEnd/start-openwebui-local.ps1`
- `FrontEnd/stop-openwebui-local.ps1`
- `FrontEnd/README.md`
- `.gitignore`
- `Docs/Changes/26052703_openwebui-local-source.md`

## Verification

- 已运行 `npm ci` 安装前端依赖。
- 已运行 `uv venv .venv --python 3.12 --managed-python` 创建后端虚拟环境。
- 已运行 `uv pip install --python .venv\Scripts\python.exe -r backend\requirements.txt` 安装后端依赖。
- 已运行 `npm run build`，前端生产构建通过。
- 已运行 `.\start-openwebui-local.ps1`，`http://127.0.0.1:3000/health` 返回 `200`。
- 已确认后端托管的 WebUI 页面 `http://127.0.0.1:3000` 返回 `200`，页面 HTML 不包含 frontend-only 错误文案。

## Notes

- OpenWebUI 需要由后端服务托管前端构建产物；不要直接打开 Vite 开发端口，否则会出现 frontend-only 不受支持提示。
- `FrontEnd/OpenWebUI` 当前是本地 Git checkout，后续若需要纳入主仓库版本管理，建议转换为 fork 或 git submodule。
