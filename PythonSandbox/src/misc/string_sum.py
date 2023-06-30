"""
ab9q???qY1ery???y9ay?t?y?udf1
Match format <num><could be alpha chars>???<could be alpha chars><num>
Rules:
numbers on each side of ??? (3 question marks) should add up to 10
return True if so, False otherwise.
"""

# using a stack
def isValid_v2(s): 
    queue = []
    qMarkCount = 0
    i = 0
    while i < len(s):
        ch = s[i]

        if ch == "?":
            qMarkCount += 1

        if (qMarkCount == 0 or qMarkCount == 3) and ch.isdigit():
            queue.append(int(ch))
        
        if len(queue) == 2:
            qSum = sum(queue)
            if qSum != 10:
                return False

            queue.pop(0)
            qMarkCount = 0

        i += 1

    if qMarkCount > 0:
        return False

    return True


def isValid_v1(s):
    i = 0

    while i  < len(s)-1:
        ch = s[i]
        print(f"--- idx: {i}, ch: {ch}")
        qMarkCount = 0
        pairTotal = 0

        if ch.isdigit():
            pairTotal += int(ch)

            j = i+1
            #print(f"starting j: ", j)
            while j < len(s) and not s[j].isdigit():
                if s[j] == "?":
                    qMarkCount += 1
                j += 1
            #print(f"ending j: ", j, " jth char: ", s[j] if j < len(s) else None)

            if j > len(s)-1:
                return False

            if s[j].isdigit():
                pairTotal += int(s[j])
            
            if qMarkCount == 3 and pairTotal != 10:
                return False

            if qMarkCount != 3 and j == len(s)-1:
                return False
            
            i = j
        else:
            i += 1
    
    return True

def test():
    #s = "ab9q???qY1ery???y9ay?t?y?udf1" # expected True
    #s = "ab3q???qY7ery???y3ay?t?y?udf3" # expected False
    #s = "3???8" # expected False
    #s = "2??8" # expected False
    #s = "2???8" # expected True
    #s = "3???8" # expected False
    #s = "3q???u7" # expected True
    #s = "3q???uu" # expected False
    #s = "u?u" # expected False
    #s = "u???u" # expected False
    #s = "4???u" # expected False
    #s = "9???2" # expected false
    s = "2???8" # expected True
    # result = isValid_v1(s)
    result = isValid_v2(s)
    print("result: ", result)

test()
