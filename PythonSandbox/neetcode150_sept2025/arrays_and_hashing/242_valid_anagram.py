from collections import Counter

class ValidAnagram:
    # def isAnagram(self, s: str, t: str):
    #     return sorted(s) == sorted(t)
    
    # using hash table
    # TC: O(n) where n = len(max(s,t))
    # SC: O(n)
    def isAnagram(self, s: str, t: str):
        return Counter(s) == Counter(t)

