class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupMap = {}

        for s in strs:
            sSorted = "".join(sorted(s))
            
            if sSorted not in groupMap.keys():
                groupMap[sSorted] = [s]
            else:
                groupMap[sSorted].append(s)
        
        anagramGroups = list(map(lambda k: groupMap.get(k), groupMap.keys()))
        #anagramGroups = map(lambda item: item[1], groupMap.items()) # alternative way to write this
        return anagramGroups