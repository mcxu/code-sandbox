"""
https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/description/ 
"""
from typing import List

class Solution:
    """ Notes:
    let n ~ len(cards)
    Time complexity: O(n), while loop iterates through all of cards array
    Space complexity: O(n), worse case is that there are no matching cards; dict must store n cards
    """
    def minimumCardPickup(self, cards: List[int]) -> int:
        seenCards = {}

        i = 0
        j = 0

        minConsec = float('inf')

        while j < len(cards):
            card = cards[j]
            #print(f"i:{i}, j:{j}, card:{card}, minConsec:{minConsec}, seenCards:{seenCards}")
            if card not in seenCards:
                seenCards[card] = j
                #print("added card")
                j += 1
            else:
                minConsec = min(minConsec, j - seenCards[card] + 1)
                seenCards.pop(card)
                #print("removed card")
                i += 1
        
        return minConsec if minConsec != float('inf') else -1