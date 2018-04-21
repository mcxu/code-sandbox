'''
Created on Aug 26, 2015

@author: Michael
'''

class RepeatSandbox(object):

    def __init__(self):
        '''
        Constructor
        '''
        self.freqDict = {}
        
    def findFirstNonRepeatedChar(self, input_str):
        for char in input_str:
            dictValue = self.freqDict.get(char)
            print("char", char)
            if(dictValue == None):
                self.freqDict[char] = 1
            else:
                self.freqDict[char] = dictValue + 1
        print("dict:", self.freqDict)  # print out the freqDict  
        
        # now go throug freqDict to see if there are any 1's
        for char in input_str:
            dictValue = self.freqDict[char]
            if(dictValue == 1):
                return char
            
        return None
    
    
def main():
    rs = RepeatSandbox()
    print(rs.findFirstNonRepeatedChar("adsfaydsf"))

if __name__ == "__main__":
    main()
        