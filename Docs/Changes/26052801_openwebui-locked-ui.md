# Open WebUI 锁定式前端

Date: 2026-05-28
Code: 26052801
Type: Feature

## Summary

将本地 `OpenWebUI` 定制为项目专用入口：隐藏不需要的产品入口，固定使用 `.env` 中的 Dify OpenAI-compatible 连接，并把模型锁定为 `unity-rag-assistant`。

## Changes

- 清除前端中的 `Playground`、`Automations`、`Calendar`、外部帮助文档、发行版、更新和授权升级提示入口。
- 用户设置和管理员设置中不再开放外部连接与集成配置入口。
- 模型选择器改为只展示固定模型，不允许添加、移除或切换模型。
- 后端模型发现和聊天请求都会强制使用 `OPENWEBUI_LOCKED_MODEL_ID`/`DIFY_MODEL_ID`，默认值为 `unity-rag-assistant`。
- 启动脚本改为设置锁定模型、关闭外部连接相关功能，并通过 `PYTHONPATH` 加载 Windows 启动兼容补丁。

## Files

- `FrontEnd/OpenWebUI/src/lib/components/chat/ModelSelector.svelte`
- `FrontEnd/OpenWebUI/src/lib/components/chat/Navbar.svelte`
- `FrontEnd/OpenWebUI/src/lib/components/chat/SettingsModal.svelte`
- `FrontEnd/OpenWebUI/src/lib/components/layout/Sidebar.svelte`
- `FrontEnd/OpenWebUI/src/lib/components/layout/Sidebar/UserMenu.svelte`
- `FrontEnd/OpenWebUI/src/lib/components/layout/UpdateInfoToast.svelte`
- `FrontEnd/OpenWebUI/src/lib/components/admin/Settings.svelte`
- `FrontEnd/OpenWebUI/src/lib/components/admin/Settings/General.svelte`
- `FrontEnd/OpenWebUI/src/lib/components/admin/Users/UserList.svelte`
- `FrontEnd/OpenWebUI/src/routes/(app)/playground/+layout.ts`
- `FrontEnd/OpenWebUI/src/routes/(app)/automations/+layout.ts`
- `FrontEnd/OpenWebUI/src/routes/(app)/calendar/+page.ts`
- `FrontEnd/OpenWebUI/backend/open_webui/main.py`
- `FrontEnd/OpenWebUI/backend/open_webui/routers/openai.py`
- `FrontEnd/OpenWebUI/backend/sitecustomize.py`
- `FrontEnd/start-openwebui-local.ps1`
- `FrontEnd/README.md`

## Verification

- 运行 `python -m py_compile` 验证后端改动语法。
- 运行 `npm run build`，前端构建成功。
- 运行 `.\start-openwebui-local.ps1`，确认 `127.0.0.1:3000` 正常监听并返回 HTTP 200。
- 请求 `http://127.0.0.1:3000/api/config` 返回 HTTP 200，版本更新检查为关闭状态。

## Notes

当前 `/api/models` 需要登录态才能查询；锁定模型逻辑已在后端模型发现和聊天请求路径中实现。聊天功能仍需使用实际管理员/用户账号登录后结合 Dify Key 做端到端问答验收。
