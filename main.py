"""Copy entry.txt beside this file to $MAKEFUN_OUTPUT_DIR/entry.txt.

One direct write, no temp file or rename, mode 0644, so the grader
can always read the output."""
import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

data = (HERE / "entry.txt").read_bytes()
try:
    OUT.mkdir(parents=True, exist_ok=True)
    target = OUT / "entry.txt"
    target.write_bytes(data)
    os.chmod(target, 0o644)
except OSError as exc:
    raise SystemExit(f"cannot write entry.txt to {OUT}: {exc}") from exc
