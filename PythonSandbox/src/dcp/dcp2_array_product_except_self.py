'''
This problem was asked by Uber. [Hard]

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
'''

class DCP2():
    ''' eval:
    Time complexity: O(n^2) where n:num values in a. Because of nested for loops.
    Space complexity: O(n), since the output stores up to n products.
    '''
    def eval(self, a):
        output = []
        for i in range(len(a)):
            p = []
            for j in range(len(a)):
                if(j != i):
                    p.append(a[j])
            print("p: {}".format(p))
            
            # take product of p
            prod = p[0]
            for k in range(1, len(p)):
                prod *= p[k]
            print("prod: {}".format(prod))
            
            # append prod to output
            output.append(prod)
        return output
    
    ''' eval2: using division
    Time complexity: O(n), where n~len(a). Because the 2 sequential for loops traverse at most n elements.
    Space complexity: O(n), because out stores at most n products.
    '''
    def eval2(self, a):
        maxProd = a[0]
        for i in range(1, len(a)):
            maxProd = maxProd * a[i]
        
        out = []
        for i in range(len(a)):
            out.append(int(maxProd/a[i]))
        return out
    
    ''' eval3: can't use division, solve in O(n). (https://www.youtube.com/watch?v=khTiTSZ5QZY)
    Time complexity: O(n): 4*n iterations: 2*n iters in for loop to populate leftProds and rightProds.
        2*n iters for return for loop with zip(leftProds,rightProds).
    Space complexity: 2*n total values stored in leftProds and rightProds
    '''
    def eval3(self, a):
        leftProds = [1]
        rightProds = [1]
        
        # make a separate array of products to the left of a value in the input array 
        # and a separate array of products to to the right of a value in the input array.
        # If there is no value to the left or right, then value in the aux arrays is 1.
        for i in range(0, len(a)-1):
            leftProds.append(leftProds[-1]*a[i])
            rightProds.insert(0, rightProds[0]*a[len(a)-1-i])
        print("leftProds populated: ", leftProds)
        print("rightProds populated: ", rightProds)
        return [i*j for i,j in zip(leftProds, rightProds)]

if __name__ == "__main__":
    p2 = DCP2()
    a = [1,2,3,4,5]
    out1 = p2.eval3(a)
    print("out1: {}".format(out1))
    
    b = [3,2,1]
    out2 = p2.eval3(b)
    print("out2: {}".format(out2))