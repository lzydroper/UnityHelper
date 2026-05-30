# Dify 直连跨域、着色编辑与顶部常驻卡片修复

Date: 2026-05-30
Code: 26053003
Type: Feature

## Summary

修复并优化了 Dify 前端直连功能：使用 CodeMirror 编辑器代替 textarea 实现 C# 代码识别与颜色高亮；使输入区高度可手动拉伸；在对话顶部常驻本次对话环境配置及可折叠代码卡片；在后端建立轻量级代理路由，彻底打通 CORS 跨域瓶颈，实现 SSE 数据 100% 流式互通。

## Changes

- **CodeMirror 语法着色编辑器集成**：在 `MessageInput.svelte` 中以 `CodeEditor.svelte` 替换了原生的 `textarea`，显式指定 `lang="csharp"`，实现 C# 代码的高清语法着色与行号行距辅助。
- **高度垂直拉伸控制**：在 `MessageInput.svelte` 中，使代码输入容器具有 `overflow-auto` 和 `resize-y` 特性，最小高度设为 `300px` 且支持用户手动垂直拖拽拉伸。
- **对话环境上下文常驻面板**：在 `Chat.svelte` 顶部（`<Messages>` 上方）新增了一块常驻卡片。通过翡翠绿和深蓝标签标记本次会话锁定的“Unity 版本”和“编程语言”，并提供一键展开/折叠长代码块的折叠式显示面板，方便在对话中后期随时检索检查开发环境配置。
- **高安全性、无 CORS 限制的后端反向代理**：在后端 `main.py` 中建立轻量级的 `/api/dify/chat-messages` 服务端路由，前端凭 JWT Token 认证（`Bearer ${token}`）发送请求，由后端安全注入 Dify 密钥并发起 SSE 转发，彻底解决浏览器跨域（CORS）连通失败导致的 `net error` 问题。

## Files

- `FrontEnd/OpenWebUI/src/lib/components/chat/MessageInput.svelte`
- `FrontEnd/OpenWebUI/src/lib/components/chat/Chat.svelte`
- `FrontEnd/OpenWebUI/src/lib/apis/openai/index.ts`
- `FrontEnd/OpenWebUI/backend/open_webui/main.py`

## Verification

- **前端打包编译**：本地通过 `npx vite build` 重新编译打包全部成功，静态站点输出至后端 `build` 文件夹。

## Notes

- 重新部署后，用户只需在 `FrontEnd/.env` 中将 `DIFY_OPENAI_BASE_URL` 设置为 Dify 服务的原生端点（例如 Dify 官方云的 `https://api.dify.ai/v1`），并将 `DIFY_OPENAI_API_KEY` 设置为原生 Chat App 的 API 密钥（通常以 `app-` 开头），启动即可生效。
