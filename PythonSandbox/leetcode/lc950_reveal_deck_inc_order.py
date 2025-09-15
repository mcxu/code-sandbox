'''
https://leetcode.com/problems/reveal-cards-in-increasing-order/
'''
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck = sorted(deck)
        deckInds = [i for i in range(len(deck))]
        revealed = [None]*len(deck)
        
        while deckInds:
            di = deckInds.pop(0)
            revealed[di]=deck.pop(0)
            
            if deckInds:
                nxtInd = deckInds.pop(0)
                deckInds.append(nxtInd)

        return revealed