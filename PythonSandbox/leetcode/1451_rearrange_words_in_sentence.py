'''
https://leetcode.com/problems/rearrange-words-in-a-sentence/
Given a sentence text (A sentence is a string of space-separated words) in the following format:
First letter is in upper case. Each word in text are separated by a single space.

Your task is to rearrange the words in text such that all words are rearranged in an increasing order of their lengths. 
If two words have the same length, arrange them in their original order.
'''

class Solution:
    def arrangeWords(self, text: str) -> str:
        textSplit = text.split(" ")
        aux = []
        for i,word in enumerate(textSplit):
            aux.append((word,len(word)))
        aux = sorted(aux, key=lambda x: x[1])

        newText = ""
        for j,tup in enumerate(aux):
            wrd = tup[0]
            if j == 0:
                wrd = wrd[0].upper() + wrd[1:]
            else:
                wrd = wrd.lower()
            newText += (wrd + " ")
        
        return newText[:-1]
    
    def test1(self):
        text = "Leetcode is cool"
        #text = "To be or not to be"
        res=self.arrangeWords(text)
        print("res: ", res)

prob = Solution()
prob.test1()
