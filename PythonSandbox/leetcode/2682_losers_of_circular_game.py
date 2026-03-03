"""
https://leetcode.com/problems/find-the-losers-of-the-circular-game/
"""
from typing import List

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:

        currFriend = 0
        # print("currFriend start: ", currFriend)
        
        freqMap = {0: 1}
        i = 1
        
        runGame = True
        while runGame:
            
            currFriend = (currFriend + (i*k)) % n
            # print("currFriend: ", currFriend)
            
            if currFriend in freqMap.keys():
                freqMap[currFriend] += 1
            else:
                freqMap[currFriend] = 1
            
            if freqMap[currFriend] == 2:
                runGame = False
            
            i += 1
        
        # print("freqMap: ", freqMap)
        
        nSet = set([i for i in range(1, n+1)])
        includedFriends = set([k+1 for k in freqMap.keys()])
        output = []
        for friend in nSet:
            if friend not in includedFriends:
                output.append(friend)
        
        return output
        
        