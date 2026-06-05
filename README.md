# Advent of Code Solutions

My personal collection of [Advent of Code](https://adventofcode.com/) solutions from previous years, all written in Python. Working through these puzzles has helped me grow as a programmer in terms of sharpening my problem solving skills, and learning to optimize my solutions.

## How it's organized

Solutions are grouped by year (`2016/`, `2021/`, `2022/`, `2023/`, `2024/`, `2025/`), and each year has a folder per day:

```
2024/
  day3/
    day3.py   # solution script
    day3.in   # my puzzle input
```

## Running a solution

Each script reads from stdin and prints to stdout. From the repo root:

**Unix/WSL:**
```bash
python 2024/day3/day3.py < 2024/day3/day3.in
```

**Windows PowerShell:**
```powershell
Get-Content 2024\day3\day3.in | python 2024\day3\day3.py
```

Just Python 3.8+ required, no external packages.
