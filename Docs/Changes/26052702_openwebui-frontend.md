# Open WebUI 前端封装

Date: 2026-05-27
Code: 26052702
Type: Feature

## Summary

新增 `FrontEnd` 的 Docker 化 Open WebUI 前端封装，用于作为 Unity 开发智能适配助手的对话入口，并通过 Dify 的 OpenAI-compatible 端点接入现有 RAG 应用。

## Changes

- 新增 `docker-compose.yml`，默认使用 `ghcr.io/open-webui/open-webui:v0.9.5`，支持通过 `OPEN_WEBUI_IMAGE` 切换镜像，绑定本机 `3000` 端口并持久化 Open WebUI 数据。
- 新增 `.env.example`，提供 Dify OpenAI-compatible URL、API Key、模型 ID、WebUI 名称和密钥配置模板。
- 新增 `README.md`，说明本地配置、启动、镜像拉取失败处理、Dify 连接、Model IDs Filter 和验收测试步骤。
- 更新 `.gitignore`，忽略 `FrontEnd/.env` 等本地密钥文件。

## Files

- `FrontEnd/docker-compose.yml`
- `FrontEnd/.env.example`
- `FrontEnd/README.md`
- `.gitignore`
- `Docs/Changes/26052702_openwebui-frontend.md`

## Verification

- 已运行 `docker compose --env-file .env.example config` 验证 Compose 配置可展开。
- 已运行 `git diff --check` 检查补丁空白格式。
- 未运行 `docker compose --env-file .env up -d`，因为当前仓库未提供真实 `FrontEnd/.env`，避免使用模板 Dify 端点写入 Open WebUI 持久化配置。
- 待在 Open WebUI 中配置真实 Dify 端点并执行 F1 到 F5 问答验收用例。
- 用户本地尝试拉取 `ghcr.io/open-webui/open-webui:v0.9.5` 时遇到 `short read` / `unexpected EOF`，已补充重试与 slim 镜像替代说明。

## Notes

- Dify OpenAI-compatible 插件不支持 `/models` 时，需要在 Open WebUI 的 `Model IDs (Filter)` 中手动加入 `DIFY_MODEL_ID`。
- 真实 `FrontEnd/.env` 不进入版本控制，需要在本地或部署环境单独维护。
