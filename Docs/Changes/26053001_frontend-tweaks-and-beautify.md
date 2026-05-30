# 前端微调与美化

Date: 2026-05-30
Code: 26053001
Type: Feature

## Summary

修改前端和后端相关配置，清除工作空间与模型编辑的入口，删除 WEBUI_NAME 变量末尾的 " (Open WebUI)" 后缀，并追加精细的 CSS 规则，使前端界面更加简洁、美观和高端。

## Changes

- **移除标题后缀**：修改后端的 `env.py` 文件，移除当 `WEBUI_NAME` 不为默认值时追加 ` (Open WebUI)` 字符串的条件判断逻辑，使其直接显示原始设定的名称。
- **清除工作空间入口**：在前端 `UserMenu.svelte` 模块中将指向 `/workspace` 路径的判断条件设置为 `false &&`，且在 `Sidebar.svelte` 的 `isMenuItemVisible` 函数中将 `workspace` 的返回值锁死为 `false`，实现多重隐藏。
- **清除模型列表折叠栏**：在 `Sidebar.svelte` 中将 `Models` 折叠文件夹块的渲染条件设置为 `false &&`，彻底从左侧边栏隐藏 Pinned Models 入口。
- **清除模型编辑入口**：在前端 `ModelItemMenu.svelte` 模块中将“编辑”与“删除”按钮的渲染条件设置为 `false &&`，隐藏从模型选择下拉框直接进入修改模型的入口。
- **美化前端界面**：在 `app.css` 中追加输入组件焦点变换过渡效果、主色调 hover 样式、细腻的阴影和微交互动画，微调聊天输入界面的外观。

## Files

- `FrontEnd/OpenWebUI/backend/open_webui/env.py`
- `FrontEnd/OpenWebUI/src/lib/components/layout/Sidebar/UserMenu.svelte`
- `FrontEnd/OpenWebUI/src/lib/components/layout/Sidebar.svelte`
- `FrontEnd/OpenWebUI/src/lib/components/chat/ModelSelector/ModelItemMenu.svelte`
- `FrontEnd/OpenWebUI/src/app.css`

## Verification

- **项目编译校验**：在本地 Node.js (v22.13.1) 环境中成功运行了 `npm run build`。打包编译正常通过，新生成的前端静态资源文件已完整输出至后端挂载的 `build` 文件夹目录。经过多端审查，隐藏工作空间菜单、侧边栏模型列表及后缀格式皆已完全对齐设计规格。

## Notes

- 无。
