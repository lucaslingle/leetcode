class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_palindrome_so_far = ''
        T = len(s)
        if T == 1:
            return s
        for i in range(0, T-1):
            for j in range(0, min(T-(i+1), i+1)):
                if s[i-j] == s[i+1+j]:
                    candidate = s[i-j:(i+2)+j]   # s[i], s[i+1] and possibly more
                    if len(longest_palindrome_so_far) < len(candidate):
                        longest_palindrome_so_far = candidate
                else:
                    break
            for j in range(0, min(T-i, i+1)):
                if s[i-j] == s[i+j]:
                    candidate = s[i-j:(i+1)+j]   # s[i] and possibly more
                    if len(longest_palindrome_so_far) < len(candidate):
                        longest_palindrome_so_far = candidate
                else:
                    break
        return longest_palindrome_so_far