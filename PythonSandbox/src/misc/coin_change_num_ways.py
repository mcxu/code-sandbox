"""
Given array of pos ints representing denominations, and a single non-negative
int representing a target amount of money. Write function to return number
of ways to make change for that target amount.

Sample input: 6,[1,5]
Sample output: 2 (1x1 + 1x5 and 6x1)
"""

class Prob:
    
    """
    Complexity
    Time: O(n*denoms), because you need for loop for denoms, and for loop for n
    Space: O(n), because you need an array to store up to n values.
    """
    @staticmethod
    def numberOfWaysToMakeChange(n, denoms):
        # init array to keep track of ways to make change up to n
        waysForAmt = [0] * (n+1)
        waysForAmt[0] = 1 # because for n=0, there is only 1 way to make change, and that is with no coins.
        #print("waysForAmt: ", waysForAmt)
        
        for d in denoms:
            for i in range(n+1):
                #print("d: {}, i: {}".format(d, i))
                if i >= d:
                    waysForAmt[i] += waysForAmt[i-d]
            #print("waysForAmt: ", waysForAmt)
        
        # the last value will result in the total num of ways to make change
        return waysForAmt[-1]
        
    @staticmethod
    def test1():
        n = 6
        denoms = [1,5]
        Prob.numberOfWaysToMakeChange(n, denoms)
    
    @staticmethod
    def test2():
        n = 9
        denoms = [5,1]
        Prob.numberOfWaysToMakeChange(n, denoms)
    
    @staticmethod
    def test3():
        n = 25
        denoms = [1,5,10,25]
        ways = Prob.numberOfWaysToMakeChange(n, denoms)
        print("test3: ways: ", ways)
    
    @staticmethod
    def test4():
        n = 0
        denoms = [1,2,3,4]
        ways = Prob.numberOfWaysToMakeChange(n, denoms)
        print("test4: ways: ", ways)

#Prob.test1()
#Prob.test2()
#Prob.test3()
Prob.test4()


# find actual combinations (not correct implementation)
#     @staticmethod
#     def numberOfWaysToMakeChange(n, denoms):
#         denoms = sorted(denoms, reverse=True) # sort from large to small denoms
#         print("denoms sorted: ", denoms)
#         combos = []
#         for i in range(len(denoms)):
#             print("i = ", i)
#             j = i
#             for j in range(i,len(denoms)):
#                 print(  "    j = ", j)
#                 k = j
#                 nInit = n
#                 combo = []
#                 while k < len(denoms):
#                     print("        k = ", k)
#                     d = denoms[k]
#                     quo = int(nInit/d)
#                     rdr = nInit%d
#                     print("        d: {}, quo: {}, rdr: {}".format(d, quo, rdr))
#                     
#                     if quo >= 1:
#                         combo.append((quo, d)) #quantity, denomination
#                     
#                     nInit = rdr
#                     print("        nInit=rdr=", nInit)
#         
#                     k += 1
#                 print("        combo: ", combo)
#                 
#                 if combo not in combos:
#                     combos.append(combo)
#             
#         print("all combos: ", combos)