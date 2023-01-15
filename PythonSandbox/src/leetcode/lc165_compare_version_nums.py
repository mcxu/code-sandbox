# https://leetcode.com/problems/compare-version-numbers/

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1split = version1.split(".")
        v2split = version2.split(".")
        minLen = min(len(v1split), len(v2split))
        
        i=0
        while i < minLen:
            n1 = int(v1split[i])
            n2 = int(v2split[i])
            if n1 > n2:
                return 1
            elif n1 < n2:
                return -1
            i += 1
            
        if len(v1split) > len(v2split):
            while i < len(v1split):
                if int(v1split[i])!=0:
                    return 1
                i += 1
        elif len(v1split) < len(v2split):
            while i < len(v2split):
                if int(v2split[i])!=0:
                    return -1
                i += 1
        return 0