"""
Product Sum

Write a function that takes in a "special" array and returns its product sum. 
A "special" array is a non-empty array that contains either integers or other "special" arrays. 
The product sum of a "special" array is the sum of its elements, where "special" arrays inside it 
should be summed themselves and then multiplied by their level of depth. 
For example, the product sum of [x, y] is x + y; the product sum of [x, [y, z]] is x + 2y + 2z.

Sample input: [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
Sample output: 12 (5 + 2 + 2 * (7 - 1) + 3 + 2 * (6 + 3 * (-13 + 8) + 4))
"""

class ProductSum:
    def productSum(self, array):
        # sum starts at 0, level starts at 1
        ps = self.productSumHelper(array, 0, 1)
        return ps

    def productSumHelper(self, array, ps, level):
        print("====== level:{}, array: {}, ps: {}".format(level, array, ps))
        for elt in array:
            if isinstance(elt, list):
                print("list found at level {}: {}".format(level+1, elt))
                # set the product sum of the nested problems to 0
                # because you are starting to count the product sums
                # within this subproblem, which should start from 0.
                ps += level*self.productSumHelper(elt, 0, level+1)
            else:
                ps += level*elt
                print("elt={}, level={}, ps={}".format(elt, level, ps))
        return ps


    def test_productSum(self):
        input = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
        output = self.productSum(input)
        print("test_productSum: output: ", output)
    
    def test_productSum2(self):
        input = [5, 2, 7, -1, 3, 6, -13, 8, 4]
        output = self.productSum(input)
        print("test_productSum2: output: ", output)
    
    def test_productSum3(self):
        input = [1,[2,[3]]]
        output = self.productSum(input)
        print("test_productSum3: output: ", output)


def main():
    ps = ProductSum()
    ps.test_productSum()
    #ps.test_productSum2()
    #ps.test_productSum3()

if __name__ == "__main__":
    main()