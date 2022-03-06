class Solution:
    def myAtoi(self, s: str) -> int:
        accepting_whitespace = True
        accepting_signs = True
        accepting_digits = True
        whitespace = []
        signs = []
        digits = []
        for char in list(s):
            if char in [' ', '\t', '\n']:
                if accepting_whitespace:
                    whitespace.append(char)
                    accepting_whitespace = True
                    accepting_signs = True
                    accepting_digits = True
                else:
                    break
            elif char in ['-', '+']:
                if accepting_signs:
                    signs.append(char)
                    accepting_whitespace = False
                    accepting_signs = False
                    accepting_digits = True
                else:
                    break
            elif char in set(list("123456789")) or (char == '0' and len(digits) > 0):
                if accepting_digits:
                    digits.append(char)
                    accepting_whitespace = False
                    accepting_signs = False
                    accepting_digits = True
                else:
                    break
            elif char == '0':
                accepting_whitespace = False
                accepting_signs = False
                accepting_digits = True
            else:
                break
        result = 0
        for i, digit in enumerate(reversed(digits)):
            result += (10 ** i) * int(digit)
        if len(signs) > 0:
            if signs[0] == '-':
                result = -result
        if result < -2147483648:  # (2 ** 31)
            return -2147483648
        if result > 2147483647:  # (2 ** 31) - 1
            return 2147483647
        return result
