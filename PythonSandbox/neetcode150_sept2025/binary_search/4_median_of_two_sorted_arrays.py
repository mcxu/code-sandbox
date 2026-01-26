from typing import List

class Med2SortedArrays:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1, len2 = len(nums1), len(nums2)

        # 1. Ensure nums1 is the shorter array for O(log(min(m, n))) complexity
        # By swapping, we ensure the binary search is performed on the smaller search space.
        if len1 > len2:
            return self.findMedianSortedArrays(nums2, nums1)

        # half: The number of elements needed on the left side of the combined median cut
        half = (len1 + len2 + 1) // 2

        # Binary search range for the cut in nums1
        # 'cut1' will be the number of elements taken from nums1 for the left partition
        lo, hi = 0, len1

        while lo <= hi:
            # i: The cut point index in nums1 (number of elements taken from nums1)
            i = lo + (hi - lo) // 2
            # j: The cut point index in nums2 (number of elements taken from nums2)
            # We must ensure i + j = half
            j = half - i
            
            # 2. Define the four elements surrounding the median cut
            # Left side boundary elements
            # A_left is the last element of the left partition of nums1
            A_left = nums1[i - 1] if i > 0 else float('-inf')
            # B_left is the last element of the left partition of nums2
            B_left = nums2[j - 1] if j > 0 else float('-inf')

            # Right side boundary elements
            # A_right is the first element of the right partition of nums1
            A_right = nums1[i] if i < len1 else float('inf')
            # B_right is the first element of the right partition of nums2
            B_right = nums2[j] if j < len2 else float('inf')

            # 3. Check for the Perfect Partition
            # The cut is perfect if:
            # 1. Every element in the left partition is <= every element in the right partition.
            # 2. The left partition has exactly 'half' elements.
            if A_left <= B_right and B_left <= A_right:
                # Perfect partition found!
                # Odd length: Median is the largest element in the left partition
                if (len1 + len2) % 2 == 1:
                    return max(A_left, B_left)
                # Even length: Median is the average of the two middle elements
                else:
                    left_max = max(A_left, B_left)
                    right_min = min(A_right, B_right)
                    return (left_max + right_min) / 2.0

            # 4. Adjust the Binary Search Range (Not a perfect cut)
            # If A_left > B_right, it means A_left is too large.
            # We need to move the cut in nums1 to the left (i.e., take fewer elements from nums1).
            elif A_left > B_right:
                hi = i - 1
            # If B_left > A_right, it means A_right is too small.
            # We need to move the cut in nums1 to the right (i.e., take more elements from nums1).
            else: # B_left > A_right
                lo = i + 1

        # Should not be reached if inputs are valid arrays
        return 0.0
    