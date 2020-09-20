package leetcode;

public class lc34_FirstLastPositionEltSortedArray {
    public int[] searchRange(int[] nums, int target) {
        int lo = 0;
        int hi = nums.length - 1;
        while(lo <= hi) {
            int med = (int)(hi-lo)/2;
            if(nums[lo] == target) {
                int[] res = expand(nums, target, lo);
                return res;
            } else if (nums[med] == target) {
                int[] res = expand(nums, target, med);
                return res;
            } else if (nums[hi] == target) {
                int[] res = expand(nums, target, hi);
                return res;
            }

            if(nums[med] < target) {
                lo += 1;
            } else {
                hi -= 1;
            }

        }

        return new int[]{-1, -1};
    }

    public int[] expand(int[] nums, int target, int i) {
        int j = i;
        while(i >= 0 && nums[i] == target) {
            i -= 1;
        }

        while(j <= nums.length-1 && nums[j] == target) {
            j += 1;
        }

        return new int[]{i+1, j-1};
    }

}
