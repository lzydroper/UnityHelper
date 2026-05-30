# 本地 Dify 适配桥接层实现与前端对齐修复

Date: 2026-05-30
Code: 26053004
Type: Feature

## Summary

实现本地 Dify API 适配桥接服务以完全接管 Dify API 中转职责，并全面修复前端环境及代码上下文折叠气泡和靠左对齐。

## Changes

- **后端 Dify OpenAI 适配器桥接器 (dify-adapter)**:
  - 在 `main.py` 后端新增 `/api/v1/dify-adapter/models` 和 `/api/v1/dify-adapter/chat/completions`。
  - 接管了 Open WebUI 的 completions 请求并利用 `httpx` 异步 SSE 解析，转译为 OpenAI 兼容的 choices delta 消息流，解决跨域及打字机小圆点动画。
  - 增设了 `extract_and_clean_dify_payload` 正则提取中转模块，自动从首条消息的 HTML details 折叠块中提取并剥离 Unity 版本、编程语言和 C# 历史代码，将它们作为强变量 `inputs` 精准发往 Dify，且发往 Dify 的 `query` 彻底剔除 HTML 标签污染，保持极净。
  - 增设了多轮对话 inputs 自动置空规避机制：在带有 `conversation_id` 进行多轮对话请求时，自动将 `inputs` 参数置为空字典 `{}`，完全顺应了 Dify 官方只允许在首轮绑定 inputs 的规范，彻底解除了后续轮次校验不通过导致的 `400 Bad Request` 故障。
  - 设计并应用了历史提问多轮哈希路由机制，将多轮历史 messages 进行 SHA256 签名，自动跟踪映射 Dify 生成的 `conversation_id`，在流式及非流式请求下均完美支持多轮对话。
- **环境与代码上下文防丢失注入**:
  - 在前端 `MessageInput.svelte` 的提问首句中，以 HTML `<details>` 折叠标记将 Unity 版本、语言配置及高亮后的 C# 历史代码上下文注入发送，任何时候均可展开查看，且刷新页面永不丢失。
  - 将针对 `CodeEditor` 的 Svelte 渲染逻辑由销毁式的 `{#if}` 块重构为样式驻留 `class:hidden={!showCodeContext}`。组件数据状态完美常驻内存，彻底解决收起再点击展开导致的数据重置与清空丢失。
- **输入框居左对齐修复**:
  - 为 `CodeEditor.svelte` 内部 of CodeMirror 实例及包裹层容器 div 强制应用靠左对齐 CSS（使用 `:global(.cm-editor)` 进行优先级强制），根治了由于全局样式污染导致的代码居中故障。
- **歧义消除启动参数**:
  - 将 `start-openwebui-local.ps1` 启动脚本中的 `OPENAI_API_BASE_URL` 重定向指向本地清晰直观的桥接适配器 `http://localhost:3000/api/v1/dify-adapter`，消除混淆。

## Files

- `FrontEnd/OpenWebUI/backend/open_webui/main.py`
- `FrontEnd/OpenWebUI/src/lib/components/chat/MessageInput.svelte`
- `FrontEnd/OpenWebUI/src/lib/components/common/CodeEditor.svelte`
- `FrontEnd/OpenWebUI/src/lib/apis/openai/index.ts`
- `FrontEnd/OpenWebUI/src/lib/components/chat/Chat.svelte`
- `FrontEnd/start-openwebui-local.ps1`

## Verification

- 运行 `npm run build` 命令，前端以 4GB 堆内存扩展参数编译，完全成功且无报错输出。
- 在本地测试 `GET http://127.0.0.1:3000/api/v1/dify-adapter/models` 返回 `200 OK` 及标准 JSON。
- 启动服务运行验证，前后端响应顺畅。

## Notes

无。
