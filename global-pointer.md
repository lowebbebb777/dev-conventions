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

- 原本 / Source: `C:\Users\soich\dev-conventions`(GitHub: lowebbebb777/dev-conventions)
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

- 新しい開発を始める前に、dev-conventions `docs/DEVELOPMENT_PHILOSOPHY.md` §14 に従い、ユーザー価値・重複・捨てる仕事・リリースへの影響を確認する。優先目標を阻む場合はユーザーに忠告し、決定権を奪わない。

- 商品開発のDR（デザインレビュー）は `dev-conventions/docs/DEVELOPMENT_PHILOSOPHY.md` §16 が正本。DR123等の統合審査・差戻し・軽量DRを許容し、初回出荷審査は別途承認とする。詳細は正本を読む（ここに複製しない）。

- **AIとGit名義**: AI名義のGit Author / Committer / Co-Authored-Byを使用しない。AIの作業と人間の承認はLOGへ分離記録。既存履歴は変更しない。正本: `dev-conventions/docs/COMMIT_ATTRIBUTION.md`。

## ショートカット(合言葉・全AI共通)/ Shortcuts
- **ds = 引継ぎする**: 今いる repo の `docs/STATE.md`(無ければ `AGENTS.md`)を読み、
  「残作業」の最上位から着手する。区切りではその repo の `AGENTS.md`「終了時の義務」に従う。
- **dm = 引継ぎ保存**: 途中経過を `docs/STATE.md`(現在地・次の一手)と `docs/LOG.md` に書いて commit。
- **di = 引継ぎ登録**: このrepoを規約に登録 — テンプレから `AGENTS.md`/`docs/STATE.md`/
  `docs/LOG.md`/`docs/IDEAS.md`/`tests/test_conventions.py` を作成 + `projects.md` に1行追加 + commit。
  既にあるファイルは上書きしない。
- **did = アイディアを棚に落とす**: 直前に出た案を、今いる repo の `docs/IDEAS.md` へ
  **発言者を明記した逐語原文＋別記の詩文（1〜2文）＋具体タグ2語以上**で保存する。原文を意訳しない。
  仕様も手順も書かない。STATE には置かない。横断的な着想を `lowebbebb777/Ideas` へ
  集約したい場合は、その旨を明示して指示すること。
```
