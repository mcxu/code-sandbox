'''
Intersection of 2 sorted arrays.
'''

class Prob:
    '''
    Time complexity: O(len(arr1) + len(arr2))
    Space complexity: O(1), excluding the matches array since that's the output.
    '''
    @staticmethod
    def intersectionOf2SortedArrays(arr1, arr2):
        matches = []
        i = 0 # for arr1
        j = 0 # for arr2
        while i < len(arr1) and j < len(arr2):
            a1Val = arr1[i]
            a2Val = arr2[j]
            if a1Val < a2Val:
                i += 1
            elif a1Val > a2Val:
                j += 1
            else:
                matches.append(a1Val)
                i += 1
                j += 1
        return matches
    
    @staticmethod
    def test1():
        arr1 = [1,12,15,19,20,21]
        arr2 = [2,15,17,19,21,25,27]
        matches = Prob.intersectionOf2SortedArrays(arr1, arr2)
        print("test1 matches: ", matches)
                    
Prob.test1()