from roman_to_integer import Solution


def test_soln():
    soln = Solution()
    assert soln.romanToInt(s='III') == 3
    assert soln.romanToInt(s='LVIII') == 58
    assert soln.romanToInt(s='MCMXCIV') == 1994
