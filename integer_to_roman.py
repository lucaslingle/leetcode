class Solution:
    def intToRoman(self, num: int) -> str:
        assert 1 <= num <= 3999

        roman = ''
        thousands_coef = num // 1000
        if thousands_coef == 0:
            pass
        elif thousands_coef == 1:
            roman += 'M'
        elif thousands_coef == 2:
            roman += 'MM'
        elif thousands_coef == 3:
            roman += 'MMM'
        else:
            raise NotImplementedError

        num = num - thousands_coef * 1000
        hundreds_coef = num // 100
        if hundreds_coef == 0:
            pass
        elif hundreds_coef == 1:
            roman += 'C'
        elif hundreds_coef == 2:
            roman += 'CC'
        elif hundreds_coef == 3:
            roman += 'CCC'
        elif hundreds_coef == 4:
            roman += 'CD'
        elif hundreds_coef == 5:
            roman += 'D'
        elif hundreds_coef == 6:
            roman += 'DC'
        elif hundreds_coef == 7:
            roman += 'DCC'
        elif hundreds_coef == 8:
            roman += 'DCCC'
        elif hundreds_coef == 9:
            roman += 'CM'
        else:
            raise NotImplementedError

        num = num - hundreds_coef * 100
        tens_coef = num // 10
        if tens_coef == 0:
            pass
        elif tens_coef == 1:
            roman += 'X'
        elif tens_coef == 2:
            roman += 'XX'
        elif tens_coef == 3:
            roman += 'XXX'
        elif tens_coef == 4:
            roman += 'XL'
        elif tens_coef == 5:
            roman += 'L'
        elif tens_coef == 6:
            roman += 'LX'
        elif tens_coef == 7:
            roman += 'LXX'
        elif tens_coef == 8:
            roman += 'LXXX'
        elif tens_coef == 9:
            roman += 'XC'
        else:
            raise NotImplementedError

        num = num - tens_coef * 10
        ones_coef = num
        if ones_coef == 0:
            pass
        elif ones_coef == 1:
            roman += 'I'
        elif ones_coef == 2:
            roman += 'II'
        elif ones_coef == 3:
            roman += 'III'
        elif ones_coef == 4:
            roman += 'IV'
        elif ones_coef == 5:
            roman += 'V'
        elif ones_coef == 6:
            roman += 'VI'
        elif ones_coef == 7:
            roman += 'VII'
        elif ones_coef == 8:
            roman += 'VIII'
        elif ones_coef == 9:
            roman += 'IX'
        else:
            raise NotImplementedError

        return roman
