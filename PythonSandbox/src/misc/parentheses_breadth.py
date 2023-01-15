'''
Given string that has valid parentheses. Get the max breadth of the parentheses.
"()()()" return 3
"(()()())" return 3
"(())(())" return 2
'''
# TODO: incorrect
def getBreadth(s):
    m = {}
    stack = []
    for i,p in enumerate(s):
        print("---- i: {}, p: {}, stack: {}".format(i, p, stack))
        print("m: ", m)
        if stack and stack[-1]=="(":
            if p==")":
                stack.pop()
            else:
                stack.append(p)

            if len(stack) not in m.keys():
                m[len(stack)] = 1
            else:
                m[len(stack)] += 1 
        else:
            stack.append(p)

        print("stack: B:", stack)
        print("m B: ", m)

    return max(m.values())

def test1():
    #s = "()()()" # 3
    #s = "(()()())" # 3
    #s = "(())"
    s = "(())(()())"
    res = getBreadth(s)
    print("res: ", res)
test1()    
