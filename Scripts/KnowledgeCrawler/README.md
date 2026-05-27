# KnowledgeCrawler

This folder contains the repeatable data pipeline for the Unity assistant knowledge base.

## 1. Install dependencies

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r Scripts\KnowledgeCrawler\requirements.txt
```

## 2. Copy and edit config

```powershell
Copy-Item config.example.json config.local.json
```

Set `GITHUB_TOKEN` before collecting GitHub Issues to avoid low anonymous rate limits:

```powershell
$env:GITHUB_TOKEN="your_token_here"
```

## 3. Crawl Unity official docs

```powershell
python crawl_unity_docs.py --config config.local.json
```

For later top-ups, use incremental mode. This skips URLs already present in
`unity_docs.jsonl`, appends new rows, and writes a separate batch file such as
`unity_docs_incremental_260527.jsonl`.

```powershell
python crawl_unity_docs.py --config config.local.json --incremental --max-new-pages 200
python clean_existing_unity_docs.py --config config.local.json
python prepare_dify_dataset.py --config config.local.json --dataset unity_docs
```

The incremental Dify bundle is named like
`unity_official_docs_incremental_260527_001.md`, so it does not overwrite
`unity_official_docs_bundle_001.md` that may already have been uploaded to Dify.

Output:

- `Data/KnowledgeBase/raw/unity_docs/unity_docs.jsonl`
- `Data/KnowledgeBase/raw/unity_docs/html/*.html`

## 4. Crawl xLua/toLua docs

```powershell
python crawl_lua_docs.py --config config.local.json
python prepare_dify_dataset.py --config config.local.json --dataset lua_docs
```

Output:

- `Data/KnowledgeBase/raw/lua_docs/lua_docs.jsonl`
- `Data/KnowledgeBase/raw/lua_docs/html/*.html`
- `Data/KnowledgeBase/processed_clean/dify_bundle/unity_lua_hot_update_bundle_001.md`

## 5. Collect community and GitHub issues

```powershell
python collect_issues.py --config config.local.json
```

Output:

- `Data/KnowledgeBase/raw/issues/issues.jsonl`

The GitHub collector filters out low-relevance results, fetches issue comments, and stores selected solution-like comments under `Selected solution comments`. StackOverflow collection stores accepted or high-voted answers under `Selected answers`.

Create a simple category report:

```powershell
python issue_category_report.py --input ..\..\Data\KnowledgeBase\raw\issues\issues.jsonl --output-dir ..\..\Data\KnowledgeBase\reports
```

Output:

- `Data/KnowledgeBase/reports/issue_category_summary.json`
- `Data/KnowledgeBase/reports/issue_category_details.csv`

## 6. Prepare Dify import files

If `unity_docs_clean.jsonl` exists, this command writes cleaned outputs to `Data/KnowledgeBase/processed_clean`.
Otherwise it writes to `Data/KnowledgeBase/processed`.

```powershell
python prepare_dify_dataset.py --config config.local.json
```

The default prepares all known sources for backward compatibility. To prepare
only one Dify knowledge-base direction, pass `--dataset`:

```powershell
python prepare_dify_dataset.py --config config.local.json --dataset unity_docs
python prepare_dify_dataset.py --config config.local.json --dataset issues
python prepare_dify_dataset.py --config config.local.json --dataset lua_docs
```

Output:

- `Data/KnowledgeBase/processed_clean/dify_import/*.md`
- `Data/KnowledgeBase/processed_clean/dify_bundle/*.md`
- `Data/KnowledgeBase/processed_clean/manifest.jsonl`

For Dify Cloud free upload limits, use the files in `dify_bundle` first:

- `unity_official_docs_bundle_001.md` for the official documentation dataset.
- `unity_official_docs_incremental_*.md` for later Unity official documentation top-ups.
- `unity_issues_cases_bundle_001.md` for the Issues/cases dataset.
- `unity_lua_hot_update_bundle_001.md` for the xLua/toLua hot-update dataset.

The many small files in `dify_import` are kept for local inspection and traceability. Do not upload them one by one unless your Dify plan supports batch import.

## Optional: re-clean existing Unity HTML

When the raw Unity JSONL contains feedback forms, footers, or low-value one-line API pages, re-clean from the saved HTML without crawling again:

```powershell
python clean_existing_unity_docs.py --config config.local.json
python prepare_dify_dataset.py --config config.local.json
```
