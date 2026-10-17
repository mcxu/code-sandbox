def validParenthesis(s):
    stack = []

    # map closing parenthesis to opening parenthesis
    charMap = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for _,c in enumerate(s):
        print("--- c: ", c)
        print("stack: ", stack)
        if not stack:
            stack.append(c)
        else:
            if c in charMap:
                if stack[-1] == charMap[c]:
                    stack.pop(-1)
                else:
                    return False
            else:
                stack.append(c)

    if stack:
        return False
    
    return True

def test1():
    #s = "([{}])"
    # s = "[[][{][][()][}]]"
    result = validParenthesis(s)
    print("result: ", result)

test1()

