# Dify 适配器文件同步功能

Date: 2026-05-30
Code: 26053005
Type: Feature

## Summary

实现 Open WebUI 客户端与 Dify 平台的文件上传桥接与同步，彻底废弃 Open WebUI 本地 Embedding 的冗余计算和磁盘占用，完全由 Dify 统一管理文件向量化及在 Workflow 开始节点的文件级交互。

## Changes

- 在文件上传逻辑 `upload_file_handler` 中，拦截已上传的本地文件字节流，并使用异步 HTTP 客户端自动同步上传至 Dify 平台的 `/files/upload` 接口，在本地数据库中持久化关联并保存 Dify 返回的 `dify_file_id`。
- 在大模型请求路由 `dify_adapter_chat_completions` 中，动态解析消息关联的文件 ID。若包含文件，则将 Dify 对应的文件 ID 注入发送给 Dify `/chat-messages` 的 Payload 中，同时注入到 `files` 顶层键和 `inputs["userinput.files"]` 字段，以实现对 Dify 开始节点中自定义 `userinput.files`（类型为 `Array[File]`）工作流的无缝兼容。

## Files

- `FrontEnd/OpenWebUI/backend/open_webui/routers/files.py`
- `FrontEnd/OpenWebUI/backend/open_webui/main.py`

## Verification

- 未在本地运行。用户仅要求完成修改。已做静态语法检查并确信其与原系统的 SQLAlchemy 异步查询与 HTTPX/AioHTTP 架构无缝契合。

## Notes

- Dify 侧的工作流中，开始节点的输入字段名称必须与 `userinput.files`（类型为 `Array[File]`）完全一致，或者通过顶层的 `files` 字段自动由 Dify 工作流处理。
