package leetcode;

public class LC152_MaxProductSubarray {
    public int maxProduct(int[] nums) {
        int prevMaxUpTo = nums[0];
        int prevMinUpTo = nums[0];

        int prevMaxPossible = 1;
        int prevMinPossible = 1;

        int currMaxUpTo = nums[0];
        int currMinUpTo = nums[0];

        int currMaxSoFar = nums[0];

        for(int i=1; i < nums.length; i++) {
            //System.out.println("i:" + i);
            int n = nums[i];

            prevMaxPossible = Math.max(prevMinUpTo*n, prevMaxUpTo*n);
            currMaxUpTo = Math.max(prevMaxPossible, n);

            prevMinPossible = Math.min(prevMinUpTo*n, prevMaxUpTo*n);
            currMinUpTo = Math.min(prevMinPossible, n);

            if(currMaxUpTo > currMaxSoFar) {
                currMaxSoFar = currMaxUpTo;
            }

            prevMaxUpTo = currMaxUpTo;
            prevMinUpTo = currMinUpTo;
        }

        return currMaxSoFar;
    }
}

class Test {
    public static void main(String[] args) {
        LC152_MaxProductSubarray lc152 = new LC152_MaxProductSubarray();
        test1(lc152);
    }
    
    public static void test1(LC152_MaxProductSubarray lc) {
        int[] nums = {2,3,-2,4};
        int expected = 6;
        
        int result = lc.maxProduct(nums);
        System.out.println("result: " + result);
        assert result == expected;
    }
}
