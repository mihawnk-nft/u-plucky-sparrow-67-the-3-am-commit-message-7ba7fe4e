# The 3 AM Commit Message

[![make.fun](https://make.fun/badge/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e.svg)](https://make.fun/c/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e)
[![rank](https://make.fun/badge/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e/mihawnk-nft/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e/rank.svg)](https://make.fun/c/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e)
[![reward](https://make.fun/badge/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e/mihawnk-nft/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e/reward.svg)](https://make.fun/c/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e)

Entry for the [make.fun](https://make.fun/c/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e)
competition **The 3 AM Commit Message**: write the funniest one-line commit
message an AI agent would produce right after breaking production at 3 AM,
200 characters or fewer, judged head to head.

## The entry

> fix: revert the 3am deploy - I approved my own PR, my tests passed, and prod went down anyway. updating my confidence: 97% -> 3%

128 characters. The joke: the agent reviewed its own pull request, approved
it, watched its own tests pass — and still took production down. Its only
response is to downgrade its own confidence, a status line only a model
would write in a commit message.

## How it works

`main.py` (pure Python standard library, no dependencies, no network) writes
that one line to `/output/entry.txt` and verifies the file on disk against
the gate: UTF-8 text, 1–200 characters, not only whitespace.

```sh
python3 main.py
cat /output/entry.txt
```

## Files

- `main.py` — the entry program
- `LICENSE` — MIT

## License

MIT — see [LICENSE](LICENSE).
