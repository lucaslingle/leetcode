from typing import Tuple
import string


class Solution:
    def get_next_p_token(self, p: str) -> Tuple[str, str]:
        if len(p) > 1 and p[1] == '*':
            return p[0:2], p[2:]
        else:
            return p[0], p[1:]

    def simplify(self, p: str) -> str:
        p_tokens = []
        while len(p) > 0:
            p_token, p = self.get_next_p_token(p)
            if (
                len(p_tokens) == 0 or
                len(p_token) == 1 or
                (len(p_token) == 2 and p_tokens[-1] != p_token)
            ):
                p_tokens.append(p_token)
        return ''.join(p_tokens)

    def stars_only(self, p: str) -> bool:
        while len(p) > 0:
            p_token, p = self.get_next_p_token(p)
            if len(p_token) == 1:
                return False
        return True

    def _isMatch(self, s: str, p: str) -> bool:
        assert 1 <= len(s) <= 20
        assert 1 <= len(p) <= 30
        assert set(s) <= set(list(string.ascii_lowercase))
        assert set(p) <= set(list(string.ascii_lowercase)).union({'.', '*'})

        p_token, p_tail = self.get_next_p_token(p)
        if len(p_token) == 1:  # non-star tokens -- match literals or anything.
            if p_token == '.' or p_token == s[0]:
                if len(s[1:]) == 0 and self.stars_only(p_tail):
                    return True
                elif len(s[1:]) == 0 and not self.stars_only(p_tail):
                    return False
                elif len(s[1:]) != 0 and len(p_tail) == 0:
                    return False
                else:
                    return self._isMatch(s=s[1:], p=p_tail)
            else:
                return False
        else:  # something star token -- match zero or more repeats.
            while len(s) > 0:
                if len(p_tail) > 0 and self._isMatch(s=s, p=p_tail):
                    return True
                elif p_token[0] == '.' or p_token[0] == s[0]:
                    s = s[1:]
                else:
                    break
            if len(s) == 0 and self.stars_only(p_tail):
                return True
            elif len(s) == 0 and not self.stars_only(p_tail):
                return False
            elif len(s) != 0 and len(p_tail) == 0:
                return False
            else:
                return self._isMatch(s=s, p=p_tail)

    def isMatch(self, s: str, p: str) -> bool:
        return self._isMatch(s=s, p=self.simplify(p))
