from palindrome_number import Solution


def test_soln():
    soln = Solution()
    assert not soln.isPalindrome(-121)
    assert soln.isPalindrome(121)
    assert soln.isPalindrome(1331)
    assert soln.isPalindrome(0)
    assert soln.isPalindrome(1)
    assert soln.isPalindrome(2001002)
    assert not soln.isPalindrome(2020102)


if __name__ == '__main__':
    test_soln()