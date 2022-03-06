from longest_palindromic_substring import Solution


def test_soln():
    soln = Solution()
    assert soln.longestPalindrome(s='babad') in ['bab', 'aba']
    assert soln.longestPalindrome(s='abcdeedcba') in ['abcdeedcba']
    assert soln.longestPalindrome(s='a') in ['a']
    assert soln.longestPalindrome(s='') in ['']
    assert soln.longestPalindrome(s='a' * 1000) in ['a' * 1000]
    assert soln.longestPalindrome(s='a' * 1000 + 'b') in ['a' * 1000]
    assert soln.longestPalindrome(s='cbbd') in ['bb']
    assert soln.longestPalindrome(s='ccc') in ['ccc']
