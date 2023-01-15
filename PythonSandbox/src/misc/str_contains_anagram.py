'''
Given string a and string b, if any substring
in string a contains an anagram of b, return the index in a where
the anagram begins. Otherwise, if a doesn't contain an
anagram of b, return -1.
Ex.
a = "racecar"
b = "ecc"
return True ("cec" is an anagram of "ecc")
'''
def strContainsAnagram(a, b):
    if len(a) < len(b):
        return False

    bMap = getFreqMap(b)

    for i in range(len(a)-len(b)+1):
        sub = a[i: i+len(b)]
        print("sub: ", sub)
        subMap = getFreqMap(sub)
        print("subMap: ", subMap)
        if subMap.keys()==bMap.keys():
            for k in subMap.keys():
                if subMap[k]!=bMap[k]:
                    continue
            return i
    return -1

def getFreqMap(s):
    freqMap = {}
    for i,ch in enumerate(s):
        if ch not in freqMap.keys():
            freqMap[ch] = 1
        else:
            freqMap[ch] += 1
    return freqMap

def test1():
    a = "racecar"
    b = "care"
    res = strContainsAnagram(a,b)
    print("res: ", res)
test1()