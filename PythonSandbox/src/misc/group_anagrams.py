'''
Group Anagrams

Function that takes in list of strings, and returns list of groups (lists) of anagrams.
Sample input: ["yo", "act", "flop", "tac", "cat", "oy", "olfp"]
Sample output: [["yo", "oy"], ["flop", "olfp"], ["act", "tac", "cat"]]
'''

class Prob:
    @staticmethod
    def groupAnagrams(words):
        countMapList = [] # store maps of character counts
        
        # populate countMapList
        for word in words:
            countMap = {}
            for char in word:
                if char in countMap.keys():
                    countMap[char] += 1
                else:
                    countMap[char] = 1
            countMapList.append(countMap)
        
        anMap = {} # store lists of anagrams with format word:[anagram,...]
        # check for anagrams using countMapList
        i = 0
        while i < len(words):
            anMap[words[i]] = []
            j = i+1
            while j < len(words):
                if countMapList[j] == countMapList[i]:
                    anMap[words[i]].append(words[j])
                    words.pop(j); countMapList.pop(j)
                    j -= 1
                j += 1
            i += 1
        
        # return required format
        output = []
        for key in anMap.keys():
            output.append([key] + anMap[key])
        return output
            

    @staticmethod
    def test1():
        words = ["yo", "act", "flop", "tac", "cat", "oy", "olfp"]
        correctOut =  [["yo", "oy"], ["flop", "olfp"], ["act", "tac", "cat"]]
        output = Prob.groupAnagrams(words)
        print("test1: output: ", output)

Prob.test1()