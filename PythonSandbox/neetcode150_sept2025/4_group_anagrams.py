from typing import List

class GroupAnagrams:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strMap = {}
        for s in strs:
            sSorted = "".join(sorted(s))

            if sSorted in strMap:
                strMap[sSorted].append(s)
            else:
                strMap[sSorted] = [s]
        
        # output list
        output = []
        for key in strMap:
            anagramList = strMap[key]
            output.append(anagramList)

        return output