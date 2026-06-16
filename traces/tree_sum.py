"""
tree_sum.py — Recursive tree walker (sum all integer leaves in a nested list)
==============================================================================
This is the working recursive function used for AI trace verification in Part 4.

The AI traced 3 invocations call-by-call. Run tree_sum_instrumented.py
to generate print-verified output and compare against the AI trace in
docs/ai_transcripts.md.
"""


def tree_sum(node):
    """
    Recursively sum all integer leaves in a nested list structure.

    Base case  : node is an integer -> return it directly
    Recursive  : node is a list -> sum the tree_sum of each child

    Examples:
        tree_sum(5)                    -> 5
        tree_sum([1, 2, 3])            -> 6
        tree_sum([[1, 2], [3, [4, 5]]]) -> 15
    """
    if isinstance(node, int):
        return node
    return sum(tree_sum(child) for child in node)


if __name__ == "__main__":
    tests = [
        (5,                         5),
        ([1, 2, 3],                 6),
        ([[1, 2], [3, [4, 5]]],    15),
        ([[[1]], [[2]], [[3]]],      6),
        (0,                         0),
    ]

    print("--- tree_sum test cases ---\n")
    all_pass = True
    for inp, expected in tests:
        result = tree_sum(inp)
        status = "✓" if result == expected else "✗"
        print(f"  {status}  tree_sum({inp!r:<30} ) = {result}  (expected {expected})")
        if result != expected:
            all_pass = False

    print()
    print("All tests passed." if all_pass else "SOME TESTS FAILED.")
