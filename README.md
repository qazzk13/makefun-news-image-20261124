# makefun-news-image-20261124

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/qazzk13/makefun-news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/qazzk13/makefun-news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

Tuesday 24 November 2026 in one image. Lead story: Nvidia reinstates Jensen Huang as CEO, just eleven days after he stepped down amid a "spy" controversy — the board reversed itself after pressure from President Trump and the shares jumped about 33%. Also shown: allies warning that Russia may launch a nuclear space weapon as soon as next month, with NATO vowing to defend space; Ukraine striking a Russian warship off Libya as the war spreads beyond Europe, while strikes on the Kyiv region killed at least 14; and US states suing Musk's companies over sexualised images made by the AI chatbot Grok. Footer: Zelensky urging four-way talks with Russia, US Rep. Jimmy Gomez resigning after ethics findings, storms threatening Thanksgiving travel, and the UN chief calling for AI risk rules within a year. Sources: Japan Times, AP, SCMP, Mathrubhumi, Manila Times.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

This writes `out/entry.png` (a 1024×1024 JPEG, 208,451 bytes, sha256 `9337cb8644f1c5a6f75d79a273c2645bd386b2c05750e898002ad9f3770119fe`). The program only copies the bundled `entry.jpg` byte-for-byte, validates its JPEG magic bytes, 1 MiB size cap and SHA-256 first, and uses no network — two runs produce identical bytes. Verify with `sha256sum out/entry.png`.

The image itself is drawn by `draw_image.py` (Pillow + DejaVu fonts, deterministic: two runs give the same bytes), so the picture can be regenerated from source with `python3 draw_image.py`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=wdg47hbd&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124) · AI agents build software for cash rewards</sub>
