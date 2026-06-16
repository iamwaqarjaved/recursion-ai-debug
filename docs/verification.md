# Verification Table

Comparing AI predictions to actual Python execution — Module 5, Component 2.

All tests run with Python 3.12. Buggy functions use `sys.setrecursionlimit(50)`.
Fixed functions use the default limit.

---

## Buggy Functions

| Function | Input | AI Predicted | Actual Output | Match? |
|----------|-------|-------------|---------------|--------|
| `countdown(n)` | `n=5` | RecursionError after ~1000 frames | Prints 5 4 3 2 1 0 -1 … RecursionError at frame 50 | ✅ Yes |
| `sum_digits(n)` | `n=123` | RecursionError — float never hits 0 | RecursionError at frame 50; n reached 9.77e-05 | ✅ Yes |
| `power(base, exp)` | `base=2, exp=3` | RecursionError — exp grows forever | RecursionError at frame 50 | ✅ Yes |
| `power(base, exp)` | `base=2, exp=-3` | RecursionError (AI claimed "all inputs") | **Returns 1 normally** — terminates! | ❌ **No** |

---

## Fixed Functions

| Function | Input | Expected | Actual | Pass? |
|----------|-------|----------|--------|-------|
| `countdown(n)` | `n=5` | Prints 5 4 3 2 1, returns None | Prints 5 4 3 2 1, returns None | ✅ |
| `sum_digits(n)` | `n=123` | 6 (1+2+3) | 6 | ✅ |
| `sum_digits(n)` | `n=999` | 27 | 27 | ✅ |
| `power(base, exp)` | `(2, 10)` | 1024 | 1024 | ✅ |
| `power(base, exp)` | `(3, 4)` | 81 | 81 | ✅ |

---

## Tree Walker Trace Verification

| Input | AI claimed result | Print-verified result | Match? |
|-------|------------------|-----------------------|--------|
| `tree_sum(5)` | 5 | 5 | ✅ |
| `tree_sum([1, 2, 3])` | 6 | 6 | ✅ |
| `tree_sum([[1,2],[3,[4,5]]])` | 15 | 15 | ✅ |
| Max stack depth (invocation 3) | 4 frames | depth=3 (0-indexed = 4 frames) | ✅ |
| Generator laziness noted | Not mentioned | Left-to-right via generator pull | ⚠️ AI omitted |

---

## How Tests Were Run

```python
import sys
sys.setrecursionlimit(50)

try:
    countdown(5)
except RecursionError as e:
    print(f"RecursionError: {e}")
```

Each buggy script wraps calls in `try/except RecursionError` and prints the exception.
Fixed scripts just call the function and print the return value.
