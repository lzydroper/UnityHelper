# Dify 原生 SSE 直连流与 Unity 选项控制集成

Date: 2026-05-30
Code: 26053002
Type: Feature

## Summary

在 Open WebUI 前端聊天界面直接集成并直连 Dify 原生流式 API，摆脱了对中间后端的依赖，并为用户在开启新对话时提供了专用的 Unity 版本、代码语言与代码上下文的个性化输入控制面板。

## Changes

- **Unity 开发首句配置面板**：在 `MessageInput.svelte` 中，仅在对话的第一条消息前，以极富磨砂玻璃质感的 Svelte 动态渐显面板为用户提供“Unity 版本”、“编程语言”的选择下拉菜单（默认为 Unity 6 与 C#）和可伸缩的“代码上下文”编辑区，在发送时以 `dify_inputs` 对象附带变量发送。
- **前端原生 SSE 直连与多轮绑定**：在 `Chat.svelte` 中，若 Dify 环境变量有效，则通过自定义的 SSE 数据拦截器直接请求 Dify 真实端点。流式获取 delta chunks 并将其逐字反应渲染在 Open WebUI 的 UI 打字机中，并自动利用 localStorage 映射绑定 Dify 侧的 `conversation_id` 维持多轮追问。
- **主动式 Abort 控制**：建立 local 级 `difyAbortController`。当用户在生成中点击“Cancel”或“停止生成”时，瞬间 abort 相关的 fetch 链路，保障客户端性能和 Dify 端的 Token 消耗。
- **Dify 工作流 YML 优化及验证**：编写 `Scripts/format_dify_workflow.py` 自动化格式脚本，成功对 RAG 链路的 24 个图节点进行扫描重排，验证了 7 个核心大模型节点中对 start 节点注入的三个参数引用并重新格式化为 clean yml 输出至 `Workflows/1.2.0workflow.yml`。

## Files

- `FrontEnd/OpenWebUI/src/lib/components/chat/MessageInput.svelte`
- `FrontEnd/OpenWebUI/src/lib/components/chat/Chat.svelte`
- `Scripts/format_dify_workflow.py`
- `Workflows/1.2.0workflow.yml`

## Verification

- **前端打包编译**：本地通过 `node-v22.13.1` 运行 `npm run build`，编译打包全部成功，静态站点输出至后端 `build` 文件夹。
- **YAML 验证**：成功运行 `python Scripts/format_dify_workflow.py` 且控制台打印 24 个节点完全校验通过。

## Notes

- 重新部署后，用户只需在 `FrontEnd/.env` 中将 `DIFY_OPENAI_BASE_URL` 设置为 Dify 服务的原生端点（例如 Dify 官方云的 `https://api.dify.ai/v1`），并将 `DIFY_OPENAI_API_KEY` 设置为原生 Chat App 的 API 密钥（通常以 `app-` 开头），启动即可生效。
