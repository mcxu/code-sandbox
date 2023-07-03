package leetcode;

public class LC53_MaximumSubarray 
{
    public int maxSubArray(int[] nums) {
        int maxSumSoFar = Integer.MIN_VALUE;
        int maxSumUpToN = 0;

        for(int i=0; i < nums.length; i++) {
            int n = nums[i];

            if(maxSumUpToN + n > n) {
                maxSumUpToN = maxSumUpToN + n;
            } else {
                maxSumUpToN = n;
            }

            maxSumSoFar = Math.max(maxSumSoFar, maxSumUpToN);
        }

        return maxSumSoFar;
    }
}

class Test {
    public static void main(String[] args) {
        LC53_MaximumSubarray lc53 = new LC53_MaximumSubarray();
        test1(lc53);
    }
    
    public static void test1(LC53_MaximumSubarray lc53) {
        int[] nums = {-2,1,-3,4,-1,2,1,-5,4};
        int expected = 6;
        
        int result = lc53.maxSubArray(nums);
        System.out.println("result: " + result);
        assert result == expected;
    }
}