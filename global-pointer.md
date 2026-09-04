# グローバルポインタ(各ツールの全セッション設定に貼る文面)/ Global Pointer Text

各AIツールのグローバル設定に貼るのは以下の文面のみ。規約本体を貼らない。
Paste only the text below into each AI tool's global settings. Never paste the convention body.

配置先 / Where to paste:
- Claude Code: `~/.claude/CLAUDE.md`
- Codex: `~/.codex/AGENTS.md`
- Antigravity / Cursor: 各アプリ設定画面の Global Rules / User Rules(UIから登録)

---

```markdown
# マルチエージェント引き継ぎ規約(全プロジェクト共通)/ Multi-Agent Handoff Convention

- 原本 / Source: `C:\Users\soich\dev-conventions\`(GitHub: lowebbebb777/dev-conventions)
- リポジトリに `AGENTS.md` / `docs/STATE.md` がある場合: それが正。作業開始時は
  `docs/STATE.md` を最初に読み、終了時はリポジトリの `AGENTS.md` の「終了時の義務」に必ず従う。
  If the repo has `AGENTS.md` / `docs/STATE.md`, they are canonical: read `docs/STATE.md`
  first, and always follow the repo AGENTS.md "End-of-Session Duties" before finishing.
- 無いリポジトリで開発を始める場合: dev-conventions のテンプレートからの導入を
  ユーザーに提案する(勝手に導入しない)。
  In repos without them, propose adopting the templates from dev-conventions; do not
  adopt silently.
- 規約本体をこのファイルに複製しない(二重管理禁止。正は各repo内と dev-conventions)。
  Do not duplicate the convention body here; canon lives in each repo and dev-conventions.

## ショートカット(合言葉・全AI共通)/ Shortcuts
- **ds = 引継ぎする**: 今いる repo の `docs/STATE.md`(無ければ `AGENTS.md`)を読み、
  「残作業」の最上位から着手する。区切りではその repo の `AGENTS.md`「終了時の義務」に従う。
- **dm = 引継ぎ保存**: 途中経過を `docs/STATE.md`(現在地・次の一手)と `docs/LOG.md` に書いて commit。
- **di = 引継ぎ登録**: このrepoを規約に登録 — テンプレから `AGENTS.md`/`docs/STATE.md`/
  `docs/LOG.md`/`docs/IDEAS.md`/`tests/test_conventions.py` を作成 + `projects.md` に1行追加 + commit。
  既にあるファイルは上書きしない。
- **did = アイディアを棚に落とす**: 直前に出た案を、今いる repo の `docs/IDEAS.md` へ
  **詩**(散文でない1〜2文)で追記する。仕様も手順も書かない。STATE には置かない。
  横断的な着想を `lowebbebb777/Ideas` へ集約したい場合は、その旨を明示して指示すること。
```
