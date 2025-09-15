class MaxOf3Nums:
    def maxOf3Nums(self, a, b, c):
        m = a

        if b > m:
            m = b
        
        if c > m:
            m = c
        
        return m
    
    def test(self):
        cases = [
            dict(a=10, b=14, c=12, output=14),
            dict(a=22, b=33, c=11, output=33),
            dict(a=2, b=4, c=3, output=4),
            dict(a=56, b=90, c=67, output=90)
        ]

        for c in cases:
            res = self.maxOf3Nums(c["a"], c["b"], c["c"])
            print("case: ", c)
            print("res: ", res)
            assert res == c["output"]

sol = MaxOf3Nums()
sol.test()
