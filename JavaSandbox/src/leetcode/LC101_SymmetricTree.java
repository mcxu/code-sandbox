package leetcode;

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

public class LC101_SymmetricTree {
    public boolean isSymmetric(TreeNode root) {
        if ((root.left != null) && (root.right != null) && (root.left.val != root.right.val)) {
            return false;
        }

        return this.dfs(root.left, root.right);
    }

    public boolean dfs(TreeNode leftNode, TreeNode rightNode) {

        if(leftNode == null && rightNode == null)
            return true;

        if(leftNode != null && rightNode == null)
            return false;
        
        if(leftNode == null && rightNode != null)
            return false;
        
        if(leftNode.left != null && rightNode.right != null && (leftNode.left.val != rightNode.right.val))
            return false;
        
        if(leftNode.right !=null && rightNode.left != null && (leftNode.right.val != rightNode.left.val))
            return false;
        
        boolean leftIsSym = this.dfs(leftNode.left, rightNode.right);
        boolean rightIsSym = this.dfs(leftNode.right, rightNode.left);

        return leftIsSym && rightIsSym;
    }

    public static void main(String[] args) {
        LC101_SymmetricTree sol = new LC101_SymmetricTree();
        sol.test1(); 
    }

    //----------------- test cases -----------------

    public void test1() {
        int[] arr = {1,2,2,3,4,4,3};
        TreeNode root = this.arrToBinaryTree(arr);
        boolean isSym = this.isSymmetric(root);
        System.out.println("isSym: " + isSym);
    }
    
    //----------------------------------------------

    public TreeNode arrToBinaryTree(int[] arr) {
        TreeNode root = this.buildTree(arr, 0);        
        return root;
    }

    public TreeNode buildTree(int[] arr, int i) {
        if(i > arr.length-1) {
            return null;
        }
        
        TreeNode newNode = new TreeNode(arr[i]);
        newNode.left = this.buildTree(arr, 2*i+1);
        newNode.right = this.buildTree(arr, 2*i+2);
        return newNode;
    }
}
