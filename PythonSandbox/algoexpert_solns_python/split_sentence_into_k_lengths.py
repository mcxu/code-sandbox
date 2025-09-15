"""
Given a string (with words and spaces), split it into substrings that have at most k characters each.
Each substring must contain whole words only. Assume that k > the shortest word in the sentence.

Example: 
s = "I pet my cats and dogs"
k = 5
expected output: ['I pet', 'my', 'cats', 'and', 'dogs']

Example 2:
s = "the quick brown fox jumps over the lazy dog"
k = 15
expected output: ['the quick brown', 'fox jumps over', 'the lazy dog']
"""
class Solution:
    def splitSentence(self, s, k):
        output = []
        i = 0; j = 0
        sWords = s.split(" ")
        charCount = 0
        
        while j < len(sWords):
            currWord = sWords[j]
            charCount += len(currWord) + 1
            if (charCount - 1) > k:
                currSent = "".join(sWords[q] + " " for q in range(i, j))
                output.append(currSent[:-1])
                charCount = 0
                i = j
            else:
                j += 1

        output.append("".join(sWords[q] + " " for q in range(i, len(sWords)))[:-1])
        return output

    def test(self):
        #s = "I pet my cats and dogs"; k = 5
        s = "the quick brown fox jumps over the lazy dog"; k = 15
        result = self.splitSentence(s, k)
        print("result: ", result)
    
s = Solution()
s.test()
