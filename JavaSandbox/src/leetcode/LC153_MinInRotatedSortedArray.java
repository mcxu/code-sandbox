package leetcode;
//https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

class LC153_MinInRotatedSortedArray 
{
    public int findMin(int[] nums) {
        int i = 0;
        int j  = nums.length - 1;

        while(i <= j) 
        {
            int midIdx = (i+j)/2;

            if(midIdx-1 >= 0 && nums[midIdx-1] > nums[midIdx]){
                return nums[midIdx];
            }

            if(nums[i] <= nums[midIdx] && nums[midIdx] > nums[j]) {
                i = midIdx + 1;
            } else {
                j = midIdx - 1;
            }
        }

        return nums[i];
    }
}