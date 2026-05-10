import shutil
from datetime import datetime, timedelta
from pathlib import Path

DAILY_DIR = Path("docs/daily")
DB_DIR = Path("db")
DAYS = 60

DAILY_DIR.mkdir(parents=True, exist_ok=True)

puzzles = sorted(DB_DIR.glob("single_*.txt")) + sorted(DB_DIR.glob("multi_*.txt"))

existing = sorted(DAILY_DIR.glob("*.txt"))
if existing:
    last_date = datetime.strptime(existing[-1].stem, "%Y-%m-%d")
    start_index = len(existing)
else:
    last_date = datetime.today() - timedelta(days=1)
    start_index = 0

for i in range(DAYS):
    idx = start_index + i
    if idx >= len(puzzles):
        print(f"Ran out of puzzles after {i} days ({len(puzzles)} total available)")
        break

    date = last_date + timedelta(days=i + 1)
    dest = DAILY_DIR / f"{date.strftime('%Y-%m-%d')}.txt"

    shutil.copy2(puzzles[idx], dest)
    print(f"{dest.name}  <-  {puzzles[idx].name}")

print(f"\nDone! {min(DAYS, len(puzzles) - start_index)} files written to {DAILY_DIR}")
