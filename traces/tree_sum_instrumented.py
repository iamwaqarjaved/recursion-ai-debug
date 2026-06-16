"""
tree_sum_instrumented.py — Print-verified trace for AI comparison (Part 5)
===========================================================================
This is tree_sum() augmented with depth-tracking print statements.

Run this and compare the output against the AI trace in docs/ai_transcripts.md.
The two traces should match. Any difference is a place where the AI's mental
model of the call stack diverged from what Python actually did.

Usage:
    python traces/tree_sum_instrumented.py
"""


def tree_sum(node, depth=0):
    indent = "  " * depth
    print(f"{indent}tree_sum({node!r}, depth={depth})")

    if isinstance(node, int):
        print(f"{indent}  → base case, returning {node}")
        return node

    result = sum(tree_sum(child, depth + 1) for child in node)
    print(f"{indent}  → list node done, returning {result}")
    return result


def run_trace(label, inp, expected):
    print(f"\n{'='*60}")
    print(f"Invocation: tree_sum({inp!r})")
    print(f"Expected  : {expected}")
    print(f"{'='*60}")
    result = tree_sum(inp)
    status = "PASS" if result == expected else "FAIL"
    print(f"\n[{status}] Result = {result}  (expected {expected})")


if __name__ == "__main__":
    print("tree_sum — print-verified trace")
    print("Compare this output against docs/ai_transcripts.md (Part 4 trace)\n")

    run_trace("Invocation 1", 5, 5)
    run_trace("Invocation 2", [1, 2, 3], 6)
    run_trace("Invocation 3", [[1, 2], [3, [4, 5]]], 15)

    print("\n" + "="*60)
    print("Trace complete. Check each level against the AI trace.")
    print("Key things to verify:")
    print("  1. Call order matches")
    print("  2. Max depth matches")
    print("  3. Intermediate return values match")
    print("  4. Final result matches")
