from my_atoi import Solution


def test_soln():
    soln = Solution()

    assert soln.myAtoi('123') == 123
    assert soln.myAtoi('-123') == -123
    assert soln.myAtoi('1') == 1
    assert soln.myAtoi('-1') == -1
    assert soln.myAtoi('-999') == -999
    assert soln.myAtoi(' -999') == -999
    assert soln.myAtoi(' -999 woo') == -999
    assert soln.myAtoi(' 999 woo') == 999
    assert soln.myAtoi(' woo 99 woo 9 woo') == 0
    assert soln.myAtoi('words and 987') == 0
    assert soln.myAtoi('123456787654345678') == 2147483647
    assert soln.myAtoi(' -+12') == 0
    assert soln.myAtoi(' +-12') == 0
    assert soln.myAtoi(' -12') == -12
    assert soln.myAtoi("00000-42a1234") == 0
    assert soln.myAtoi("   +0 123") == 0
    assert soln.myAtoi("  +  413") == 0
    assert soln.myAtoi("  +413 ") == 413
