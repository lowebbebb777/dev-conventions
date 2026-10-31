# AGENTS.md — <プロジェクト名 / Project Name> エージェント共通ルール / Common Agent Rules

全エージェント(Codex / Antigravity / Claude Code / Cursor)共通の入口 / Common entry point for all agents.
**このファイルには「今やること」を書かない**(陳腐化するため)。現在地は `docs/STATE.md` / **Never write "current tasks" here** (it goes stale). Current position lives in `docs/STATE.md`.

## 読む順番 / Reading Order

1. [共通開発思想](https://github.com/lowebbebb777/dev-conventions/blob/main/docs/DEVELOPMENT_PHILOSOPHY.md) — 役割・権限の原則。モデル名では権限が決まらない / Common role-based authority canon
   （本リポジトリの承認済み設計正典: <設計文書 / approved project design canon>）
2. `docs/STATE.md` — 現在地と残作業 / current position and remaining work
3. <設計文書 / design docs> — 仕様の正。矛盾時の優先順: <A> > <B> / spec canon; precedence on conflict
4. `docs/LOG.md` — 経緯と判断理由(必要時のみ遡る) / history and rationale (consult as needed)

## ビルド・環境 / Build & Environment

```
<build command>
<test command>
```

テストを持たないリポジトリではその旨と、代わりの検証手順を書く /
If the repo has no tests, say so and write the verification procedure used instead.

## 不変条件 / Invariants

権限の共通正本は `dev-conventions/docs/DEVELOPMENT_PHILOSOPHY.md`。
製品固有の正は <正典ファイル> / Canon: <canonical file>.

## 役割と権限の境界 / Roles & Authority (non-optional)

- **ユーザー / User**: 役割の任命・変更・取消し、要求・設計変更・最終受入の承認者。
- **設計担当AI / Design AI**: ユーザーが**明示的に**委任した範囲だけで企画・要求・設計を担当。
- **実装担当AI / Implementer AI**: 確定した要求・設計仕様の実装と検証。技術的な実装裁量は設計権限ではない。
- **独立レビュー担当 / Independent reviewer**: 契約と証拠の照合。最終承認を代行しない。
- AIモデル名・性能・製品名から権限を推定しない。**仕様変更、受入基準変更、範囲拡大、権限変更は事前承認**。
- 設計の穴・矛盾は影響、選択肢、推奨案を LOG に報告し、承認前に仕様を変えない。
- 優先順位: ユーザーの明示指示・承認済み実装契約 > 共通権限原則 > 製品固有規約の範囲内の実装裁量。
  LOG の事後報告や STATE への仮定記載は承認に代わらない。

## ユーザー価値と捨てる仕事 / Value-First Scope Pruning (§14, required)

- 新しい仕事の前に、**ユーザー価値、既存との重複、最優先リリースへの影響、捨てる・統合する仕事**を確認する / Check user benefit, duplicates, release impact, and what to stop.
- 最優先目標とぶつかる新案には**根拠を示してユーザーへ忠告**する。最終判断はユーザー。AIは独断でスコープを変更しない / Warn respectfully, user decides.
- 安全・品質・法令・権利・データ保全・必要な実機評価を安易に捨てない。正本: `docs/DEVELOPMENT_PHILOSOPHY.md` §14。

## Design Review / DR Gate (§16, required)

- 共通正本: [Design Review §16](https://github.com/lowebbebb777/dev-conventions/blob/main/docs/DEVELOPMENT_PHILOSOPHY.md)。**DR0（アイディア）/DR1（商品企画・要求）/DR2（構想）/DR3（詳細）/DR4（実装・検証）/DR5（リリース準備）/初回出荷審査（別途承認）/DR6（ライフサイクル）** をリスクに応じて適用する。
- **DR123等の統合審査**や設計への差戻し・反復を認める。ただしDR別の証拠と判定を残す / Combined reviews and agile rework are allowed, with per-stage evidence.
- 小さな変更は軽量DR／既存レビュー・テストでよい。重大リスクと受入・出荷の権限ゲートを省略しない / Scale depth to risk; never self-approve shipping.
- 任意記録テンプレート: `dev-conventions/templates/docs/DR_RECORD.template.md`。DR審査とユーザー最終承認を混同しない。

## AIとGit名義 / AI Commit Attribution (§15)

- Git Author / Committerには本人が承認した人間や正規bot名義を使用。Claude・Codex・GPT等のAI名義とAIの `Co-Authored-By` 自動追加は禁止 / Use only authorized human or real bot identities.
- Gitの有効名義を検証し、AI作業・人間の承認を `docs/LOG.md` に別記。**過去履歴は変更しない** / Check identity; keep history intact.
- 正本: [dev-conventions/docs/COMMIT_ATTRIBUTION.md](https://github.com/lowebbebb777/dev-conventions/blob/main/docs/COMMIT_ATTRIBUTION.md)。

## 終了時の義務 / End-of-Session Duties

このリポジトリは複数エージェントのリレーで開発されている。記録が次走者の命綱 / This repo is developed in relay by multiple agents. The record is the next runner's lifeline.

1. **1 Step = 1 コミット**。仕様があればメッセージに節番号、無ければ目的を1行 /
   One step = one commit; cite the spec section if there is one, otherwise one line of intent.
2. `docs/STATE.md` を**上書き更新** / Overwrite `docs/STATE.md`.
3. `docs/LOG.md` に**1エントリ追記** / Append one entry to `docs/LOG.md`.
4. 検証を実行し、結果(何をどう確かめたか)を STATE と LOG に記録 /
   Run the verification; record in STATE and LOG what you checked and how.
   **新しいテストは、修正前のコードで FAIL することを確認してから緑にする**(緑だけでは
   何も検証していないテストと区別できない)/ Confirm each new test FAILS against the pre-fix
   code before accepting green.
5. repo の事実は必ず repo 内に置く(エージェント固有メモリだけに残さない) /
   Repo facts always live in the repo; never only in agent-private memory.
6. 今やらない案は `docs/IDEAS.md` に**原文（逐語）＋詩文（1〜2文）＋具体タグ2語以上**を保存。STATEには置かない /
   Preserve attributed verbatim source, poetic rendering and searchable tags.

## 運用の指針 / Operating Guidance

以下の報告・探索方法だけが**既定値**。委任範囲内で外したら LOG に理由を書く /
Only reporting and exploration guidance is a default; note deviations in LOG.
**役割・権限・不変条件・承認ゲートはAI判断で変更できない / Authority and approvals are not defaults.**
機械で判定できることは心がけでなく `tests/` に置く / Whatever can be checked mechanically
belongs in `tests/`, not in good intentions — those checks are rules, not defaults.

1. **報告は結論ファースト / Lead with the conclusion**:
   挨拶・前置き・自己弁護は書かない。ただし**行数上限は設けない** — 判断理由・
   トレードオフ・リスク・逸脱は必要なだけ書く。「短さ」より「次走者が再現できること」 /
   No greetings or preamble, but **no line limit**: write as much rationale, trade-off,
   risk and deviation as the next runner needs to reproduce your reasoning.
2. **探索は構造から、変更は本体を読んでから / Skim structurally, read before you edit**:
   俯瞰には AST 要約や grep / ripgrep(各AIのネイティブ検索でよい)を使う。
   **変更を加えるファイルは本体を読む**。読まずに直した手戻りは、節約したトークンより高くつく /
   Use AST summaries and grep to orient, but read the full file you are about to change —
   a wrong edit costs more than the tokens it saved.
3. **状態の正は `docs/STATE.md` 一つ / One source of truth for state**:
   補助的な JSON/メモはセッション内利用に留め commit しない。食い違ったら STATE が正 /
   Keep scratch state out of the repo; on conflict, STATE wins.
4. **完了の判定 / Definition of done**:
   - 緑は**必要条件**。ただし **PASS だけでは根拠にならない** — 新しいテストは
     **修正前のコードで FAIL することを確認**してから採用する /
     Green is necessary but not sufficient: confirm each new test FAILS against the pre-fix code.
   - テストを持てない領域(ドキュメント・調査): 「どう確かめたか」を手順ごと
     STATE の「検証済みの事実」に書けば根拠になる。手順を書けないものは完了ではない /
     Where tests cannot exist, the verification steps written into STATE are the evidence;
     if you cannot write the steps, it is not done.
   - **緑になった瞬間にセッションを終える義務はない**。残作業を続けてよい /
     Green does not oblige you to stop; carry on with the remaining work.

## 自律範囲 / Autonomy — 確認なしでやってよいこと

契約内の軽微・可逆な**実装詳細**だけは仮定を STATE に記録して進める /
Only minor, reversible implementation details may proceed on documented assumptions.
要求・設計・受入基準が不明なら独断せず、必要な決定を権限者へ返す / Escalate design ambiguity.

- 読み取り全般 / ビルド・テスト・lint・型チェックの実行 / Reading, building, testing, linting
- 実装・リファクタ・テスト追加、作業ブランチの作成、ローカル commit /
  Implementing, refactoring, adding tests, branching, committing locally
- 一時ファイル(scratch)の作成、サブエージェント・並列探索の起動 /
  Scratch files, subagents, parallel exploration
- 既存契約内の軽微な実装方式の選択(仮定を STATE に記録し、設計を変えない) /
  Minor implementation choices within approved contract (not changes to design)
- **規約そのものへの改善提案**(このファイルを含む。提案は LOG に書き、適用はユーザー承認後) /
  Proposing changes to this convention itself (write the proposal in LOG; apply after approval)

事前承認が必要（列挙は限定ではない）/ Requires approval (non-exhaustive):

- 要求・設計思想・確定設計・受入基準の変更、作業範囲拡大、役割・権限変更 / Design, scope and authority changes
- `push` / PR作成 / main統合 / リリース・デプロイ、外部への送信 / Pushing, PRs, merging, releases, anything outbound
- 破壊的操作(履歴改変、force push、ファイル・データの削除)/ Destructive operations
- 依存の追加・更新、有料APIの実行 / Adding or upgrading dependencies, paid API calls
- `docs/STATE.md`「着手禁止」に載っている項目 / Anything listed under STATE's "Do Not Start"

## ショートカット(合言葉)/ Shortcuts
- **ds = 引継ぎする**: `docs/STATE.md` を読んで「残作業」の最上位から着手し、区切りでは上記
  「終了時の義務」に従う / read STATE.md and start from the top remaining task.
- **dm = 引継ぎ保存**: 途中経過を `docs/STATE.md`(次の一手)と `docs/LOG.md` に書いて commit /
  checkpoint now before switching AI mid-task.
- **di = 引継ぎ登録**: 新規repoを規約に登録(テンプレから AGENTS/STATE/LOG/IDEAS +
  `tests/test_conventions.py` を作成 + `dev-conventions/projects.md` に1行追加 + commit)/
  onboard a new repo.
- **did = アイディアを棚に落とす**: 今いるrepoの `docs/IDEAS.md` に原文（発言者・逐語）＋詩文（1〜2文）＋具体タグ2語以上を登録。原文を意訳せず、AI発言とユーザー発言を区別する。
  Keep the verbatim source and poem distinct; keep specs, tasks and progress out of IDEAS.
  横断アイデアを `lowebbebb777/Ideas` に集約するときは同repoのAGENTSに従う。
