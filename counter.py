#!/usr/bin/env python3
"""Code Line Counter - counts code, comment and blank lines per language."""
import argparse
import os

LANGUAGES = {
    ".py": ("Python", "#"),
    ".js": ("JavaScript", "//"),
    ".ts": ("TypeScript", "//"),
    ".java": ("Java", "//"),
    ".c": ("C", "//"),
    ".cpp": ("C++", "//"),
    ".go": ("Go", "//"),
    ".rb": ("Ruby", "#"),
    ".php": ("PHP", "//"),
    ".sh": ("Shell", "#"),
    ".sql": ("SQL", "--"),
    ".html": ("HTML", None),
    ".css": ("CSS", None),
}
SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv", "dist", "build"}


def count_file(path, comment_prefix):
    """Return (code, comments, blank) line counts for one file."""
    code = comments = blank = 0
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                s = line.strip()
                if not s:
                    blank += 1
                elif comment_prefix and s.startswith(comment_prefix):
                    comments += 1
                else:
                    code += 1
    except OSError:
        pass
    return code, comments, blank


def scan(root):
    """Return {language: {"files": n, "code": n, "comments": n, "blank": n}}."""
    stats = {}
    for folder, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for name in files:
            ext = os.path.splitext(name)[1].lower()
            if ext not in LANGUAGES:
                continue
            lang, prefix = LANGUAGES[ext]
            c, m, b = count_file(os.path.join(folder, name), prefix)
            s = stats.setdefault(lang, {"files": 0, "code": 0, "comments": 0, "blank": 0})
            s["files"] += 1
            s["code"] += c
            s["comments"] += m
            s["blank"] += b
    return stats


def format_table(stats):
    header = f"{'Language':<12}{'Files':>6}{'Code':>8}{'Comments':>10}{'Blank':>8}"
    lines = [header, "-" * len(header)]
    total = {"files": 0, "code": 0, "comments": 0, "blank": 0}
    for lang, s in sorted(stats.items(), key=lambda kv: -kv[1]["code"]):
        lines.append(f"{lang:<12}{s['files']:>6}{s['code']:>8}{s['comments']:>10}{s['blank']:>8}")
        for k in total:
            total[k] += s[k]
    lines.append("-" * len(header))
    lines.append(f"{'TOTAL':<12}{total['files']:>6}{total['code']:>8}{total['comments']:>10}{total['blank']:>8}")
    return "\n".join(lines)


def main():
    p = argparse.ArgumentParser(description="Count lines of code by language")
    p.add_argument("path", nargs="?", default=".", help="folder to scan (default: current)")
    args = p.parse_args()
    stats = scan(args.path)
    print(format_table(stats) if stats else "No supported source files found.")


if __name__ == "__main__":
    main()
