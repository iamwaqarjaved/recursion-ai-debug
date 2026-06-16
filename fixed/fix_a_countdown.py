"""
Fix A: countdown — add the missing base case
"""


def countdown(n):
    if n <= 0:          # base case: stop when we reach 0
        return
    print(n)
    return countdown(n - 1)


if __name__ == "__main__":
    print("--- Fix A: countdown(5) ---")
    countdown(5)
    print("Done.")
