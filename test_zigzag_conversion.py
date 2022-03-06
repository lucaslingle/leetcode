from zigzag_conversion import Solution


def test_soln():
    soln = Solution()
    assert soln.convert('PAYPALISHIRING', 3) == 'PAHNAPLSIIGYIR'
    assert soln.convert('PAYPALISHIRING', 4) == 'PINALSIGYAHRPI'
    assert soln.convert('A', 1) == 'A'
    assert soln.convert('AB', 1) == 'AB'
