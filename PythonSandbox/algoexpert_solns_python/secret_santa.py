"""
https://www.youtube.com/watch?v=y7FtwrjWXCg
"""

import random

def createList(players):
    pairs = []

    while len(players) > 0:
        currPair = []

        if len(players) == 1:
            return pairs

        i = 0
        while i < 2:
            randomIdx = random.randint(0, len(players)-1)
            selectedPlayer = players.pop(randomIdx)
            currPair.append(selectedPlayer)
            i += 1
        
        #print("currPair: ", currPair)
        pairs.append(currPair)
    
    return pairs

def test():
    # input = ["Barney", "Wilma", "Fred", "Pebbles", "Bam Bam"]
    input = ["Barney", "Wilma", "Fred", "Pebbles"]
    output = [["Barney", "Wilma"], ["Fred", "Pebbles"]] # possible output

    result = createList(input)
    print("result: ", result)

test()