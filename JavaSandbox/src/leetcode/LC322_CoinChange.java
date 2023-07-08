package leetcode;
//https://leetcode.com/problems/coin-change/description/

import java.util.Arrays;

public class LC322_MinNumOfCoinsForAmt {
    public int coinChange(int[] coins, int amount) {
        Arrays.sort(coins);
        int[] mncForAmt = new int[amount + 1];
        int LIM = (int)Math.pow(10, 6);
        Arrays.fill(mncForAmt, LIM);
        mncForAmt[0] = 0;
        //System.out.println("mncForAmt: " + Arrays.toString(mncForAmt));

        for(int amt=0; amt <= amount; amt++) {
            for(int denom: coins) {
                if(amt-denom >= 0) {
                    mncForAmt[amt] = Math.min(mncForAmt[amt], mncForAmt[amt-denom] + 1);
                } else {
                    break;
                }
            }
        }
        //System.out.println("final mncForAmt: " + Arrays.toString(mncForAmt));

        if(mncForAmt[amount] == LIM) {
            return -1;
        }
        return mncForAmt[amount];
    }
}
