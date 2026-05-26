# 知识库采集与清洗能力增强

Date: 2026-05-26
Code: 26052601
Type: Feature

## Summary

增强 `KnowledgeCrawler` 的 Unity 官方文档与 GitHub/社区 Issues 数据采集质量，减少噪声内容进入 Dify 知识库，并支持免费版 Dify 的单文件上传限制。

## Changes

- 新增 Unity 文档清洗流程，过滤反馈表单、页脚版权、Cookie/隐私链接和低价值短页面。
- 新增基于 Unity `docdata/toc.js` 的深层页面预发现能力，提升 Manual 深层页面覆盖。
- 新增图片引用保留策略，将正文图片转换为 Markdown 图片 URL 与说明文本。
- 新增 Dify bundle 输出，将同类知识库内容合并为单个 Markdown 文件。
- 优化 GitHub Issues 采集，加入 Unity 相关性评分、精选解决评论抓取与 StackOverflow 高票/采纳答案抓取。
- 扩展质量报告，增加 clean pages、rejected pages、bundle 文件大小与 issue 评论质量统计。

## Files

- `Scripts/KnowledgeCrawler/crawl_unity_docs.py`
- `Scripts/KnowledgeCrawler/unity_doc_cleaner.py`
- `Scripts/KnowledgeCrawler/clean_existing_unity_docs.py`
- `Scripts/KnowledgeCrawler/collect_issues.py`
- `Scripts/KnowledgeCrawler/prepare_dify_dataset.py`
- `Scripts/KnowledgeCrawler/quality_report.py`
- `Scripts/KnowledgeCrawler/config.local.json`
- `Scripts/KnowledgeCrawler/config.example.json`
- `Scripts/KnowledgeCrawler/README.md`
- `Docs/Plan/2.GitHub与社区Issues采集计划.md`
- `Docs/Plan/3.数据清洗分块与Dify导入计划.md`

## Verification

- 已运行 `python -m py_compile` 检查相关 Python 脚本语法。
- 已运行 `python -m json.tool Scripts\KnowledgeCrawler\config.local.json` 校验配置文件。
- 已运行 `python Scripts\KnowledgeCrawler\clean_existing_unity_docs.py --config Scripts\KnowledgeCrawler\config.local.json` 生成 clean/rejected Unity 文档。
- 已运行 `python Scripts\KnowledgeCrawler\prepare_dify_dataset.py --config Scripts\KnowledgeCrawler\config.local.json` 生成 `processed_clean` Dify 导入文件。
- 已运行 `python Scripts\KnowledgeCrawler\quality_report.py --root Data\KnowledgeBase` 查看数量与 bundle 大小。

## Notes

- GitHub Issue 精选评论功能需要重新运行 `collect_issues.py` 才会更新现有 `issues.jsonl`。
- 已移除 README 中误写入的真实 GitHub token；该 token 建议在 GitHub 后台撤销后重新生成。
