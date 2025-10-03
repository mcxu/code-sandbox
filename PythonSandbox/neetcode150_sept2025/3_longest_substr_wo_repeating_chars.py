class LongestSubstringWithoutRepeatingCharacters:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestSoFar = 0
        seenChars = set()
        
        i = 0
        j = 0
        while j < len(s):
            iChar, jChar = s[i], s[j]
            
            print(f"===== j={j} ch: ", jChar, "\nseenChars before: ", seenChars)
            if jChar in seenChars:
                seenChars.remove(iChar)
                print("seenChars after remove: ", seenChars)
                i += 1
                print("i is now: ", i)
            else:
                seenChars.add(jChar)
                print("seenChars after: ", seenChars)

                longestSoFar = max(longestSoFar, j - i + 1)
                print("longestSoFar: ", longestSoFar)
                j += 1

        return longestSoFar

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