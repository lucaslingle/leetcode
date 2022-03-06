import sys

"""
class Solution:
    def find_power(self, x: int) -> int:
        sign_x = 1 if x >= 0 else -1
        for power in range(0, 10):
            if sign_x * x // (10 ** power) == 0:
                return power

    def reverse(self, x: int) -> int:
        sign_x = 1 if x >= 0 else -1
        starting_pow = self.find_power(x)
        result = 0
        for power in range(starting_pow - 1, -1, -1):  # starting_pow, ..., 0.
            digit = (sign_x * x // (10 ** power)) % 10
            if x > 0:
                result += digit * (10 ** (starting_pow - power - 1))
            else:
                result -= digit * (10 ** (starting_pow - power - 1))
        return result
"""


class Solution:
    def reverse(self, x):
        sign_x = 1 if x >= 0 else -1
        x = sign_x * x
        ans = 0
        while x > 0:
            #if ans > 2147483647 // 10:
            #    return 0
            temp = 10 * ans + (x % 10)
            ans = temp
            x //= 10
            print(ans)
        if ans > 2147483647:
            return 0
        return sign_x * ans
