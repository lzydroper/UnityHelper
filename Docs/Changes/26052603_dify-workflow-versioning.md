# Dify 工作流版本化产出

Date: 2026-05-26
Code: 26052603
Type: Feature

## Summary

根据项目建议书重新规划 Dify RAG 工作流，并将可导入 DSL 按版本命名规则迁移到 `Workflows` 目录。

## Changes

- 新增 `Workflows/1.0.0workflow.yml`，作为首个多功能整合版本工作流。
- 工作流接入 `gemini-3.5-flash`、`gemini-embedding-001` 与 `qwen3-rerank` 配置。
- 复用现有导出文件中的 `Unity_Official_Docs` 与 `Unity_Issues_Cases` 知识库 ID。
- 新增二级错误类型识别与 Lua/热更新兜底分支，贴合项目建议书中的错误诊断、上下文代码感知与热更新痛点。
- 更新 `Docs/Plan/4.RAG工作流与调优计划.md`，记录版本命名、路由策略、模型配置和验收指标。
- 移除旧的 `Docs/Plan/dify_unity_rag_chatflow.yml`，避免工作流产物散落在计划目录中。

## Files

- `Workflows/1.0.0workflow.yml`
- `Docs/Plan/4.RAG工作流与调优计划.md`

## Verification

- 已使用 Python `yaml.safe_load` 检查 `Workflows/1.0.0workflow.yml` 可解析。
- 已校验工作流包含 24 个节点、31 条边，且无断开的边引用。
- 已确认模型名为 `gemini-3.5-flash`，知识库 ID 为现有导出文件中的两个 ID。

## Notes

- 当前导出文件未发现独立 `Unity_Error_Cases` 或 xLua/toLua 知识库 ID，因此 `1.0.0` 版本使用 `Unity_Issues_Cases` 与 `Unity_Official_Docs` 作为报错和热更新分支的临时知识来源。
