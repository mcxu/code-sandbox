"""
Given an array of ints and an int.
Write function that moves all instances of this int, in array to the end.
Do this in-place. Does not need to maintain order of other ints in array.

Sample input: [2, 1, 2, 2, 2, 3, 4, 2], 2
Sample output: [1, 3, 4, 2, 2, 2, 2, 2] (the numbers 1, 3, and 4 could be ordered differently)
"""

class MVEnd:
    @staticmethod
    def moveElementToEnd(array, toMove):
        
        i = len(array) - 1 
        
        # partition pointer; separator for dirty section of list from ordered
        # ptn should define inclusive [: dirty boundary]
        ptn = len(array) - 1
        
        while i >= 0:
            iv = array[i]
            ptnVal = array[ptn]
            print("i: {}, iv: {},  ptn: {}, ptnVal: {}".format(i, iv, ptn, ptnVal))
            
            if iv == toMove:
                if not i == len(array)-1:
                    # swap ith num with (ptn-1)th num
                    tmp = array[i]
                    array[i] = array[ptn]
                    array[ptn] = tmp
                
                # update ptn <- ptn-1
                ptn -= 1
            print("    array: ", array)
            i -= 1
        
        return array
    
    @staticmethod
    def test_moveElementToEnd():
        array =  [2, 1, 2, 2, 2, 3, 4, 2]
        toMove = 2
        result = MVEnd.moveElementToEnd(array, toMove)
        print("result: ", result)
    
    @staticmethod
    def test_moveElementToEnd2():
        array = [3, 1, 2, 4, 5]
        toMove = 3
        result = MVEnd.moveElementToEnd(array, toMove)
        print("result: ", result)

MVEnd.test_moveElementToEnd()
#MVEnd.test_moveElementToEnd2()