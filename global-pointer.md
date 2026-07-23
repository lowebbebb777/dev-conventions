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
```
