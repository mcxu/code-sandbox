'''
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
    Time: O(n^2), since there is a single while loop iterating through string s,
        but within this loop, the substr takes worst case O(n) time complexity.
        if substr in diction is just O(1) since dictionary is a set.
    Space: (Assuming we are not counting out variable to contribute to this).
        It is O(n) since the substr variable stores worst case all of s.
    '''
    def stringToSentence(self, s, dictionary):
        loInd=0
        hiInd=0
        out = ""
        while hiInd < len(s):
            substr = s[loInd:hiInd+1]
            if substr in dictionary:
                out += (substr + " ")
                hiInd+=1
                loInd=hiInd
            else:
                hiInd += 1
        
        if loInd >= len(s):
            return out[:-1]
        
        return None
    
    def test1(self):
        s = "hellothere"
        dictionary = set(["hello", "there"])
        res = self.stringToSentence(s, dictionary)
        print("res: ", res)

prob = StringToSentence()
prob.test1()