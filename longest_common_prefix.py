from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = ''
        idx = 0
        while True:
            char = None
            for str_ in strs:
                if idx < len(str_):
                    if char is None:
                        char = str_[idx]
                    if char != str_[idx]:
                        return lcp
                else:
                    return lcp
            lcp += char
            idx += 1
        return lcp
