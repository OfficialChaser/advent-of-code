# Advent of Code — Solutions Collection

This repository contains my Advent of Code solutions organized by year and day. Each day folder contains a Python solution (`dayN.py`) and the input file used for that puzzle (`dayN.in`).

Repository layout
- `2016/`, `2021/`, `2022/`, `2023/`, `2024/`, `2025/` — top-level year folders
- Each year contains `dayX/` subfolders (e.g. `day1/`) with:
  - `dayX.py` — solution script (Python)
  - `dayX.in` — puzzle input used by the script

Running solutions
- Requirements: Python 3.8+ (no external packages required unless a solution states otherwise).
- Run a solution from the repository root. Example (Unix-like shells or WSL):

```bash
python 2024/day3/day3.py < 2024/day3/day3.in
```

On Windows PowerShell you can use:

```powershell
Get-Content 2024\day3\day3.in | python 2024\day3\day3.py
```

Notes and conventions
- Solutions are written as standalone scripts that read input from stdin and print results to stdout.
- Filenames follow the `dayN.py` / `dayN.in` pattern for easy discovery and execution.

Contributing
- To add a solution: create a new `dayX/` folder under the appropriate year with `dayX.py` and `dayX.in`.
- Follow the existing style: simple scripts, clear variable names, and minimal external dependencies.

License
- No license specified. Add a `LICENSE` file if you want to set repository licensing.

Enjoy exploring the puzzles and solutions!
