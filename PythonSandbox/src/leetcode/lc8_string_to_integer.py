"""
https://leetcode.com/problems/string-to-integer-atoi/
"""

class LC8_StrToInt():
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        s = s.strip()

        MIN = -(2**31)
        MAX = (2**31)-1

        sRev = ""
        i = 0
        sign = 1

        if s[0] == "-":
            i = 1
            sign = -1
        elif s[0] == "+":
            i = 1
            sign = 1

        while i < len(s) and s[i].isnumeric():
            sRev = s[i] + sRev
            i += 1

        place = 1
        tot = 0
        for c in sRev:

            if sign == -1:
                tot -= int(c) * place
            else:
                tot += int(c) * place

            if tot <= MIN:
                return MIN
            elif tot >= MAX:
                return MAX

            place *= 10
        
        return tot

    def test1(self):
        #s = "42"
        # s = "4193 with words"
        # s = "  -42"
        s = "-3"
        res = self.myAtoi(s)
        print("res: ", res)

    def test2(self):
        s = "-91283472332"
        res = self.myAtoi(s)
        print("res: ", res)
        assert res == -2147483648

    def test2(self):
        s = "+1"
        res = self.myAtoi(s)
        print("res: ", res)
        assert res == 1

sol = LC8_StrToInt()
# sol.test1()
sol.test2()