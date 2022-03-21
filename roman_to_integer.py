class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        if s.startswith('M') and not s.startswith('MM'):
            num += 1000
            s = s[1:]
        elif s.startswith('MM') and not s.startswith('MMM'):
            num += 2000
            s = s[2:]
        elif s.startswith('MMM'):
            num += 3000
            s = s[3:]

        if s.startswith('D'):
            num += 500
            s = s[1:]

        if (
                s.startswith('C') and
                not s.startswith('CC') and
                not s.startswith('CD') and
                not s.startswith('CM')
        ):
            num += 100
            s = s[1:]
        elif s.startswith('CC') and not s.startswith('CCC'):
            num += 200
            s = s[2:]
        elif s.startswith('CCC'):
            num += 300
            s = s[3:]
        elif s.startswith('CD'):
            num += 400
            s = s[2:]
        elif s.startswith('CM'):
            num += 900
            s = s[2:]

        if s.startswith('L'):
            num += 50
            s = s[1:]

        if (
                s.startswith('X') and
                not s.startswith('XX') and
                not s.startswith('XL') and
                not s.startswith('XC')
        ):
            num += 10
            s = s[1:]
        elif s.startswith('XX') and not s.startswith('XXX'):
            num += 20
            s = s[2:]
        elif s.startswith('XXX'):
            num += 30
            s = s[3:]
        elif s.startswith('XL'):
            num += 40
            s = s[2:]
        elif s.startswith('XC'):
            num += 90
            s = s[2:]

        if s.startswith('V'):
            num += 5
            s = s[1:]

        if (
                s.startswith('I') and
                not s.startswith('II') and
                not s.startswith('IV') and
                not s.startswith('IX')
        ):
            num += 1
            s = s[1:]
        elif s.startswith('II') and not s.startswith('III'):
            num += 2
            s = s[2:]
        elif s.startswith('III'):
            num += 3
            s = s[3:]
        elif s.startswith('IV'):
            num += 4
            s = s[2:]
        elif s.startswith('IX'):
            num += 9
            s = s[2:]

        print(s)
        assert len(s) == 0
        return num


