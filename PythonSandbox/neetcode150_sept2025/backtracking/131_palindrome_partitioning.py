class Solution:
    def partition(self, s: str)-> list[list[str]]:
        results = []
        currPath = []
        self.dfs(s, 0, currPath, results)
        return results

    def dfs(self, s, partitionIdx, currPath, results):
        if partitionIdx == len(s):
            results.append(currPath[:])
            return
        
        for end in range(partitionIdx+1, len(s)+1):
            substr = s[partitionIdx: end]
            if self.isPalindrome(substr):
                currPath.append(substr)
                self.dfs(s, end, currPath, results)
                currPath.pop()
        return

    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        while i < j and s[i] == s[j]:
            i += 1
            j -= 1
        return j - i < 1
    
    def test_isPalindrome(self):
        # s = "aab"
        s = "a"
        s = "racecar"
        s = "racqtcar"
        s = ""
        ispal = self.isPalindrome(s)
        print(f"{ispal=}")
    
    def test1(self):
        s = "aab"
        expected = [["a","a","b"],["aa","b"]]
        result = self.partition(s)
        print("result: ", result)

if __name__ == "__main__":
    s = Solution()
    # s.test_isPalindrome()
    s.test1()