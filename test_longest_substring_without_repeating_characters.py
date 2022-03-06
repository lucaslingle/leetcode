from longest_substring_without_repeating_characters import Solution


def test_soln():
    soln = Solution()
    assert soln.lengthOfLongestSubstring(s="abcabcbb") == 3
    assert soln.lengthOfLongestSubstring(s=" ") == 1
    assert soln.lengthOfLongestSubstring(s="aardvark") == 5
