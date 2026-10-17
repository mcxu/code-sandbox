class LCS:
    def longestCommonSubsequence(self, text1: str, text2: str) -> str:
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        for y in range(1, len(text1) + 1):
            for x in range(1, len(text2) + 1):
                if text1[y-1] == text2[x-1]:
                    dp[y][x] = dp[y-1][x-1] + 1
                else:
                    dp[y][x] = max(dp[y-1][x], dp[y][x-1])
        return dp[len(text1)][len(text2)]
    
    def test1(self):
        text1 = "abcde"
        text2 = "ace"
        print(self.longestCommonSubsequence(text1, text2))

if __name__ == "__main__":
    lcs = LCS()
    lcs.test1()