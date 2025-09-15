'''
Counting Sort
'''

class Prob:
    
    @staticmethod
    def countingSort(array):
        # if the array is blank, then return it
        if not array:
            return array
        
        # identify highest value k in input array
        k = max(array)
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
        sa = Prob.countingSort(l)
        print("test_countingSort: before sort:", l)
        print("test_countingSort: after sort:", sa)

Prob.test_countingSort()