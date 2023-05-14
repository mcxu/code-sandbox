"""
ab9q???qY1ery???y9ay?t?y?udf1

Match format <num><could be alpha chars>???<could be alpha chars><num>
"""

def isValid(s):
    i = 0

    while i < len(s)-1:
        ci = s[i]

        qMarkCount = 0
        pairTotal = 0
        
        if ci.isdigit():
            pairTotal += int(ci)
            
            j = i+1
            while j  < len(s) and not s[j].isdigit():
                if s[j] == "?":
                    qMarkCount += 1
                j += 1

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


# def isValid(s):
#     i = 0

#     while i < len(s)-1:
#         ci = s[i]

#         qMarkCount = 0
#         pairTotal = 0

#         if ci.isdigit():
#             pairTotal += int(ci)
            
#             j = i+1
#             while j < len(s) and not s[j].isdigit():
#                 if s[j] == "?":
#                     qMarkCount += 1
#                 j += 1
            
#             if s[j].isdigit():
#                 pairTotal += int(s[j])
            
#             if qMarkCount == 3 and pairTotal != 10:
#                 return False
            
#             if qMarkCount != 3 and j == len(s)-1:
#                 return False
            
#             i = j
#         else:
#             i += 1
    
#     return True

def test():
    #s = "ab9q???qY1ery???y9ay?t?y?udf1" # expected True
    # s = "3???8" # expected False
    #s = "2??8"
    #s = "2???8" # expected True
    #s = "3???8" # expected False
    s = "3q???u7" # expected True
    result = isValid(s)
    print("result: ", result)

test()
