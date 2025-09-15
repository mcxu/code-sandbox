'''
Turn word1 into word2 by replacing 1 char at a time.
Each intermediate transformed string must also be a word.
Assume you have a dictionary of words.
Assume that all words during transformation are same length.

Example:
HEAD -> HEAL -> TEAL -> TELL -> TALL -> TAIL
output: list of all intermediate transformations including begin and end words.
'''

class TransformWord:
    def __init__(self, dictionary=None):
        if dictionary is not None:
            self.dicitonary = dictionary
        else:
            #self.dictionary = set(["HEAD", "HEAL", "TEAL", "TELL", "TALL", "TAIL"])
            self.dictionary = set(["HEAL", "HEAD", "TEAL", "TALL", "TAIL", "TELL"])

    def transformWord(self, word1, word2):
        out = [word1]
        currWord = word1
        while currWord != word2:
            nextWord = self.findNextWord(currWord, out)
            if nextWord != None:
                out.append(nextWord)
            else:
                return None
            currWord = nextWord
        return out
    
    # find word that has 1 char diff, and is a part of the dictionary.
    def findNextWord(self, word, out):
        for dWord in self.dictionary:
            if self.numDiffs(word, dWord) == 1 and dWord not in out:
                return dWord
        return None

    # find number of diff chars between 2 words.
    def numDiffs(self, word1, word2):
        diffs = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                diffs += 1
        return diffs

    def test1(self):
        word1 = "HEAD"
        word2 = "TAIL"
        res = self.transformWord(word1, word2)
        print("test1 res: ", res)

prob = TransformWord()
prob.test1()