'''
Watering Flowers 2.0
https://leetcode.com/discuss/interview-question/394347/

Example: Given plants=[2,4,5,1,2]
Capacities: c1 = 5, c2 = 7
Return Expected Refills = 3 
'''
import time # not needed, just for debugging

class Solution:
    def numRefills(self, plants, c1, c2):
        # start with 2 because persons 1 and 2 start with 0 water
        # and so need to refill their cans from the start.
        refills = 2
        i = 0; j = len(plants)-1
        amt1 = c1; amt2 = c2 # amounts in each person's can

        while i < j:
            print("------")
            print("amt1: {}, amt2: {}".format(amt1, amt2))
            print("i={}, j={}, planti: {}, plantj: {}".format(i, j, plants[i], plants[j]))
            
            planti = plants[i]
            print("planti: ", planti)
            if planti > c1:
                print("planti > c1")
                cr1 = int(planti/c1)-1 # complete refills from person 1 for a plant
                print("cr1: ", cr1)
                rem1 = planti%c1 # remaining water to add to a plant
                amt1 -= rem1
                refills += cr1
                print("planti refills if: ", refills)
            else:
                print("planti else: planti=", planti)
                if amt1 < planti:
                    print("amt1 < planti")
                    amt1 = c1
                    refills += 1
                    print("planti refills else: ", refills)
                amt1 -= planti
            print("amt1 now: ", amt1)
                    
            #time.sleep(.5)

            plantj = plants[j]
            print("plantj: ", plantj)
            if plantj > c2:
                print("plantj > c2")
                cr2 = int(plantj/c2)-1
                print("cr2: ", cr2)
                rem2 = plantj%c2
                amt2 -= rem2
                refills += cr2
                print("plantj refills if:", refills) 
            else:
                print("plantj else: plantj=", plantj)
                if amt2 < plantj:
                    print("amt2 < plantj")
                    amt2 = c2
                    refills += 1
                    print("plantj refills else: ", refills)
                amt2 -= plantj
            print("amt2 now: ", amt2)
                
            #time.sleep(.5)

            i += 1; j -= 1
        
        print("amt1 after: ", amt1)
        print("amt2 after: ", amt2)
        totAmt = amt1 + amt2
        if totAmt >= plants[i]:
            return refills
        
        # if totAmt is less than plants[i] (which is now the middle value),
        # then you know you need 1 more refill.
        return refills + 1

    def test1(self):
        plants=[2,4,5,1,2]
        #plants=[2,4,5,21,2]
        #plants = [1,2,5,4,3,5,3,5,4,2]
        #plants = [20,4,5,1,2]
        res = self.numRefills(plants, 5, 7)
        print("test1: res: ", res)

    def test2(self):
        #plants=[2,4,5,1,2]
        #plants=[2,4,5,21,2]
        #plants = [1,2,5,4,3,5,3,5,4,2]
        plants = [20,4,5,1,2]
        res = self.numRefills(plants, 20, 100) 
        print("test2: res: ", res)
    
s = Solution()
s.test1()
#s.test2()