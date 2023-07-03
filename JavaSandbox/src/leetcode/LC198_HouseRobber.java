package leetcode;

import java.util.HashMap;

public class LC198_HouseRobber {
    public int rob(int[] nums) {
        int i = 0;
        HashMap<Integer, Integer> memo = new HashMap<>();
        int maxReward = this.getReward(nums, i, memo);
        return maxReward;
    }

    public Integer getReward(int[] nums, int i, HashMap<Integer, Integer> memo)
    {
        if(i > nums.length-1) {
            return 0;
        }

        if(memo.containsKey(i)) {
            return memo.get(i);
        }

        Integer robCurrent = this.getReward(nums, i+2, memo) + nums[i];
        Integer dontRobCurrent =  this.getReward(nums, i+1, memo);
        Integer maxResult = Math.max(robCurrent, dontRobCurrent);
        memo.put(i, maxResult);
        return memo.get(i);
    }
}
