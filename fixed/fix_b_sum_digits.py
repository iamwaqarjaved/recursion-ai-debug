"""
Fix B: sum_digits — use floor division so n stays an integer and reaches 0
"""


def sum_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_digits(n // 10)   # // instead of /


if __name__ == "__main__":
    print("--- Fix B: sum_digits ---")
    print(f"sum_digits(123) = {sum_digits(123)}")   # 1+2+3 = 6
    print(f"sum_digits(9)   = {sum_digits(9)}")     # 9
    print(f"sum_digits(999) = {sum_digits(999)}")   # 27
