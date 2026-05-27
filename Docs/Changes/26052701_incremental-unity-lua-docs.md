# Unity 与 Lua 文档增量采集

Date: 2026-05-27
Code: 26052701
Type: Feature

## Summary

增强 `KnowledgeCrawler` 的文档采集与 Dify 准备流程，支持 Unity 官方文档增量补采、xLua/toLua 专项文档采集，以及按知识库方向单独生成 Dify 导入文件。

## Changes

- `crawl_unity_docs.py` 新增 `--incremental`、`--max-new-pages`、`--refresh-existing`，增量记录会带 `crawl_batch` 并生成独立 `unity_docs_incremental_*.jsonl`。
- 新增 `crawl_lua_docs.py`，采集 xLua 与 toLua 文档，过滤 GitHub Issues、tags、search、edit/history 等低价值导航页。
- `prepare_dify_dataset.py` 新增 `--dataset unity_docs|issues|lua_docs|all`，默认保持全量兼容；Unity 增量会生成 `unity_official_docs_incremental_*.md`，不覆盖 `unity_official_docs_bundle_001.md`。
- `quality_report.py` 增加 Lua 文档、Unity 增量批次、section 统计，并按 `chunk_id` 去重统计多份 manifest。
- 已生成 `unity_lua_hot_update_bundle_001.md` 与 `unity_official_docs_incremental_260527_001.md`，用于后续分别上传到 Lua/热更新知识库和 Unity 官方文档知识库。

## Files

- `Scripts/KnowledgeCrawler/crawl_unity_docs.py`
- `Scripts/KnowledgeCrawler/crawl_lua_docs.py`
- `Scripts/KnowledgeCrawler/clean_existing_unity_docs.py`
- `Scripts/KnowledgeCrawler/prepare_dify_dataset.py`
- `Scripts/KnowledgeCrawler/quality_report.py`
- `Scripts/KnowledgeCrawler/config.example.json`
- `Scripts/KnowledgeCrawler/config.local.json`
- `Scripts/KnowledgeCrawler/README.md`
- `Docs/Plan/1.Unity官方文档采集计划.md`
- `Docs/Plan/3.数据清洗分块与Dify导入计划.md`
- `Docs/Plan/4.RAG工作流与调优计划.md`

## Verification

- 已运行 `python -m compileall -q Scripts\KnowledgeCrawler`。
- 已运行 `python -m json.tool Scripts\KnowledgeCrawler\config.example.json` 与 `python -m json.tool Scripts\KnowledgeCrawler\config.local.json`。
- 已运行 `python Scripts\KnowledgeCrawler\crawl_unity_docs.py --config Scripts\KnowledgeCrawler\config.local.json --incremental --max-new-pages 20`，新增 20 条原始 Unity 记录。
- 已运行 `python Scripts\KnowledgeCrawler\clean_existing_unity_docs.py --config Scripts\KnowledgeCrawler\config.local.json`，新增 15 条 clean Unity 增量记录，5 条低价值记录进入 rejected。
- 已运行 `python Scripts\KnowledgeCrawler\crawl_lua_docs.py --config Scripts\KnowledgeCrawler\config.local.json`，得到 34 条 Lua 文档记录，其中 xLua 25 条、toLua 9 条。
- 已运行 `python Scripts\KnowledgeCrawler\prepare_dify_dataset.py --config Scripts\KnowledgeCrawler\config.local.json --dataset unity_docs`，生成 `unity_official_docs_incremental_260527_001.md`，并确认 `unity_official_docs_bundle_001.md` 哈希不变。
- 已运行 `python Scripts\KnowledgeCrawler\prepare_dify_dataset.py --config Scripts\KnowledgeCrawler\config.local.json --dataset lua_docs`，生成 `unity_lua_hot_update_bundle_001.md`。
- 已运行 `python Scripts\KnowledgeCrawler\prepare_dify_dataset.py --config Scripts\KnowledgeCrawler\config.local.json --dataset issues` 验证 Issues 可单独生成。
- 已运行 `python Scripts\KnowledgeCrawler\quality_report.py --root Data\KnowledgeBase`。

## Notes

- 当前只实际小批量补采 20 条 Unity 原始记录，用于验证增量链路；继续补量时可调大 `--max-new-pages`。
- `--dataset issues` 会重新生成 Issues bundle；Unity 已上传的 `unity_official_docs_bundle_001.md` 不会被 Unity 增量准备流程覆盖。
