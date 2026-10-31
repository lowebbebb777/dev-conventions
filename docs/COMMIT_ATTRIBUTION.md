# Gitコミット名義とAI作業実績の分離

2026-10-31制定。**今後の新規コミットのみ対象、過去履歴は何もしない。**

## 規則

1. Git Author / Committer は、それぞれ実際に責任を持って提出・作成した人間、または実際に実行した正規の自動化botの正しい名義を使う。本人の許可のない氏名・メールの推測や偽装は禁止する。AI製品・AIモデル・AI人格（Claude、Codex、ChatGPT、Antigravity、Geminiなど）をGit Author / Committerに設定しない。
2. **AIを Co-Authored-By に自動登録しない。** 実際に共同作業した人間のCo-Authored-Byは許可する。AIが実装・設計・レビューに参加した事実は隠さず、docs/LOG.md（必要に応じPR・設計書）に使用AI、役割、作業、指示した人、検証、承認、関連コミットを記録する。
3. コミット前に実際のAuthorとCommitterの有効値とメッセージを確認する。未設定・不明・AI名義は中止。ユーザーのGitHubに関連付いた本人用メール／no-replyを使い、勝手な名義への置き換えはしない。実際のGitHubアプリ等がbot名義で記録される場合は、その事実を記録する。
4. **過去のコミット、共同作成者表記、Contributorsは変更しない。** 既存履歴のrebase、amend、filter-repo、force push等による修正は禁止。既存履歴を新ルールで検査して全面的にFAILさせない。
5. 権利帰属や第三者OSSライセンスの確認は別の作業。GitHubのAuthor / Co-Author表示だけで著作権者・権利者が確定するわけではない。

## 手順（対象リポジトリで）

```powershell
git config --show-origin --get user.name
git config --show-origin --get user.email
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
# 未設定なら、本人が承認した値のみを当該リポジトリに設定：
# git config --local user.name "本人が承認した名前"
# git config --local user.email "本人が確認したGitHub用メール"
git config --local user.useConfigOnly true
python tools/check_commit_attribution.py --current
# ローカルhook（既存のhookに衝突しない場合だけ）
python tools/install_commit_hooks.py
```

- ガードの実行モード: `--current` は現在の有効名義、`--message PATH` はコミット本文、`--range BASE..HEAD` は**新規コミット範囲だけ**検査。過去履歴の修正はしない。
- `GIT_AUTHOR_NAME` / `GIT_COMMITTER_NAME` の環境変数や `git -c` 、`--author` で名義が上書きされることがあるため、設定ファイルではなく有効値を見る。
- Claude Code側の署名自動挿入は、バージョンに対応する公式設定で無効化する。ただしそれだけではAuthor/Committer設定は直らない。
- ガードの他repoへのコピー、ローカルhookの導入は対象repoの承認と検証が必要。`core.hooksPath` や既存hookがある場合は上書きしない。WindowsのGit設定やGitHub Web/API経由のコミットには**本repoへの規約追加だけでは強制されない**。
- 本人の明示承認なしに `git config --global` を書き換えない。ガードが使えない環境でも人間のレビューで新規コミットを確認する。
