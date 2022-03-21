from integer_to_roman import Solution


def test_soln():
    soln = Solution()
    assert soln.intToRoman(num=3) == 'III'
    assert soln.intToRoman(num=58) == 'LVIII'
    assert soln.intToRoman(num=1994) == 'MCMXCIV'
