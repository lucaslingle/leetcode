class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substring_so_far = ''
        current_substring = ''
        for i in range(len(s)):
            current_substring += s[i]
            if len(set(current_substring)) != len(current_substring):
                current_substring = current_substring[1:]
            if len(current_substring) > len(longest_substring_so_far):
                longest_substring_so_far = current_substring
        return len(longest_substring_so_far)

"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substring_so_far = ''
        current_substring = ''
        for i in range(len(s)):
            # right concatenate a new character
            current_substring += s[i]
            if len(set(current_substring)) != len(current_substring):
                # chop left character off if new current_substring has repeats
                current_substring = current_substring[1:]
            if len(current_substring) > len(longest_substring_so_far):
                # this check doesn't ensure the substring has no repeats.
                # however, if it had any repeats,
                # a character would have gotten chopped off on line 10,
                # so there is no way the new string will be set as the
                # longest_substring_so_far.
                # by induction, if longest_substring_so_far is initially
                # a string with no duplicates, it will never be overwritten
                # with a string having duplicates.
                longest_substring_so_far = current_substring
        # we now prove that longest_substring_so_far will indeed be
        # the longest substring with no duplicates (call it s').
        # if there are multiple longest substrings of s with no duplicates,
        # s' refers to the first one.
        # suppose for argument by contradiction that s' is never assigned to
        # longest_substring_so_far.
        # then one of two things must have occurred.
        #    case 1: s' was never current_substring,
        #    case 2: len(s') <= len(longest_substring_so_far),
        #    consider the first case.
        #        current_substring will eventually have s'[-1]
        #        as its last character.
        #        then since we only slice current_substring on the left,
        #        we must have sliced off the character s'[0] at some point
        #        before or upon reaching s'[-1].
        #        however, since s' has no duplicates,
        #        the slicing condition is never triggered.
        #        thus, case 1 cannot occur.
        #    consider the second case.
        #        len(s') <= len(longest_substring_so_far), then there was some
        #        substring of s assigned to longest_substring_so_far with a
        #        length greater than or equal to len(s').
        #        however, we already know that longest_substring_so_far
        #        cannot be any string except one without a duplicate
        #        (see inductive argument earlier). therefore,
        #        longest_substring_so_far has no duplicates
        #        when the check len(s') > len(longest_substring_so_far) occurs.
        #        therefore if case 2 occurs and the check is failed,
        #        there must be a substring of s ending before s' with the same 
        #        or greater length than s' and with no duplicates.
        #        however, since s' was defined to be the first longest substring
        #        with no duplicates, there cannot be any such prior substring.
        #        contradiction.
        #   thus, we have shown neither case 1 nor case 2 can occur and so
        #   we have proven that s' will be assigned to longest_substring_so_far.
        #
        return len(longest_substring_so_far)
"""