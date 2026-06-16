# AI Debugging Transcripts

Full AI conversation logs for all 3 buggy functions — Module 5, Component 1.

---

## Bug A — Missing Base Case (`buggy/bug_a_no_base_case.py`)

**Prompt sent to AI:**

> Here is a Python recursive function. Please: (a) identify the bug, (b) predict what happens at runtime with input n=5, (c) propose the fix.
>
> ```python
> def countdown(n):
>     print(n)
>     return countdown(n - 1)
> ```

**AI Response (summarized):**

**(a) Bug identified:**
The function has no base case. Every recursive call to `countdown(n-1)` will execute unconditionally — there is no condition that terminates the recursion.

**(b) Runtime prediction:**
With `n=5`, the function will print `5, 4, 3, 2, 1, 0, -1, -2 ...` and continue decrementing indefinitely. Python's default recursion limit is approximately 1000, so a `RecursionError: maximum recursion depth exceeded` will be raised after about 1000 frames.

**(c) Proposed fix:**
```python
def countdown(n):
    if n <= 0:       # base case
        return
    print(n)
    return countdown(n - 1)
```

**Verification result:** ✅ AI was correct. RecursionError raised at frame 50 (with `sys.setrecursionlimit(50)`).

---

## Bug B — Base Case Never Reached (`buggy/bug_b_unreachable_base.py`)

**Prompt sent to AI:**

> Here is a Python recursive function. Please: (a) identify the bug, (b) predict what happens at runtime with input n=123, (c) propose the fix.
>
> ```python
> def sum_digits(n):
>     if n == 0:
>         return 0
>     return (n % 10) + sum_digits(n / 10)
> ```

**AI Response (summarized):**

**(a) Bug identified:**
The function uses true division (`n / 10`) instead of integer floor division (`n // 10`). This means `n` immediately becomes a float after the first recursive call:
- `sum_digits(123)` → calls `sum_digits(12.3)`
- `sum_digits(12.3)` → calls `sum_digits(1.23)`
- `sum_digits(1.23)` → calls `sum_digits(0.123)`
- ...and so on, approaching but never reaching exactly `0.0`

The base case `if n == 0` uses integer equality. A float like `0.000097...` will never be `== 0`, so the base case is structurally unreachable with any positive integer input.

**(b) Runtime prediction:**
`RecursionError` — `n` will shrink toward zero but never reach it exactly due to floating-point representation. The stack overflows before any base case fires.

**(c) Proposed fix:**
```python
def sum_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_digits(n // 10)   # floor division keeps n an integer
```

**Verification result:** ✅ AI was correct. With `n=123`, `n` reached `9.765625e-05` before the RecursionError.

---

## Bug C — Parameter Moving in Wrong Direction (`buggy/bug_c_wrong_direction.py`)

**Prompt sent to AI:**

> Here is a Python recursive function. Please: (a) identify the bug, (b) predict what happens at runtime with input base=2, exp=3, (c) propose the fix.
>
> ```python
> def power(base, exp):
>     if exp == 0:
>         return 1
>     return base * power(base, exp + 1)
> ```

**AI Response (summarized):**

**(a) Bug identified:**
The recursive call uses `exp + 1` instead of `exp - 1`. The base case requires `exp == 0`, but each call increases `exp` rather than decreasing it. The function moves *away* from its base case on every call.

**(b) Runtime prediction:**
For `power(2, 3)`: `exp` goes `3 → 4 → 5 → 6 → ...` without bound, never reaching `0`. This will result in a `RecursionError` for **all inputs**.

**(c) Proposed fix:**
```python
def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)
```

**Verification result:** ❌ **AI was PARTIALLY WRONG.**

- `power(2, 3)` → RecursionError ✅ (AI correct)
- `power(2, -3)` → **Returns `1` normally** ❌ (AI predicted RecursionError)

**Why:** With a negative starting exponent, `exp + 1` counts *upward toward* `0`. The path is `-3 → -2 → -1 → 0` and the base case fires normally. The AI failed to consider negative inputs.

See `docs/wrong_prediction.md` for full analysis.
