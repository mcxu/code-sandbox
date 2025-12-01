import collections

class PermutationInString:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1FreqMap = collections.Counter(s1)
        
        if len(s1) > len(s2):
            return False
        
        span = s2[0:len(s1)]
        # print("first span: ", span)
        startChar, endChar = span[0], span[-1]
        s2FreqMap = collections.Counter(span)
        # print("s2FreqMap: ", s2FreqMap)
        if s1FreqMap == s2FreqMap:
            return True

        for i in range(1, len(s2) - len(s1) + 1):
            span = s2[i:i + len(s1)]
            # print("---- span: ", span)
            # print("startChar: ", startChar, "    endChar: ", endChar)
            # update the s2FreqMap to reflect the updated span
            s2FreqMap[startChar] -= 1
            if s2FreqMap[startChar] == 0:
                s2FreqMap.pop(startChar)

            startChar, endChar = span[0], span[-1]
            s2FreqMap.update(endChar)

            # print("s2FreqMap: ", s2FreqMap)
            if s1FreqMap == s2FreqMap:
                return True
        
        return False
            

    def test1(self): # expected: True
        s1 = "ab"
        s2 = "eidbaooo"
        print(self.checkInclusion(s1, s2))

    def test2(self): # expected: False
        s1 = "ab"
        s2 = "eidboaoo"
        print(self.checkInclusion(s1, s2))
    
    def test3(self): # expected: True
        s1 = "adc"
        s2 = "dcda"
        print(self.checkInclusion(s1, s2))

    def test4(self): # expected: False
        s1 = "hello"
        s2 = "eidboaooooolleoooleh"
        print(self.checkInclusion(s1, s2))

    def test5(self): # expected: True
        s1 = "a"
        s2 = "ab"
        print(self.checkInclusion(s1, s2))

if __name__ == "__main__":
    pt = PermutationInString()
    # pt.test1()
    # pt.test2()
    # pt.test3()
    # pt.test4()
    pt.test5()
