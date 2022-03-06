class Solution:
    def mod_to_row_id(self, mod, numRows):
        cycle_len = 2 * (numRows - 1)
        if mod <= cycle_len // 2:
            return mod
        else:
            return cycle_len - mod

    def convert(self, s: str, numRows: int) -> str:
        if len(s) <= 1 or numRows == 1:
            return s
        cycle_len = 2 * (numRows - 1)
        rows = {i: [] for i in range(numRows)}  # instantiates each [] sep.
        for i in range(len(s)):
            rows[self.mod_to_row_id(i % cycle_len, numRows)].append(s[i])
        row_strings = []
        for j in range(numRows):
            row_strings.append(''.join(rows[j]))
        return ''.join(row_strings)
