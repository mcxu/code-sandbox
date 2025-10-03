class ValidAnagram:
    def isAnagram(self, s: str, t: str):
        return sorted(s) == sorted(t)
    
