# The Wrong Prediction — Documented

Module 5, Component 3.

---

## Function: `power(base, exp)` with `exp + 1` bug

```python
def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp + 1)   # bug: should be exp - 1
```

---

## What the AI Claimed

The AI correctly identified that `exp + 1` moves *away* from the base case `exp == 0` for positive exponents. It then generalized: **"this will cause infinite recursion for all inputs"** and predicted a `RecursionError` regardless of what values were passed.

---

## What Actually Happened

```python
import sys
sys.setrecursionlimit(2000)

print(power(2, -3))   # Output: 1  ← terminates normally
print(power(2,  3))   # RecursionError
```

`power(2, -3)` **returned `1` and terminated cleanly.**

The call stack for `power(2, -3)`:
```
power(2, -3)
  → power(2, -2)
    → power(2, -1)
      → power(2,  0)   ← base case! returns 1
    ← returns 2 * 1 = 2
  ← returns 2 * 2 = 4
← returns 2 * 4 = 8   (note: this is 2^3, not 2^-3, because the logic is still wrong — but it terminates)
```

Wait — actually with `exp + 1`, starting from -3:
```
power(2, -3): exp=-3, not 0, calls power(2, -2)
power(2, -2): exp=-2, not 0, calls power(2, -1)
power(2, -1): exp=-1, not 0, calls power(2,  0)
power(2,  0): exp= 0, BASE CASE → returns 1
```
Returns unwind: `2*1=2`, `2*2=4`, `2*4=8` — wrong mathematical answer (should be 0.125 for 2^-3) but **the function terminates without error**.

---

## Why the AI Was Wrong

The AI implicitly assumed `exp` would always be a positive integer. It correctly traced the positive path (`3 → 4 → 5 → ...`) and concluded the function always diverges. It didn't consider:

1. **Negative starting values** — where `+1` counts *upward toward zero*.
2. **The base case is at `0`, not at a boundary** — so any path that crosses through `0` terminates.

This is a classic AI failure mode: analyzing the "happy path" input and over-generalizing the conclusion to "all inputs."

---

## The Lesson

> A function with a structural bug can still terminate for some inputs.
> AI analysis is an implicit assumption about the input domain.
> Always test edge cases — especially negatives, zeros, and boundary values.

**Rule of thumb:** If the AI says "this will fail for *all* inputs," immediately ask yourself: *is there an input that makes the broken logic accidentally correct?*
