# Complete the 'findSmallestDivisor' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#

def findSmallestDivisor(s, t):
    newt = t
    while len(newt) < len(s):
        newt += t
    #print("newt: ", newt)
    if newt == s:
        #print("is divisible")
        sms = smallestStr(s)
        return len(sms)
    else:
        #print("not divisible")
        return -1

# smallest repeated substring in s
def smallestStr(s):
    for i in range(len(s)):
        #print("i: ", i)
        aux = s[:i+1]
        #print("aux: ", aux)
        j = 0
        count = 0
        while j < len(s):
            #print("substr: ", s[i+1: i+1+len(aux)])
            if aux != s[i+1: i+1+len(aux)]:
                break
            else:
                count += 1
            
            if count == len(s):
                return aux

            j += 1
    return s