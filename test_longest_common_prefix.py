from longest_common_prefix import Solution


def test_soln():
    soln = Solution()
    assert soln.longestCommonPrefix(strs=["flower","flow","flight"]) == 'fl'
    assert soln.longestCommonPrefix(strs=["dog","racecar","car"]) == ''
    assert soln.longestCommonPrefix(strs=["doge", "dodge", "doog"]) == 'do'
    assert soln.longestCommonPrefix(strs=["", "dodge", "doog"]) == ''
    assert soln.longestCommonPrefix(strs=["d", "dodge", "doog"]) == 'd'
