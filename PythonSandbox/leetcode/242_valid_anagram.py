class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqMap = {}
        for _,c in enumerate(s):
            if c in freqMap.keys():
                freqMap[c] += 1
            else:
                freqMap[c] = 1
        
        for _,c in enumerate(t):
            if c in freqMap.keys():
                freqMap[c] -= 1
                if freqMap[c] == 0:
                    freqMap.pop(c)
            else:
                return False
        
        if freqMap:
            return False
        return True

class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = self.turnMap(s)
        tMap = self.turnMap(t)
        if sMap.keys()==tMap.keys():
            for k in tMap.keys():
                if tMap[k]!=sMap[k]:
                    return False
        else:
            return False
        return True
    
    def turnMap(self, s):
        sMap = {}
        for i,ch in enumerate(s):
            if ch in sMap.keys():
                sMap[ch] += 1
            else:
                sMap[ch] = 1
        return sMap