class RomanNumerals:
    @staticmethod
    #digit to roman
    def to_roman(val : int) -> str:
        mapp=[  (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
        result=[]
        for value,symbol in mapp:
            while val>=value:
                result.append(symbol)
                val-=value
        return "".join(result)
            
#roman to digit
    @staticmethod
    def from_roman(roman_num : str) -> int:
        mapp={"I": 1, "V": 5, "X": 10, "L": 50,
        "C": 100, "D": 500, "M": 1000}
        total=0
        for i in range(len(roman_num)-1):
            if mapp[roman_num[i]]<mapp[roman_num[i+1]]:
                total-=mapp[roman_num[i]]
            else:
                total+=mapp[roman_num[i]]
        total+=mapp[roman_num[-1]]
        return total