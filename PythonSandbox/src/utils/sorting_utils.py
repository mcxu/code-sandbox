from utils.number_utils import NumberUtils
from lib2to3.fixer_util import Number

class SortingUtils:
    
    @staticmethod
    def countingSort(array):
        # if the array is blank, then return it
        if not array:
            return array
        
        # identify highest value k in input array
        k = NumberUtils.getHighestVal(array)
        #print("highest val: {}".format(k))
 
        # initialize counts array (need to include index up to highest val)
        counts = [0] * (k+1)
        #print("counts: ", counts)
        sa = [0] * len(array) # sorted array
        #print("sa initially: {}".format(sa))
  
        # count number of times each element in input array occurs
        # then record that with the counts array
        for i in range(len(array)):
            input_val = array[i]
            #print("input_val: {}".format(input_val))
            counts[input_val] = counts[input_val] + 1
            #print("counts: {}, elements: {}".format(counts, len(counts)))
          
        # create cumulative count of elements
        for j in range(1, k+1):
            counts[j] = counts[j] + counts[j-1]
            #print("j={}, cumulative count of elements: {}".format(j, counts))
  
        # sort the data
        for m in range(len(array)-1, -1, -1):
            input_m = array[m]
            #print("m={}, input_m={}".format(m,input_m))
            c_of_input_m = counts[input_m]
            #print("    c_of_input_m: {}".format(c_of_input_m))
            sa[c_of_input_m-1] = input_m
            #print("    sa: {}".format(sa))
            counts[input_m] = counts[input_m] - 1
            #print("    counts:", counts)
            
        return sa

    @staticmethod
    def test_countingSort():
        #l = [5,0,3,4,1,2]
        #l = [6,8,2,26,4,3,12,4,15]
        l = [5,7,3,5,4,7,1,7,9,3,5,7,2,23,65,12,87]
        sa = SortingUtils.countingSort(l)
        print("test_countingSort: before sort:", l)
        print("test_countingSort: after sort:", sa)

    @staticmethod
    def mergeSort(array):
        if not array or len(array)==1:
            return array
        median = int(len(array)/2)
        l = array[:median]
        r = array[median:]
        print("mergeSort: median:{}, l:{}, r:{}".format(median,l,r))
        sl = SortingUtils.mergeSort(l)
        sr = SortingUtils.mergeSort(r)
        return SortingUtils.mergeArrays(sl,sr)
    
    # merge pre-sorted arrays
    @staticmethod
    def mergeArrays(l,r):
        
        # check if empty
        if not l:
            return l
        if not r:
            return r
        
        out = []
        i = 0
        j = 0
        while(i<len(l) and j<len(r)):
            lv = l[i]; rv = r[j]
            print("=====\ni={}, j={}".format(i,j))
            print("l:{}, r:{}, lv:{}, rv:{}".format(l,r, lv, rv))
            
            if lv <= rv:
                out.append(lv)
                i += 1
            else:
                out.append(rv)
                j += 1
                
            print("out: {}".format(out))
        
        # handle remaining left
        while(i < len(l)):
            out.append(l[i])
            i += 1
        
        # handle remaining right
        while(j < len(r)):
            out.append(r[j])
            j += 1
        return out    
    
    @staticmethod
    def test_mergeArrays():
        a = [1,4,7,128,129,130]
        b = [2,5,6,12,56,102,103,104,105,106,110,120,130]
        out = SortingUtils.mergeArrays(a,b)
        print(out)
    
    @staticmethod
    def test_mergeSort():
        a= [1,5,4,2,3]
        s = SortingUtils.mergeSort(a)
        print("s: ", s)
    
    @staticmethod
    def test_mergeSort2():
        a = []
        s = SortingUtils.mergeSort(a)
        print("sorting empty: ", s)
    
    @staticmethod
    def test_mergeSort3():
        a = NumberUtils.generateRandomNumbers(0, 10000, 100, allowDuplicates=False)
        s = SortingUtils.mergeSort(a)
        print("sorted: ", s)

def main():
    #SortingUtils.test_countingSort()
    #SortingUtils.test_mergeArrays()
    #SortingUtils.test_mergeSort()
    #SortingUtils.test_mergeSort2()
    SortingUtils.test_mergeSort3()

if __name__ == "__main__":
    main()