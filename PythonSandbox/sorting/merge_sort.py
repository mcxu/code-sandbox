'''
Merge Sort
'''

from utils.number_utils import NumberUtils

class Prob:
    def mergeSort(self, array):
        if not array or len(array)==1:
            return array
        median = int(len(array)/2)
        left = array[:median]
        right = array[median:]
        #print("mergeSort: median:{}, l:{}, r:{}".format(median,left,right))
        sl = self.mergeSort(left)
        sr = self.mergeSort(right)
        return Prob.mergeArrays(sl,sr)
    
    # merge pre-sorted arrays
    def mergeArrays(self, l,r):
        print("merging arrays: l:{}, r:{}".format(l,r))
        
        out = []
        i = 0
        j = 0
        while(i<len(l) and j<len(r)):
            lv = l[i]; rv = r[j]
            #print("=====\ni={}, j={}".format(i,j))
            #print("l:{}, r:{}, lv:{}, rv:{}".format(l,r, lv, rv))
            
            if lv <= rv:
                out.append(lv)
                i += 1
            else:
                out.append(rv)
                j += 1
        
        if i < len(l):
            # handle remaining left
            out += l[i:]
        elif j < len(r):
            # handle remaining right
            out += r[j:]
            
        return out    
    
    @staticmethod
    def test_mergeArrays():
        a = [1,4,7,128,129,130]
        b = [2,5,6,12,56,102,103,104,105,106,110,120,130]
        out = Prob.mergeArrays(a,b)
        print(out)
    
    @staticmethod
    def test_mergeSort():
        a= [1,5,4,2,3]
        s = Prob.mergeSort(a)
        print("s: ", s)
    
    @staticmethod
    def test_mergeSort2():
        a = []
        s = Prob.mergeSort(a)
        print("sorting empty: ", s)
    
    @staticmethod
    def test_mergeSort3():
        a = NumberUtils.generateRandomNumbers(0, 10000, 100, allowDuplicates=False)
        s = Prob.mergeSort(a)
        print("sorted: ", s)
    

#Prob.test_countingSort()
#Prob.test_mergeArrays()
#Prob.test_mergeSort()
#Prob.test_mergeSort2()
#Prob.test_mergeSort3()
