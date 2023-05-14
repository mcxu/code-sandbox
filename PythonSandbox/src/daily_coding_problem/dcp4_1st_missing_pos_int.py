'''
This problem was asked by Stripe. [Hard]

Given an array of integers, find the first missing positive integer in linear time and constant space. 
In other words, find the lowest positive integer that does not exist in the array. 
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
'''

import math
from utils.sorting_utils import SortingUtils

class DCP4():

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
            num = input[i]
            if num < 0:
                input.pop(i)
                i -= 1
            i += 1
        pos_sorted = SortingUtils.countingSort(input)
        print("pos_sorted: {}".format(pos_sorted))
        return pos_sorted

    
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
        #nums = [-1, -3, 45, 2, -7, 23, 4, 7, 2, 4]
        nums = [5,7,3,5,4,7,1,7,9,3,5,7,2,23,65,12,87]
        a = SortingUtils.countingSort(nums)
        print("test_counting_sort: input: {}, output: {}".format(nums, a))

    def test_split_and_sort_positives(self):
        nums = [-1, -3, 45, 2, -7, 23, 4, 7, 2, 4]
        a = self.split_and_sort_positives(nums)
        print("test_split_and_sort_positives: a: ", a)

    def test_first_missing_pos_int_1(self):
        l = [-1, -3, 45, 2, -7, 23, 4, 7, 2, 4]
        fmpi = self.first_missing_pos_int(l)
        print("test_first_missing_pos_int: fmpi: {}".format(fmpi))
    
    def test_first_missing_pos_int_2(self):
        l = [-4, -2, -8, 5,3,4,1,2,1]
        fmpi = self.first_missing_pos_int(l)
        print("test_first_missing_pos_int: fmpi: {}".format(fmpi))

def main():
    p4 = DCP4()
    #p4.test_counting_sort()
    #p4.test_split_and_sort_positives()
    p4.test_first_missing_pos_int_1()
    #p4.test_first_missing_pos_int_2()

if __name__ == "__main__":
    main()