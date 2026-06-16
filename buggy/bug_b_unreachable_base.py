"""
Bug B: Base Case That's Never Reached
======================================
AI Diagnosis  : Uses true division (/) instead of floor division (//).
                n becomes a float and never equals exactly 0.
AI Prediction : RecursionError — n shrinks but never hits the base case.
Actual Result : RecursionError — n reached 0.000097... not 0.
AI Correct?   : YES

Run this file to see the error:
    python buggy/bug_b_unreachable_base.py
"""

import sys
sys.setrecursionlimit(50)


def sum_digits(n):
    # BUG: n / 10 produces a float.
    # e.g. 123 -> 12.3 -> 1.23 -> 0.123 -> 0.0123 -> ...
    # It approaches 0 but never equals it exactly, so base case never fires.
    if n == 0:
        return 0
    return (n % 10) + sum_digits(n / 10)   # should be n // 10


if __name__ == "__main__":
    print("--- Bug B: Base Case Never Reached ---")
    print("Calling sum_digits(123) with recursion limit = 50\n")
    try:
        result = sum_digits(123)
        print(f"Result: {result}")
    except RecursionError as e:
        print(f"\n[RecursionError caught] {e}")
        print("AI predicted this correctly.")
        print("Tip: try sum_digits(1) and watch n become 0.1, 0.01, 0.001...")
