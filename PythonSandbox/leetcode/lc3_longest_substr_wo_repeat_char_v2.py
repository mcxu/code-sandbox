class Solution:
    def lengthOfLongestSubstring(self, s: str, option: int = 1) -> int:
        longestLen = 0
        seenChars = set()
        # longestSubstr = ""

        i, j = 0, 0
        while j < len(s):
            ival, jval = s[i], s[j]

            if jval not in seenChars:
                seenChars.add(jval)
                j += 1
                longestLen = max(longestLen, j-i)

                # Do this if you want to save the actual substring
                # currLen = j-i
                # if currLen > longestLen:
                #     longestLen = currLen
                #     longestSubstr = s[i:j]
            else:
                seenChars.remove(ival)
                i += 1
        
        # print("longestSubstr: ", longestSubstr)
        return longestLen