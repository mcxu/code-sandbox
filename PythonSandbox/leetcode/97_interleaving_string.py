class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        print(f"s1:{s1}, s2:{s2}, s3:{s3}")

        if not s1 and not s2:
            if s3:
                return False
            return True
        
        if s1+s2 == s3:
            return True
        
        if not s2 and s1 != s3:
            return False
        elif not s1 and s2 != s3:
            return False

        if len(s1) + len(s2) != len(s3):
            return False

        memo = [[0 for _ in range(len(s1))] for _ in range(len(s2))]

        print("initial memo")
        for row in memo:
            print(row)

        # if not memo:
        #     return False

        for r in range(len(memo)): # along s2 (rows)
            for c in range(len(memo[0])): # along s1 (cols)
                print(f"--- r:{r}, c:{c}")

                # if c > len(s3)-1 or r > len(s3)-1:
                #     return False

                #print(f"s1[c]:{s1[c]}, s2[r]:{s2[r]}")

                """
                abaa
                   a  a
                a [1, 1]
                b [0, 0]

                r=1, c=0
                s1[0] s3[0]
                """

                if r==c==0:
                    memo[r][c] = 1 # if both str empty, then output should be true
                elif r==0 and c>0 and s2[c-1]==s3[c-1] and memo[r][c-1]==1: 
                    #print(f"elif reached: s1[c]:{s1[c]}, s2[r]:{s2[r]}")
                    memo[r][c] = memo[r][c-1] # 0, 1
                    print("A")
                elif r>0 and c==0 and s1[r-1]==s3[r-1] and memo[r-1][c]==1:
                    memo[r][c] = memo[r-1][c]
                    print("B")
                elif r!=0 and c!=0 and s1[r-1]==s3[r+c-1] and memo[r-1][c]==1:
                    memo[r][c] = memo[r-1][c]
                    print("C")
                elif r!=0 and c!=0 and s2[c-1]==s3[r+c-1] and memo[r][c-1]==1:
                    memo[r][c] = memo[r][c-1]
                    print("D")
                else:
                    memo[r][c] = 0
                    print("E")

                for row in memo:
                    print(row)

        # print("memo after for loop")
        # for row in memo:
        #     print(row)

        return memo[-1][-1] == 1
    
    def test1(self):
        s1 = "aabcc"
        s2 = "dbbca"
        s3 = "aadbbcbcac"
        res = self.isInterleave(s1, s2, s3)
        # expected True
        print("res: ", res)
    
    def test2(self):
        s1 = "aabcc"
        s2 = "dbbca"
        s3 = "aadbbbaccc"
        res = self.isInterleave(s1, s2, s3)
        # expected False
        print("res: ", res)
    
    def test3(self):
        s1 = ""
        s2 = ""
        s3 = ""
        res = self.isInterleave(s1, s2, s3)
        # expected True
        print("res: ", res)

    def test4(self):
        s1 = ""
        s2 = ""
        s3 = "a"
        res = self.isInterleave(s1, s2, s3)
        # expected False
        print("res: ", res)
    
    def test5(self):
        s1 = ""
        s2 = "a"
        s3 = "a"
        res = self.isInterleave(s1, s2, s3)
        # expected True
        print("res: ", res)

    def test6(self):
        s1 = "a"
        s2 = ""
        s3 = "c"
        res = self.isInterleave(s1, s2, s3)
        # expected False
        print("res: ", res)

    def test7(self):
        s1 = "a"
        s2 = "b"
        s3 = "a"
        res = self.isInterleave(s1, s2, s3)
        # expected False
        print("res: ", res)
    
    def test8(self):
        s1 = "db"
        s2 = "b"
        s3 = "cbb"
        res = self.isInterleave(s1, s2, s3)
        # expected False
        print("res: ", res)
    
    def test9(self): # Fails (TODO)
        s1 = "aa"
        s2 = "ab"
        s3 = "abaa"
        res = self.isInterleave(s1, s2, s3)
        # expected True
        print("res: ", res)

s = Solution()
# s.test1()
# s.test2()
# s.test3()
# s.test4()
# s.test5()
# s.test6()
# s.test7()
# s.test8()
s.test9()