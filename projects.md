# プロジェクト索引 / Project Index

AIが「どのプロジェクトを引き継ぐか」を選ぶための一覧。
各プロジェクトの**正はそのrepo**(`AGENTS.md` → `docs/STATE.md`)。ここは所在ポインタだけ。
旧 USB `AI_KEY/10_PROJECTS/` の後継で、**この索引の正本は git**(USBは不要)。

共通の起動プロンプト:
> 「AGENTS.md を読んで、docs/STATE.md の残作業(優先順)から着手して」

| プロジェクト | ローカルパス | remote | 正典ドキュメント |
|---|---|---|---|
| sleepsm(SmartSleepManager / Sleep v3) | `C:\Users\soich\AndroidStudioProjects\sleepsm` | github.com/lowebbebb777/sleepsm | `AGENTS.md` → `docs/STATE.md` → `docs/DESIGN_V3_1.md` |
| SleepSoundSampler(Sleep-Audio-AI) | `C:\Users\soich\PycharmProjects\Sleep-Audio-AI` | github.com/lowebbebb777/Sleep-Audio-AI | `AGENTS.md` → `docs/STATE.md` → `docs/ma_engine_design.md` |
| SleepSoundOne(Android自然音・Ma音響アプリ) | `C:\Users\soich\AndroidStudioProjects\SleepSoundOne` | github.com/lowebbebb777/SleepSoundOne | `AGENTS.md` → `docs/STATE.md` → `docs/PORTING.md` |
| Runova(WebAI駆動エージェンティックCLI/GUI) | `C:\Users\soich\PycharmProjects\Runova` | github.com/lowebbebb777/Runova | `AGENTS.md` → `docs/STATE.md` → `docs/EX_STREAM_DESIGN.md` |
| Facefusionkai(特定人物適応型顔変換アダプタ) | `C:\AI\Facefusionkai` | github.com/lowebbebb777/Facefusionkai | `AGENTS.md` → `docs/STATE.md` → `release_gates.toml` |
| RanovaCLI(RUNOVA CLI/GUI/Orchestra) | `C:\Users\soich\PycharmProjects\RanovaCLI` | github.com/lowebbebb777/RunovaCLI | `AGENTS.md` → `docs/STATE.md` → `docs/EX_STREAM_DESIGN.md` |
| LLLM(小型ローカルLLM研究・DeltaFEM) | `C:\Users\soich\PycharmProjects\LLLM` | github.com/lowebbebb777/LLLM | `README.md` → `docs/STATE.md` → `deltafem/RESEARCH_PLAN.md` |
| gbmc(GBMesh Code・ローカルLLMコーディングエージェント) | `C:\Users\soich\PycharmProjects\gbmesh-code` | github.com/lowebbebb777/gbmesh-code | `AGENTS.md` → `docs/STATE.md` → `docs/UX_RELIABILITY/README.md` |

| RevoAim（統計的問題解決支援） | `(clone先未固定)` | github.com/lowebbebb777/RevoAim | `AGENTS.md` → `docs/STATE.md` → `docs/UPSTREAM_DESIGN.md` |
| Ideas(RUNOVA Labs横断アイデア保管庫) | `(clone先未固定)` | github.com/lowebbebb777/Ideas | `README.md` → `docs/STATE.md` → `ideas/<slug>/IDEA.md` |

<!-- 新規プロジェクトは1行追加するだけ。詳細は各repoのSTATE/LOGが持つ。
     remote URLがあれば埋める(他マシン・クラウドAIからcloneできるように)。
     ローカルに存在しないパスは行ごと削除する(tests/test_conventions.py が落とす)。
     2026-08-02: CloudCodeEX はローカル実体が消滅していたため削除。設計文書は
     Runova 側の docs/ に同名で存在する。 -->
