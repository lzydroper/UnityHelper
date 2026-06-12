# OpenWebUI Docker 打包脚本

Date: 2026-06-12
Code: 26061201
Type: Feature

## Summary

新增自定义 OpenWebUI Docker 镜像构建和启动流程，方便将当前项目定制版打包后分发给组员运行。

## Changes

- 新增 `build-openwebui-docker.ps1`，支持构建 `unity-open-webui:local` 镜像，并可通过 `-SaveTar` 导出镜像 tar。
- `build-openwebui-docker.ps1` 支持 `-OverlayOfficialImage`，可在 Docker 内源码构建网络不稳定时，复用本地 `OpenWebUI/build` 并叠加到官方 OpenWebUI 镜像上。
- 新增 `docker-compose.local-image.yml` 和 `start-openwebui-docker.ps1`，用于从本地镜像启动定制版 OpenWebUI。
- Docker 运行配置会将 OpenAI 兼容调用路由到容器内的 Dify adapter，并继续锁定 `DIFY_MODEL_ID`。
- 更新 `FrontEnd/README.md`，补充构建者导出 tar、组员导入 tar 和 Docker 启动步骤。

## Files

- `FrontEnd/build-openwebui-docker.ps1`
- `FrontEnd/start-openwebui-docker.ps1`
- `FrontEnd/docker-compose.local-image.yml`
- `FrontEnd/README.md`
- `.gitignore`

## Verification

- 已进行 PowerShell 脚本语法解析校验。
- 未运行完整 `docker build`，因为构建需要下载基础镜像和 npm/Python 依赖，耗时且依赖网络环境。

## Notes

- 收到镜像 tar 的组员只需要 Docker Desktop、项目代码和 `FrontEnd/.env`，不需要本地 Node.js、Python venv 或 `npm run build`。
