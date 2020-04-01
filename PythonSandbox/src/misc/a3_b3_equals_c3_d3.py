'''
Find all combinations for a,b,c,d between 1 <= a,b,c,d <= 1000,
that satisfy a^3 + b^3 = c^3 + d^3
'''

class Prob:
    @staticmethod
    def eval(lo, hi):
        abMap = {} # maps: a^3 + b^3 : [a,b]
        for a in range(lo, hi+1):
            for b in range(lo, hi+1):
                leftSide = a**3 + b**3
                if leftSide not in abMap.keys():
                    abMap[leftSide] = [[a,b]]
                else:
                    abMap[leftSide].append([a,b])
                    
        out = []
        for c in range(lo, hi+1):
            for d in range(lo, hi+1):
                rightSide = c**3 + d**3
                if rightSide in abMap.keys():
                    for pair in abMap[rightSide]:
                        out.append(pair + [c,d])
        
        print("abMap:")
        print(abMap)
        print("out: ", out)
    
    @staticmethod
    def test1(alg): 
        lo = 1
        hi = 2
        Prob.eval(lo, hi)

alg = Prob.eval

Prob.test1(alg)       
                