class LC1213_Intersection3SortedArrays:
    """
    1213. Intersection of 3 sorted arrays
    """
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