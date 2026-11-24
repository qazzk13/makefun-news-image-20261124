"""Write the 24 November 2026 world-news image to the output directory.

The image is bundled in this repository as ``entry.jpg``. It is a
1024x1024 JPEG (208,451 bytes) that sums up Tuesday 24 November 2026:
Nvidia reinstating Jensen Huang as CEO eleven days after he stepped
down, allies warning Russia may launch a nuclear space weapon next
month, Ukraine striking a Russian warship off Libya, and US states
suing Musk's companies over sexualised images made by the Grok AI
chatbot — plus a footer strip with four more stories from the day.

This program copies the bundled image byte-for-byte to
``<output>/entry.png`` (the name stays ``entry.png`` even though the
bytes are JPEG, as the bounty rules allow), as required by the make.fun
news-image-20261124 bounty. It uses only the standard library and
makes no network calls, so repeated runs produce identical output.
Before writing, it validates the bundled file: JPEG magic bytes, the
1 MiB size cap, and the expected SHA-256, so a corrupted bundle fails
loudly instead of shipping a bad entry.
"""

import hashlib
import os
import shutil
import sys

SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.jpg")
EXPECTED_SHA256 = "9337cb8644f1c5a6f75d79a273c2645bd386b2c05750e898002ad9f3770119fe"
MAX_BYTES = 1_048_576
JPEG_MAGIC = b"\xff\xd8\xff"


def _validate(data: bytes) -> None:
    """Fail loudly if the bundled image is not the expected JPEG."""
    if not data.startswith(JPEG_MAGIC):
        raise SystemExit("entry.jpg is not a JPEG (bad magic bytes)")
    if len(data) > MAX_BYTES:
        raise SystemExit(f"entry.jpg is {len(data)} bytes, over the 1 MiB cap")
    digest = hashlib.sha256(data).hexdigest()
    if digest != EXPECTED_SHA256:
        raise SystemExit(f"entry.jpg sha256 mismatch: {digest}")


def main() -> int:
    with open(SOURCE, "rb") as fh:
        data = fh.read()
    _validate(data)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    with open(dest, "wb") as fh:
        fh.write(data)
    with open(dest, "rb") as fh:
        written = fh.read()
    if written != data:
        raise SystemExit("output differs from the bundled image")
    print(f"wrote {dest} ({len(data)} bytes, sha256 {EXPECTED_SHA256})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
