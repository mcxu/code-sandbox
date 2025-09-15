'''
1352. Product of the Last K Numbers
Implement the class ProductOfNumbers that supports two methods:

1. add(int num)
Adds the number num to the back of the current list of numbers.

2. getProduct(int k)
Returns the product of the last k numbers in the current list.

You can assume that always the current list has at least k numbers.
At any time, the product of any contiguous sequence of numbers will fit into a 
single 32-bit integer without overflowing.
'''

class ProductOfNumbers:

    def __init__(self):
        self.prods = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.prods = [1]
        else:
            self.prods.append(self.prods[-1]*num)

    def getProduct(self, k: int) -> int:
        if k > len(self.prods)-1:
            return 0
        return int(self.prods[-1]/self.prods[len(self.prods)-1-k])
    
    def test1(self):
        seq = ["ProductOfNumbers","add","add","add","add","add","getProduct","getProduct","getProduct","add","getProduct"]
        amt = [[],[3],[0],[2],[5],[4],[2],[3],[4],[8],[2]]
        results = []
        pon = ProductOfNumbers()
        for i in range(1, len(seq)):
            seqStr = seq[i]
            amtNum = amt[i][0]
            if seqStr == "add":
                pon.add(amtNum)
                results.append(["add {}".format(amtNum)])
            elif seqStr == "getProduct":
                prod = pon.getProduct(amtNum)
                results.append(["k={},p={}".format(amtNum, prod)])
        
        print("results: ", results)

pon = ProductOfNumbers()
pon.test1()