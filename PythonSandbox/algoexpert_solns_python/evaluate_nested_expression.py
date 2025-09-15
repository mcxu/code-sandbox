'''
Given an expression string inside closed parenthesis,
calculate the result.

Ex. 
Input: ()
Output: 0

Ex.
Input: (1)
Output: 1

Ex. 
Input: (2+3)
Ouput: 5

Ex. 
Input: (3*(1+2))
Output: 9

Ex. 
Input: (4*(3+5*(2-3)))
Output: -8
'''

class Evaluator:
    def eval(self, expr):
        i = 0
        stack = []
        result = self.evalHelper(expr, i, stack)
        return result

    def evalHelper(self, expr, i, stack):
        char = expr[i]
        print("char: {}, stack: {}".format(char, stack))
        if not char.isnumeric():
            if char == "(":
                return self.evalHelper(expr, i+1, stack)
            elif char == ")":
                return stack[-1]
            
            top = stack[-1]
            if char == "+":
                print("A")
                return top + self.evalHelper(expr, i+1, stack)
            elif char == "*":
                print("B")
                return top * self.evalHelper(expr, i+1, stack)
            elif char == "-":
                print("C")
                return top - self.evalHelper(expr, i+1, stack)
        else:
            cn = int(char) # char as a number
            return self.evalHelper(expr, i+1, stack+[cn])
            #print('isnumeric: ', stack)
        
        return stack.pop()
    
    def test(self):
        expressions = [
            # "()", 
            # "(9)", 
            #"(4+3+2)" , 
            "(4-2-3)"
            ]
        for i,v in enumerate(expressions):
            print('----- test: ', i)
            print("expr: ", v)
            res = self.eval(v)
            print("res: ", res)


ev = Evaluator()
ev.test()
