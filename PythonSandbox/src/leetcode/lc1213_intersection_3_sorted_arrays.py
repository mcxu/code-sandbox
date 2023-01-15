"""
https://leetcode.com/problems/intersection-of-three-sorted-arrays/

1213. Intersection of 3 sorted arrays
"""


class LC1213_Intersection3SortedArrays:

    def arraysIntersection(self, arr1, arr2, arr3):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type arr3: List[int]
        :rtype: List[int]
        """
        numdict = {}
        for a in arr1:
            print("a:{}".format(a))
            numdict[a] = 1

        for b in arr2:
            if(b in numdict.keys()):
                numdict[b] += 1

        for c in arr3:
            if(c in numdict.keys()):
                numdict[c] += 1

        print("numdict: {}".format(numdict))

        # check for occurrence of 3
        commons = []
        for key in numdict.keys():
            print("key: {}".format(key))
            occ = numdict[key]
            if(occ == 3):
                commons.append(key)

        return sorted(commons)

    # alternative solution; this one actually runs faster
    def arraysIntersection2(self, arr1, arr2, arr3):
        return sorted(set(arr1) & set(arr2) & set(arr3))

    def arraysIntersection3(self, arr1, arr2, arr3):
        uniqueVals = []

        i, j, k = 0, 0, 0
        print("i={}, j={}, k={}".format(i, j, k))

        while i < len(arr1) and j < len(arr2) and k < len(arr3):
            if arr1[i] == arr2[j] and arr2[j] == arr3[k]:
                uniqueVals.append(arr1[i])
                i += 1
                j += 1
                k += 1
            else:
                if arr1[i] > arr2[j]:
                    j += 1
                elif arr2[j] > arr3[k]:
                    k += 1
                else:
                    i += 1

        return uniqueVals


obj = LC1213_Intersection3SortedArrays()


def test():
    a = [1, 2, 3, 4, 5]
    b = [1, 2, 5, 7, 9]
    c = [1, 3, 4, 5, 8]
    output = obj.arraysIntersection3(a, b, c)
    print("output: ", output)


def test2():
    arr1 = [197, 418, 523, 876, 1356]
    arr2 = [501, 880, 1593, 1710, 1870]
    arr3 = [521, 682, 1337, 1395, 1764]
    output = obj.arraysIntersection3(arr1, arr2, arr3)
    print("output: ", output)


test2()
