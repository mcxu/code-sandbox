'''
Balanced brackets
Function that returns True with brackets are balanced, return False otherwise.

Sample input: "([])(){}(())()()"
Sample output: True
'''

class BB(object):
    
    """
    Time complexity: O(n), n=len(string). Since for loop iterates through all chars.
    Space complexity: O(n), since at the worst case, the string contains all opening parenthesis, so all chars are put on the stack.
    """
    @staticmethod
    def balancedBrackets(string):
        stack = []
        op = ["(","[","{"]
        
        for i in range(len(string)):
            ch = string[i]
            print("i={}, ch={}".format(i,ch))
            if ch in op:
                stack.append(ch)
                print("[A] stack: ", stack)
            else:
                # handle empty case
                if not stack:
                    return False
                
                if (ch==")" and stack[-1]=="(") or \
                    (ch=="]" and stack[-1]=="[") or \
                    (ch=="}" and stack[-1]=="{"):
                    stack.pop()
                    print("[B] stack after pop: ", stack)
                else:
                    print("[C] mismatch found: ch: {}, top of stack: {}".format(ch, stack[-1]))
                    return False
        
        if not stack:
            return True

        return False
    
    @staticmethod
    def test1():
        s1 = "([])(){}(())()()"
        s2 = "(([{}()])[])"
        s3 = "([])("
        s4 = "(((((({{{{{[[[[[([)])]]]]]}}}}}))))))" # failed, should be False
        s5 = "()()[{()})]" # failed, should be False
        s6 = "[[[[[[[[[[[[["
        testArray = [s5, s6]
        for s in testArray:
            print("------------- test1: s: ", s)
            res = BB.balancedBrackets(s)
            print("test1 result: ", res)

BB.test1()
