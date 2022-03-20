from regular_expression_matching import Solution


def test_get_next_p_token():
    soln = Solution()
    assert soln.get_next_p_token('abc') == ('a', 'bc')
    assert soln.get_next_p_token('abc*') == ('a', 'bc*')
    assert soln.get_next_p_token('ab*c') == ('a', 'b*c')
    assert soln.get_next_p_token('a*bc') == ('a*', 'bc')
    assert soln.get_next_p_token('ab.*') == ('a', 'b.*')
    assert soln.get_next_p_token('ab*.') == ('a', 'b*.')
    assert soln.get_next_p_token('a*b.') == ('a*', 'b.')


def test_is_match():
    soln = Solution()
    # equal length, no stars, no dots, match
    assert soln.isMatch('abc', 'abc')
    assert soln.isMatch('def', 'def')
    assert soln.isMatch('ghi', 'ghi')
    # equal length, no stars, dots, match
    assert soln.isMatch('abc', '.bc')
    assert soln.isMatch('abc', 'a.c')
    assert soln.isMatch('abc', 'ab.')
    # equal length, no stars, not dots, nonmatch
    assert not soln.isMatch('abc', 'dbc')
    assert not soln.isMatch('abc', 'adc')
    assert not soln.isMatch('abc', 'abd')
    # equal length, no stars, dots, nonmatch
    assert not soln.isMatch('abc', 'db.')
    assert not soln.isMatch('abc', 'd.c')
    assert not soln.isMatch('abc', 'ad.')
    assert not soln.isMatch('abc', '.dc')
    assert not soln.isMatch('abc', 'a.d')
    assert not soln.isMatch('abc', '.bd')

    # equal length, one star at end, no dots, match
    assert soln.isMatch('abc', 'abc*')
    # equal length, one star at end, dots, match
    assert soln.isMatch('abc', '.bc*')
    assert soln.isMatch('abc', 'a.c*')
    assert soln.isMatch('abc', 'ab.*')
    # equal length, one star at end, no dots, nonmatch
    assert not soln.isMatch('abc', 'abd*')
    # equal length, one star at end, dots, nonmatch
    assert not soln.isMatch('abc', '.ef*')
    assert not soln.isMatch('abc', 'd.f*')
    assert not soln.isMatch('abc', 'de.*')

    # unequal length, one star at end, no dots, nonmatch
    assert not soln.isMatch('abc', 'ab*')
    assert not soln.isMatch('def', 'de*')
    assert not soln.isMatch('ghi', 'gh*')
    # unequal length, one star at end, dots, nonmatch
    assert not soln.isMatch('abc', 'd.*')
    assert not soln.isMatch('def', '.e*')

    # star in middle and at end, match
    assert soln.isMatch('abcdef', 'abc*def*')
    assert soln.isMatch('abcde', 'abc*def*')
    assert soln.isMatch('abdef', 'abc*def*')
    assert soln.isMatch('abde', 'abc*def*')

    # some leetcode test cases
    assert not soln.isMatch('aaa', 'aaaa')
    assert not soln.isMatch('aaa', 'aa.a')
    assert not soln.isMatch('a', 'ab*a')
    assert soln.isMatch('ab', '.*..c*')
    assert not soln.isMatch('aaaaaaaaaaaaab', 'a*a*a*a*a*a*a*a*a*a*c')


if __name__ == '__main__':
    test_get_next_p_token()
    test_is_match()
