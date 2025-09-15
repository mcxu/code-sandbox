'''
Given grid, and given starting coord (x,y).
Determine whether or not it is possible to travel from starting coordinate
to ending coordinate (x2,y2) if the only move types are possible:
1. (x,y) -> (x+y,y)
2. (x,y) -> (x,y+x)
'''
import unittest
class GridTravel(unittest.TestCase):
    def isTravelPossible(self, startCoord, endCoord):
        if startCoord[0] > endCoord[0] or startCoord[1] > endCoord[1]:
            return False
        
        if startCoord == endCoord:
            return True
        
        move1 = self.isTravelPossible((startCoord[0]+startCoord[1],startCoord[1]), endCoord)
        move2 = self.isTravelPossible((startCoord[0],startCoord[1]+startCoord[0]), endCoord)
        return move1 or move2
    
    def test1(self):
        startCoord = (1,1)
        endCoord = (3,5)
        res = self.isTravelPossible(startCoord, endCoord)
        print("res: ", res)

unittest.main()