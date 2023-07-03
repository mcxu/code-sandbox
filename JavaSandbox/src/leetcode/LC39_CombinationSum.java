package leetcode;

import java.util.List;
import java.util.ArrayList;
import java.util.Set;
import java.util.HashSet;
import java.util.Collections;

public class LC39_CombinationSum {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<Integer> currSolution = new ArrayList<>();
        Set<List<Integer>> allSolutions = new HashSet<List<Integer>>();

        this.dfs(candidates, target, currSolution, allSolutions);

        List<List<Integer>> output = new ArrayList<List<Integer>>();
        output.addAll(allSolutions);
        return output;
    }

    public void dfs(int[] candidates, int target, List<Integer> currSolution, Set<List<Integer>> allSolutions) {
        //System.out.printf("target: %s, currSolution: %s, allSolutions: %s\n", target, currSolution, allSolutions);
        if(target < 0) {
            return;
        }

        if(target == 0) {
            Collections.sort(currSolution);
            if(!allSolutions.contains(currSolution)) {
                allSolutions.add(currSolution);
            }
        }

        for(int i=0; i<candidates.length; i++) {
            int c = candidates[i];
            List<Integer> currSolutionCopy = new ArrayList<>(List.copyOf(currSolution));
            currSolutionCopy.add(c);
            this.dfs(candidates, target-c, currSolutionCopy, allSolutions);
            // currSolution.remove(currSolution.size()-1);
        }
    }
}
