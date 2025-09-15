# https://leetcode.com/problems/robot-bounded-in-circle/

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x = 0
        y = 0
        deltax = 0
        deltay = 1 # facing north
        for i,ch in enumerate(instructions):
            if ch=="G":
                y += deltay
                x += deltax
            elif ch=="L":
                if deltay==1:
                    deltay=0
                    deltax=-1
                elif deltay==-1:
                    deltay=0
                    deltax=1
                elif deltax==1:
                    deltax=0
                    deltay=1
                elif deltax==-1:
                    deltax=0
                    deltay=-1
            elif ch=="R":
                if deltay==1:
                    deltay=0
                    deltax=1
                elif deltay==-1:
                    deltay=0
                    deltax=-1
                elif deltax==1:
                    deltax=0
                    deltay=-1
                elif deltax==-1:
                    deltax=0
                    deltay=1
        if (x==0 and y==0) or not (deltax==0 and deltay==1):
            return True
        return False