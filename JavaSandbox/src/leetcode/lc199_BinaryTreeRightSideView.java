package leetcode;

import java.util.List;
import java.util.Map;
import java.util.TreeMap;
import java.util.ArrayList;

public class lc199_BinaryTreeRightSideView {
    Map<Integer, Integer> depthMap = new TreeMap<Integer, Integer>();
    
    public List<Integer> rightSideView(TreeNode root) {
        int depth = 0;
        
        this.helper(root, depth, depthMap);

        List<Integer> output = new ArrayList<Integer>();
        for(Integer d : depthMap.keySet()) {
            output.add(depthMap.get(d));
        }
        return output;
    }
    
    public void helper(TreeNode root, Integer depth, Map<Integer, Integer> depthMap) {
        if(root == null) {
            return;
        }
        
        depthMap.put(depth, root.val);

        this.helper(root.left, depth+1, depthMap);
        this.helper(root.right, depth+1, depthMap);
    }
}

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}