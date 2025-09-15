"""
https://algodaily.com/challenges/targets-and-vicinities

Time complexity: O(n)
    let n ~ max(len(actual), len(guess))
    1st for loop: O(n)
    2nd for loop: O(n)
    3rd for loop: O(n)
Space complexity:
    There are 2 maps with worst case O(n), so overall space complexity is O(n)
"""

def getTandV(actual, guess):
    idxMap = {} # for actual
    
    for i,ch in enumerate(actual):
        if ch in idxMap.keys():
            idxMap[ch].add(i)
        else:
            idxMap[ch] = set([i])

    guessIdxMap = {ch:"V" for _,ch in enumerate(guess)} # char -> T/V/None

    for i, guessChar in enumerate(guess):
        if guessChar in idxMap.keys():
            if i in idxMap[guessChar]:
                guessIdxMap[guessChar] = "T"
        else:
            guessIdxMap[guessChar] = None

    numTargets = 0
    numVincinities = 0
    for k in guessIdxMap.keys():
        val = guessIdxMap[k]
        if val == 'T':
            numTargets += 1
        elif val == 'V':
            numVincinities += 1

    return f"{numTargets}T{numVincinities}V"

# =================================================================

def getIdxMap(s):
    m = {}
    for i,ch in enumerate(s):
        if ch in m.keys():
            m[ch].add(i)
        else:
            m[ch] = set([i])
    return m

""" Version 2
let n ~ max(len(actual), len(guess))
Time complexity: overall O(n)
    Populating both maps is O(n)
    For loop going through guessIdxMap is O(n)
    The set intersection operation is close to O(1) unless actual and guess are the same, however
        this would NOT increase time complexity to O(n^2) since there would be only 1 key in the map.
Space complexity: overall o(n)
    2 maps are worst case O(n)
"""
def getTandV_version2(actual, guess):
    actualIdxMap = getIdxMap(actual)
    guessIdxMap = getIdxMap(guess)
    print(f"actualIdxMap: {actualIdxMap}, \nguessIdxMap:  {guessIdxMap}")

    numTargets = 0
    numVincinities = 0
    for guessChar in guessIdxMap.keys():
        if guessChar in actualIdxMap.keys():
            hits = guessIdxMap[guessChar].intersection(actualIdxMap[guessChar])
            #print(f"guessChar:{guessChar}, hits:{hits}")
            if len(hits) > 0:
                numTargets += 1
            else:
                numVincinities += 1

    return f"{numTargets}T{numVincinities}V" 

def test1():
    # actual, guess
    #testCase = ["34", "34"] # expected : 2T0V
    #testCase = ["345", "135"] # expected: 1T1V
    #testCase = ["45624", "24325"] # expected: 1T2V
    testCase = ["33333", "33343"]

    actual = testCase[0]
    guess = testCase[1]
    result = getTandV_version2(actual, guess)
    print("result: ", result)
    
test1()