'''
Given number of rows, print a diamond pattern.
n = 3
  *
* * *
  *

n = 4
  *
* * *
* * *
  *
'''

class Prob:
    @staticmethod
    def printDiamond(n):
        aux = [" "] * (n+1)
        medInd = int(n/2) # median index
        aux[medInd] = "*"
        
        lim = int(n/2)
        if n % 2 != 0:
            lim += 1
        
        for i in range(lim):
            aux[medInd - i] = "*"
            aux[medInd + i] = "*"
            rowStr = " ".join(aux)
            print(rowStr)
        
        for i in range(int(n/2), -1, -1):
            aux[medInd - i] = " "
            aux[medInd + i] = " "
            rowStr = " ".join(aux)
            print(rowStr)
            
    
    @staticmethod
    def test1():
        n = 10
        Prob.printDiamond(n)

Prob.test1()

