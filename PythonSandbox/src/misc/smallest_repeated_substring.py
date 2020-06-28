'''
Given a string s comprised of repeated substrings, return the repeated substring. 
If there is no repeating substring, return null.
If a string is not strictly comprised of repeated substrings, return null.
'''
class SRS:
    def smallestRepeatedSubstring(self, s):
        for i in range(len(s)):
            subFrom0 = s[:i+1]
            if subFrom0==s[i+1:i+1+len(subFrom0)]:
                j = i+1+len(subFrom0)
                while j < len(s):
                    aux = s[j:j+len(subFrom0)]
                    if aux != subFrom0:
                        return None
                    j += len(subFrom0)
                return subFrom0
        return None
    
    def test1(self):
        strings = [
            "abcabcabc",
            "abcabb",
            "lrbblrbb",
            "lrbblrbblr",
            "lrbbbbb",
            "abddab",
            "qwertyyyqwertyyyqwertyyyqwertyyy",
            "qwertyyyyqwertyyy"
        ]
        for i,s in enumerate(strings):
            print("--- TEST NO.: ", i)
            print("     test: ", s)
            res = self.smallestRepeatedSubstring(s)
            print("     result: ", res)

srs = SRS()
srs.test1()