'''
This problem was asked by Stripe. [Hard]

Given an array of integers, find the first missing positive integer in linear time and constant space. 
In other words, find the lowest positive integer that does not exist in the array. 
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
'''

import math

class P4():

    def first_missing_pos_int(self, input):
        input = self.split_and_sort_positives(input)
        print("first_missing_pos_int: split_and_sort_positives: {}".format(input))

        # handle case where lowest post int is inside array
        for i in range(len(input)-1):
            next_consecutive = input[i] + 1
            next_actual = input[i + 1]
            if(next_actual > next_consecutive):
                return next_consecutive

        # handle case where lowest pos int is outside array
        return input[len(input)-1] + 1

    def split_and_sort_positives(self, input):
        # split positive and negative numbers
        i=0
        while i < len(input):
            print("sort_positives")
            num = input[i]
            if num < 0:
                input.pop(i)
                i -= 1
            i += 1
        pos_sorted = self.counting_sort(input)
        print("pos_sorted: {}".format(pos_sorted))
        return pos_sorted

    def counting_sort(self, input):
        # identify highest value in input
        hi = -math.inf
        for val in input:
            if val > hi:
                hi = val
        print("highest val: {}".format(hi))

        # initialize counts array (need to include index up to highest val)
        counts = [0] * (hi+1)

        sa = [0] * len(counts) # sorted array
        print("sa initially: {}".format(sa))

        # count number of times each element occurs
        for i in range(len(input)):
            input_val = input[i]
            print("input_val: {}".format(input_val))
            counts[input_val] = counts[input_val] + 1
            print("counts: {}, elements: {}".format(counts, len(counts)))
        
        # create cumulative count of elements
        for j in range(1, hi):
            counts[j+1] = counts[j+1] + counts[j]
            print("j={}, cumulative count of elements: {}".format(j, counts))

        # sort the data
        print("input before sort: {}".format(input))
        for k in range(len(input)-1, -1, -1):
            input_k = input[k]
            print("k={}, input_k={}".format(k,input_k))
            c_of_input_k = counts[input_k]
            print(" c_of_input_k: {}".format(c_of_input_k))
            sa[c_of_input_k] = input_k
            print(" sa: {}".format(sa))
            counts[input_k] = counts[input_k] - 1

        return sa[1:len(input)+1]

    
    # def counting_sort_negatives(self, input):
    #     input_abs = [abs(x) for x in input]
    #     print("input_abs: {}".format(input_abs))
    #     sorted_abs = self.counting_sort(input_abs)
    #     print("sorted_abs: {}".format(sorted_abs))

    #     # reverse and make negative
    #     sorted_negatives = []
    #     for i in range(len(sorted_abs)-1, -1, -1):
    #         sorted_negatives.append(-sorted_abs[i])
    #     print("sorted_negatives: {}".format(sorted_negatives))
    #     return sorted_negatives

    def test_counting_sort(self):
        input_lists = [
            [5,2,7,1],
            [3, 4, -1, 1],
            [-1, -3, 45, 2, -7, 23, 4, 7, 2, 4]
            ]
        for input in input_lists: 
            a = self.counting_sort(input)
            print("test_counting_sort: input: {}, output: {}".format(input, a))

    def test_counting_sort_negatives(self):
        l = [-2,-12,-3,-7]
        self.counting_sort_negatives(l)

    def test_first_missing_pos_int_1(self):
        l = [-1, -3, 45, 2, -7, 23, 4, 7, 2, 4]
        fmpi = self.first_missing_pos_int(l)
        print("test_first_missing_pos_int: fmpi: {}".format(fmpi))
    
    def test_first_missing_pos_int_2(self):
        l = [-4, -2, -8, 5,3,4,1,2]
        fmpi = self.first_missing_pos_int(l)
        print("test_first_missing_pos_int: fmpi: {}".format(fmpi))

def main():
    p4 = P4()
    #p4.test_counting_sort()
    #p4.test_counting_sort_negatives()
    #p4.test_first_missing_pos_int_1()
    p4.test_first_missing_pos_int_2()

if __name__ == "__main__":
    main()