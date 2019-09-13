'''
Created on Aug 24, 2019

This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. 
In other words, find the lowest positive integer that does not exist in the array. 
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
'''

import math

class P4():

    def first_missing_pos_int(self, input):
        pass

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

    def test_counting_sort(self):
        input_lists = [
            [5,2,7,1],
            [3, 4, -1, 1],
            [-1, -3, 45, 2, -7, 23, 4, 7, 2, 4]
            ]
        for input in input_lists: 
            a = self.counting_sort(input)
            print("test_counting_sort: input: {}, output: {}".format(input, a))


    def test_first_missing_pos_int(self):
        pass

def main():
    p4 = P4()
    p4.test_counting_sort()
    #p4.test_first_missing_pos_int()


if __name__ == "__main__":
    main()