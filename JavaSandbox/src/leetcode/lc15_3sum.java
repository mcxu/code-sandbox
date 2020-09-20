package leetcode;

import java.util.Collections;
import java.util.Set;
import java.util.HashSet;
import java.util.List;
import java.util.ArrayList;

public class lc15_3sum {
    public List<List<Integer>> threeSum(int[] nums) {
        Set<List<Integer>> triplets = new HashSet<List<Integer>>();
        
        for(int i=0; i < nums.length; i++) {
            //System.out.println("i=: " + i);
            int target = -1 * nums[i];
            //System.out.println("target: " + target);
            ArrayList<ArrayList<Integer>> twoSumResult = twoSum(nums, i+1, target);
            //System.out.println("twoSumResult: " + twoSumResult);
            for (ArrayList<Integer> result: twoSumResult) {
                result.add(0, nums[i]);
                Collections.sort(result);
                if (!triplets.contains(result)) {
                    triplets.add(result);
                }
                
            }
        }
        //System.out.println("triplets: " + triplets);
        ArrayList<List<Integer>> out = new ArrayList<List<Integer>>();
        out.addAll(triplets);
        return out;
    }
    
    public ArrayList<ArrayList<Integer>> twoSum(int[] nums, int i, int target) {
        ArrayList<ArrayList<Integer>> out = new ArrayList<ArrayList<Integer>>();
        Set<Integer> aux = new HashSet<>();
        for(int j=i; j < nums.length; j++) {
            if(aux.contains(target-nums[j])) {
                ArrayList<Integer> a = new ArrayList<>();
                a.add(nums[j]);
                a.add(target-nums[j]);
                out.add(a);
            } else {
                aux.add(nums[j]);
            }
        }
        return out;
    }
    
}
