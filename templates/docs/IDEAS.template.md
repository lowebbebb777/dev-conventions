# IDEAS — アイディア棚 / Idea Shelf

<!-- 追記のみ。STATE.md(現在地) にも LOG.md(履歴) にも属さない
     「たまに思い出せればいいもの」の置き場。**毎セッション読まない**。
     Append-only. Home for what belongs to neither STATE (current position) nor
     LOG (history): things worth recalling occasionally. NOT read every session. -->

## 1件 = 詩 / One Entry = A Poem

アイディアは**詩だけ**を残す。仕様も手順も書かない。
Keep only the poem. No specs, no steps.

**基準は長さではなく「散文でないこと」**。1文でも2文でもよい。
The test is not length but *not-prose*. One sentence or two, either is fine.

なぜ詩か / Why poetry:

- **復号器に合わせた符号だから**。この棚を読むのは人間と言語モデルであり、両者とも
  比喩を展開するのが得意。手続き的な符号(圧縮・QR等)は復号器が無いので死ぬが、
  詩は**実在する復号器に最適化されている**。
  Match the code to the decoder you actually have: humans and language models both
  unpack metaphor natively. Procedural encodings die for lack of a decoder; poetry does not.
- **語ひとつでは足りない**。棚を読むのは記憶を共有しない別エージェントであり、
  裸の語は復元できない(原則5・6)。1文なら**関係**が入る。
  A bare word is unrecoverable for an agent that shares no memory with you; a sentence
  carries the *relations*, not just the label.
- **説明は腐るが、像は腐らない**。手順を書くと実装とずれた瞬間に嘘になる。
  Procedures rot against the code; images do not.

### 書き方 / Rules

- **散文にしない。1〜2文**。**説明を足したくなった時点で、それはアイディアではなく作業**
  (→ `docs/STATE.md`)。これが棚と現在地の境界。詩に畳むのではなく、
  **詩が原形で、仕様書のほうが展開された劣化版**
  Never prose; one or two lines. The moment you want to *explain* it, it is a task, not an
  idea (→ STATE). The line is not a compression of the idea; the spec is an expansion of it.
- **意味不明にしない**。復元できない詩は、復号器を持たない符号と同じで無価値。
  暗号ではなく、**最短の像**を書く
  Never cryptic. A line that cannot be unpacked is worth as much as a code with no decoder —
  write the shortest *image*, not a riddle.
- **その分野の名詞を必ず1つ入れる**(grep の取っ手になる)
  Include at least one domain noun — it is the grep handle.
- 着手したら `→ 着手` と印を付け、中身は `docs/STATE.md` の残作業へ移す
- **却下も消さない**。却下理由こそ一番効く1文になる(同じ死に方を二度しない)
  Never delete rejected ideas; the reason is usually the sharpest line on the shelf.

## 棚 / Shelf

表は使わない(2文が折り返して読めなくなる)。1件1項目 / No tables — two-line poems wrap badly.

- <詩> — `YYYY-MM-DD` 未着手

<!-- 例 / Examples:
- 訊かれる前に読んでおけば、往復は一度消える。 — `2026-08-02` 未着手
- 受け手が復号器を持たない符号は、どれほど密でも沈黙と同じ。 — `2026-08-02` 却下
-->
