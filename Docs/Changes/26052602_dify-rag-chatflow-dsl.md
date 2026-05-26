# Dify RAG Chatflow DSL

Date: 2026-05-26
Code: 26052602
Type: Feature

## Summary

新增可导入 Dify 的 Unity RAG Chatflow DSL 模板，用于快速搭建项目演示所需的意图识别、知识检索和回答生成流程。

## Changes

- 新增 `advanced-chat` 类型的 Dify DSL，覆盖 API 查询、报错调试、版本迁移、代码建议、概念解释和通用兜底分支。
- 在开始节点中保留 `code_context` 与 `unity_version` 可选输入，默认说明当前官方文档知识库主要基于 Unity 6.4。
- 知识检索节点暂未写死知识库 ID，便于导入后在 Dify UI 中绑定实际知识库。

## Files

- `Docs/Plan/dify_unity_rag_chatflow.yml`（临时文件，后续已移除）
- `Workflows/1.0.0workflow.yml`（正式替代版本）

## Verification

- 已使用 Python `yaml.safe_load` 检查 YAML 可解析，确认 `kind=app`、`version=0.5.0`、`mode=advanced-chat`，并包含 20 个节点与 19 条边。

## Notes

- 该临时 DSL 后续已由 `Workflows/1.0.0workflow.yml` 取代；正式工作流产物统一放入 `Workflows` 目录。
