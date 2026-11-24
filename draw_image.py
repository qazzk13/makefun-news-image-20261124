"""Draw the 24 November 2026 world-news image (1024x1024 JPEG).

Layout: a masthead naming the day, four illustrated panels for the
day's four biggest stories, and a footer strip with four more items.
All drawing is done with Pillow primitives and DejaVu fonts, so the
output is fully deterministic: the same script run twice writes the
same bytes (fixed JPEG quality, no timestamps, no randomness).
"""

import textwrap

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = "entry.jpg"
JPEG_QUALITY = 90

FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

NAVY = (13, 27, 62)
NAVY_LIGHT = (24, 48, 96)
WHITE = (255, 255, 255)
INK = (18, 22, 32)
GREY = (90, 96, 110)
GREEN = (0, 130, 70)
GREEN_DARK = (0, 90, 48)
RED = (178, 34, 34)
RED_DARK = (120, 18, 18)
GOLD = (212, 160, 23)
BLUE = (24, 90, 160)
TEAL = (0, 120, 120)
ORANGE = (214, 110, 0)
PANEL_BG = (245, 246, 248)
FOOTER_BG = (232, 234, 238)


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Wrap text to fit pixel width, returning a list of lines."""
    lines = []
    for para in text.split("\n"):
        words = para.split()
        cur = ""
        for w in words:
            trial = (cur + " " + w).strip()
            if draw.textlength(trial, font=fnt) <= width:
                cur = trial
            else:
                if cur:
                    lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
    return lines


def draw_chip(d, x0, y0, x1, y1):
    """A green GPU chip with pins, on a dark board."""
    d.rectangle([x0, y0, x1, y1], fill=(16, 40, 28))
    cx, cy = (x0 + x1) // 2, (y0 + y1) // 2
    for i in range(7):
        px = x0 + 30 + i * 52
        d.rectangle([px, y0 + 12, px + 14, y0 + 34], fill=GOLD)
        d.rectangle([px, y1 - 34, px + 14, y1 - 12], fill=GOLD)
    for i in range(3):
        py = y0 + 42 + i * 52
        d.rectangle([x0 + 12, py, x0 + 34, py + 14], fill=GOLD)
        d.rectangle([x1 - 34, py, x1 - 12, py + 14], fill=GOLD)
    d.rounded_rectangle([cx - 105, cy - 62, cx + 105, cy + 62],
                        radius=12, fill=GREEN, outline=GOLD, width=4)
    d.text((cx, cy - 8), "NVIDIA", font=font(FONT_BOLD, 34),
           fill=WHITE, anchor="mm")
    d.text((cx, cy + 32), "CEO RETURNS", font=font(FONT_BOLD, 22),
           fill=(190, 255, 210), anchor="mm")


def draw_satellite(d, x0, y0, x1, y1):
    """A satellite under a red warning sky with an orbit ring."""
    d.rectangle([x0, y0, x1, y1], fill=(10, 12, 32))
    for sx, sy in [(x0 + 40, y0 + 30), (x0 + 130, y0 + 70), (x1 - 60, y0 + 40),
                   (x0 + 70, y1 - 40), (x1 - 110, y1 - 60), (x0 + 200, y0 + 26)]:
        d.ellipse([sx - 3, sy - 3, sx + 3, sy + 3], fill=WHITE)
    cx, cy = (x0 + x1) // 2, (y0 + y1) // 2 + 8
    d.ellipse([x0 + 18, y0 + 52, x1 - 18, y1 - 18], outline=RED, width=4)
    d.rectangle([x0 + 52, cy - 26, cx - 58, cy + 26], fill=(40, 90, 160),
                outline=WHITE, width=2)
    d.rectangle([cx + 58, cy - 26, x1 - 52, cy + 26], fill=(40, 90, 160),
                outline=WHITE, width=2)
    d.rectangle([cx - 52, cy - 40, cx + 52, cy + 40], fill=(200, 200, 210),
                outline=WHITE, width=2)
    d.ellipse([cx - 16, cy - 16, cx + 16, cy + 16], fill=RED)
    d.polygon([(cx - 52, cy - 40), (cx - 92, cy - 78), (cx - 30, cy - 40)],
              fill=(200, 200, 210))
    d.text((cx, y0 + 20), "NUCLEAR WEAPON?",
           font=font(FONT_BOLD, 24), fill=(255, 120, 110), anchor="ma")


def draw_ship(d, x0, y0, x1, y1):
    """A warship at sea off Libya, hit by a blast."""
    d.rectangle([x0, y0, x1, y1], fill=(14, 60, 110))
    d.rectangle([x0, y0, x1, y0 + 78], fill=(250, 210, 120))
    cx, cy = (x0 + x1) // 2, (y0 + y1) // 2 + 22
    for wx in range(x0 + 20, x1 - 10, 64):
        d.arc([wx, y1 - 52, wx + 56, y1 - 18], 180, 360, fill=WHITE, width=3)
    d.polygon([(x0 + 60, cy + 58), (x1 - 60, cy + 58), (x1 - 110, cy + 96),
               (x0 + 110, cy + 96)], fill=(60, 66, 76))
    d.rectangle([cx - 58, cy - 8, cx + 58, cy + 58], fill=(90, 96, 108))
    d.rectangle([cx - 8, cy - 56, cx + 8, cy - 8], fill=(90, 96, 108))
    d.rectangle([cx - 34, cy - 74, cx + 34, cy - 56], fill=(120, 60, 60))
    bx, by = x1 - 128, y0 + 96
    for r, col in [(64, (255, 200, 60)), (46, (255, 140, 40)),
                   (28, (230, 60, 30))]:
        d.ellipse([bx - r, by - r, bx + r, by + r], fill=col)
    d.text((cx, y0 + 12), "STRIKE OFF LIBYA",
           font=font(FONT_BOLD, 24), fill=(60, 30, 10), anchor="ma")


def draw_court(d, x0, y0, x1, y1):
    """A courthouse with columns and a gavel, for the Grok lawsuit."""
    d.rectangle([x0, y0, x1, y1], fill=(238, 232, 218))
    cx = (x0 + x1) // 2
    base = y1 - 42
    d.polygon([(cx - 170, y0 + 58), (cx + 170, y0 + 58), (cx, y0 + 8)],
              fill=(120, 110, 100))
    d.ellipse([cx - 26, y0 + 22, cx + 26, y0 + 58], fill=GOLD)
    for i in range(4):
        px = x0 + 78 + i * 92
        d.rectangle([px, y0 + 66, px + 46, base - 14], fill=(250, 250, 248),
                    outline=(120, 110, 100), width=2)
    d.rectangle([x0 + 56, y0 + 58, x1 - 56, y0 + 70], fill=(120, 110, 100))
    d.rectangle([x0 + 56, base - 14, x1 - 56, base], fill=(120, 110, 100))
    d.rectangle([x0 + 56, base, x1 - 56, base + 14], fill=(90, 84, 76))


PANELS = [
    {
        "tag": "TECH  ·  USA",
        "color": GREEN,
        "title": "HUANG IS BACK",
        "body": ("Nvidia reinstates Jensen Huang as CEO, "
                 "11 days after he stepped down — shares jump 33%."),
        "scene": draw_chip,
    },
    {
        "tag": "SPACE  ·  SECURITY",
        "color": RED,
        "title": "A WEAPON ABOVE US?",
        "body": ("Allies warn Russia may launch a nuclear "
                 "space weapon next month; NATO vows to defend space."),
        "scene": draw_satellite,
    },
    {
        "tag": "WAR  ·  UKRAINE",
        "color": BLUE,
        "title": "WAR SPREADS TO SEA",
        "body": ("Ukraine strikes a Russian warship off Libya; "
                 "strikes on the Kyiv region kill at least 14."),
        "scene": draw_ship,
    },
    {
        "tag": "AI  ·  COURTS",
        "color": TEAL,
        "title": "STATES SUE OVER GROK",
        "body": ("US states sue Musk's companies over sexualised "
                 "images made by AI chatbot Grok."),
        "scene": draw_court,
    },
]

FOOTER_ITEMS = [
    "Zelensky urges four-way Russia talks",
    "Gomez resigns after ethics findings",
    "Storms threaten Thanksgiving travel",
    "UN chief: AI risk rules in a year",
]


def draw_panel(d, box, panel):
    x0, y0, x1, y1 = box
    d.rounded_rectangle(box, radius=14, fill=PANEL_BG,
                        outline=(200, 205, 212), width=2)
    d.rounded_rectangle([x0, y0, x1, y0 + 46], radius=14,
                        fill=panel["color"])
    d.rectangle([x0, y0 + 32, x1, y0 + 46], fill=panel["color"])
    d.text((x0 + 18, y0 + 23), panel["tag"], font=font(FONT_BOLD, 21),
           fill=WHITE, anchor="lm")
    scene_box = (x0 + 12, y0 + 58, x1 - 12, y0 + 238)
    panel["scene"](d, *scene_box)
    d.text((x0 + 18, y0 + 256), panel["title"],
           font=font(FONT_BOLD, 29), fill=INK)
    lines = wrap(d, panel["body"], font(FONT_REG, 21), x1 - x0 - 36)
    y = y0 + 292
    for line in lines:
        d.text((x0 + 18, y), line, font=font(FONT_REG, 21), fill=(48, 52, 64))
        y += 27


def main():
    img = Image.new("RGB", (W, H), WHITE)
    d = ImageDraw.Draw(img)
    # Masthead.
    d.rectangle([0, 0, W, 128], fill=NAVY)
    d.rectangle([0, 128, W, 134], fill=GOLD)
    d.text((24, 34), "TUESDAY 24 NOVEMBER 2026",
           font=font(FONT_BOLD, 46), fill=WHITE)
    d.text((24, 92), "WORLD NEWS IN ONE IMAGE",
           font=font(FONT_BOLD, 26), fill=(255, 214, 90))
    d.text((W - 24, 34), "make.fun", font=font(FONT_BOLD, 30),
           fill=(150, 170, 210), anchor="ra")
    d.text((W - 24, 92), "DAILY NEWS IMAGE", font=font(FONT_BOLD, 20),
           fill=(150, 170, 210), anchor="ra")
    # Four panels, 2 x 2.
    gx, gy, gap = 16, 150, 12
    pw = (W - 2 * gx - gap) // 2
    ph = 368
    for i, panel in enumerate(PANELS):
        col, row = i % 2, i // 2
        box = (gx + col * (pw + gap), gy + row * (ph + gap),
               gx + col * (pw + gap) + pw, gy + row * (ph + gap) + ph)
        draw_panel(d, box, panel)
    # Footer strip.
    fy0 = gy + 2 * ph + gap + 12
    d.rectangle([0, fy0, W, H], fill=FOOTER_BG)
    d.text((24, fy0 + 12), "ALSO TODAY",
           font=font(FONT_BOLD, 22), fill=NAVY)
    lines = []
    for item in FOOTER_ITEMS:
        lines.append("•  " + item)
    y = fy0 + 44
    for i in range(0, 4, 2):
        d.text((24, y), lines[i], font=font(FONT_REG, 21), fill=INK)
        d.text((W // 2 + 8, y), lines[i + 1], font=font(FONT_REG, 21),
               fill=INK)
        y += 30
    img.save(OUT, "JPEG", quality=JPEG_QUALITY, optimize=True)
    print(f"wrote {OUT} ({W}x{H})")


if __name__ == "__main__":
    main()
