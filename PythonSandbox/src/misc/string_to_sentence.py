'''
Word Break Problem ?
Given a string of words, and a dictionary of words.
Turn the string into a sentence and return it. 
If this cannot be done, then return None.

Example:
s = "hellothere"
dictionary = {"hello", "there}
output: "hello there"

Example:
s = "hellothere"
dictionary = {"hello", "the"}
output: None (Since "there" is a not a word in the dictionary, the whole sentence cannot be converted.)
'''

class StringToSentence:
    '''
    Let n = len(s)
        d = len of longest word in dictionary.
    Time: O(n^n): Since for loop calls stringToSentence n times recursively.
    Space: O(n*d): For some substring that exists in dictionary, d means there is a new level of recursion.
        starting from the (last+1)th char from that substring till the end of s.
    Not sure if this analysis is correct.
    '''
    def stringToSentence(self, s, dictionary):
        if not s or s in dictionary:
            return s
        for i in range(len(s)):
            substr = s[:i+1]
            if substr in dictionary:
                nextWord = self.stringToSentence(s[i+1:], dictionary)
                if nextWord:
                    return substr + " " + nextWord
        # for cases where there are no substr in dictionary
        return None

    def test1(self):
        s = "hellothere"
        #dictionary = set(["hello", "them"])
        #dictionary = set(["hello", "there"])
        dictionary = set(["hello", "the", "there"])
        res = self.stringToSentence(s, dictionary)
        print("res: ", res)

    def test2(self):
        s = "hellothereafter"
        #dictionary = set(["hello", "them"])
        #dictionary = set(["hello", "there"])
        dictionary = set(["hello", "there", "the", "after"])
        res = self.stringToSentence(s, dictionary)
        print("res: ", res)

    def test3(self):
        s = "hellothereeveraftertomorrow"
        #dictionary = set(["hello", "them"])
        #dictionary = set(["hello", "there"])
        dictionary = set(["hello", "there", "aft", "ever", "morrow", "to", "the", "after"])
        res = self.stringToSentence(s, dictionary)
        print("res: ", res)

prob = StringToSentence()
prob.test1()
prob.test2()
prob.test3()