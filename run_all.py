"""
run_all.py — Run every script in the repo and print a summary report.

Usage:
    python run_all.py
"""

import subprocess
import sys
import os


SCRIPTS = [
    ("Bug A — Missing base case",        "buggy/bug_a_no_base_case.py"),
    ("Bug B — Unreachable base case",    "buggy/bug_b_unreachable_base.py"),
    ("Bug C — Wrong direction",          "buggy/bug_c_wrong_direction.py"),
    ("Fix A — countdown",                "fixed/fix_a_countdown.py"),
    ("Fix B — sum_digits",               "fixed/fix_b_sum_digits.py"),
    ("Fix C — power",                    "fixed/fix_c_power.py"),
    ("Tree sum — clean",                 "traces/tree_sum.py"),
    ("Tree sum — instrumented trace",    "traces/tree_sum_instrumented.py"),
]


def run(label, path):
    print(f"\n{'='*60}")
    print(f"  {label}")
    print(f"  {path}")
    print(f"{'='*60}")
    result = subprocess.run(
        [sys.executable, path],
        capture_output=False,
        text=True,
    )
    return result.returncode


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    print("recursion-ai-debug — full run")
    print("Running all scripts...\n")

    for label, path in SCRIPTS:
        run(label, path)

    print(f"\n{'='*60}")
    print("All scripts executed. Review output above.")
    print("Compare buggy outputs to docs/verification.md")
    print("Compare trace output to docs/ai_transcripts.md")
