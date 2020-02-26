'''
This problem was asked by Uber. [Hard]

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
'''

class DCP2():
    
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
    
    def eval2(self, a):
        maxProd = a[0]
        for i in range(1, len(a)):
            maxProd = maxProd * a[i]
        
        out = []
        for i in range(len(a)):
            out.append(int(maxProd/a[i]))
        return out

if __name__ == "__main__":
    p2 = DCP2()
    a = [1,2,3,4,5]
    out1 = p2.eval2(a)
    print("out1: {}".format(out1))
    
    b = [3,2,1]
    out2 = p2.eval2(b)
    print("out2: {}".format(out2))