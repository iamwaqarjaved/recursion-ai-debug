"""
Fix C: power — change exp + 1 to exp - 1 so it counts down toward 0
"""


def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)   # exp - 1 moves toward base case


if __name__ == "__main__":
    print("--- Fix C: power ---")
    print(f"power(2, 0)  = {power(2, 0)}")   # 1
    print(f"power(2, 3)  = {power(2, 3)}")   # 8
    print(f"power(2, 10) = {power(2, 10)}")  # 1024
    print(f"power(3, 4)  = {power(3, 4)}")   # 81
