#"""
from reverse_integer import Solution


def test_soln():
    soln = Solution()
    #assert soln.find_power(64) == 2
    #assert soln.find_power(-64) == 2
    assert soln.reverse(123) == 321
    assert soln.reverse(12345) == 54321
    assert soln.reverse(-1) == -1
    assert soln.reverse(-123) == -321
    # 9646324351
    assert soln.reverse(1534236469) == 0
    assert soln.reverse(-2147483412) == -2143847412


if __name__ == '__main__':
    test_soln()
#"""