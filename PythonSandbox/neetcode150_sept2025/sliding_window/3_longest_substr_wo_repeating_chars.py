class LongestSubstringWithoutRepeatingCharacters:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        seenChars = set()

        i = 0; j = 0
        while j < len(s):
            iChar = s[i]
            jChar = s[j]
            if jChar in seenChars:
                seenChars.remove(iChar)
                i += 1
            else:
                seenChars.add(jChar)
                longest = max(longest, j - i + 1)
                j += 1
        
        return longest 

    def test_1(self):
        testCases = [
            ["abcabcbb", 3],
            # ["bbbbb", 1],
            # ["pwwkew", 3], # "wke"
            # ["dvdf", 3]
        ]

        for tc in testCases:
            s = tc[0]
            expected = tc[1]
            
            output = self.lengthOfLongestSubstring(s)
            print("output: ", output)
            assert output == expected

if __name__ == "__main__":
    cl = LongestSubstringWithoutRepeatingCharacters()
    cl.test_1()