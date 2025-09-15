"""
This problem was asked by Jane Street. [Medium]

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. 
For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

Implement car and cdr.
"""

class DCP5():
    def cons(self, a, b):
        print("cons: a={}, b={}".format(a,b))
        def pair(f):
            print("cons:pair: a={}, b={}".format(a,b))
            return f(a, b)
        return pair

    '''
    pass in the function definition of pair, but need a function to take place of f to return first or last element.
    Applies to both car and cdr
    '''
    def car(self, pair):
        print("in car")
        def f(a, b):
            print("car:first: a={}, b={}".format(a,b))
            return a
        return pair(f)

    def cdr(self, pair):
        print("in cdr")
        def f(a, b):
            print("cdr:last: a={}, b={}".format(a,b))
            return b
        return pair(f)

    def test_cons(self):
        pair = self.cons(3,4)
        print("pair: {}".format(pair))

        # pass in the function definition of 'pair'
        a = self.car(pair)
        print("test_cons: a: {}".format(a))
        b = self.cdr(pair)
        print("test_cons: b: {}".format(b))
    

def main():
    p5 = DCP5()
    p5.test_cons()

if __name__ == "__main__":
    main()