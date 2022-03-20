class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x > 0 and x % 10 == 0:
            return False
        if x // 10 == 0:
            return True

        # positive int greater than 10, not ending with a zero.
        left_power = 0
        y = x
        while y // 10 > 0:
            left_power += 1
            y //= 10

        # repeatedly compare
        left_mask = 10 ** left_power
        right_mask = 10 ** 0
        while left_mask > right_mask:
            left_digit = (x // left_mask) % 10
            right_digit = (x // right_mask) % 10
            if left_digit != right_digit:
                return False
            left_mask //= 10
            right_mask *= 10
        return True
