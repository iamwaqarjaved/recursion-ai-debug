"""
Bug A: Missing Base Case
========================
AI Diagnosis  : No base case — countdown() recurses forever.
AI Prediction : RecursionError after ~1000 frames.
Actual Result : RecursionError at frame 50 (limit set below).
AI Correct?   : YES

Run this file to see the error:
    python buggy/bug_a_no_base_case.py
"""

import sys
sys.setrecursionlimit(50)   # keep it safe — crashes at 50 frames, not 1000


def countdown(n):
    # BUG: no base case — this will recurse until the stack overflows
    print(n)
    return countdown(n - 1)


if __name__ == "__main__":
    print("--- Bug A: Missing Base Case ---")
    print("Calling countdown(5) with recursion limit = 50\n")
    try:
        countdown(5)
    except RecursionError as e:
        print(f"\n[RecursionError caught] {e}")
        print("AI predicted this correctly.")
