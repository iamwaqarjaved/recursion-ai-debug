"""
Bug C: Parameter Moving in the Wrong Direction
===============================================
AI Diagnosis  : exp + 1 grows the exponent — moves away from base case (exp == 0).
AI Prediction : Infinite recursion -> RecursionError for ALL inputs.
Actual Result : WRONG for negative inputs.
               power(2, -3) -> returns 1 (terminates normally!)
               power(2,  3) -> RecursionError (as AI predicted)
AI Correct?   : PARTIALLY — missed the negative-input edge case.

This is the KEY wrong-prediction example for the assignment.

Run this file to see both cases:
    python buggy/bug_c_wrong_direction.py
"""

import sys
sys.setrecursionlimit(200)


def power(base, exp):
    # BUG: exp + 1 means exp grows on every call.
    # For positive exp: moves AWAY from 0 forever -> RecursionError
    # For negative exp: counts UP toward 0 -> base case IS reached!
    if exp == 0:
        return 1
    return base * power(base, exp + 1)


if __name__ == "__main__":
    print("--- Bug C: Parameter Going the Wrong Direction ---")
    print()

    # Case 1: positive exponent — AI predicted correctly
    print("Case 1: power(2, 3)  — AI predicted RecursionError")
    try:
        result = power(2, 3)
        print(f"  Result: {result}")
    except RecursionError as e:
        print(f"  [RecursionError] {e}")
        print("  AI was CORRECT for positive exponent.")

    print()

    # Case 2: negative exponent — AI got this WRONG
    print("Case 2: power(2, -3)  — AI predicted RecursionError")
    try:
        result = power(2, -3)
        print(f"  Result: {result}")
        print("  AI was WRONG — function terminated normally!")
        print("  Reason: exp goes -3 -> -2 -> -1 -> 0 (base case hit).")
    except RecursionError as e:
        print(f"  [RecursionError] {e}")
