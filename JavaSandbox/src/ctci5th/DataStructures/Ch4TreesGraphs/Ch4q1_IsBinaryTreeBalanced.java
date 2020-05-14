/**
 * Question 4.1: Function to check if binary tree is balanced.
 */
package ctci5th.DataStructures.Ch4TreesGraphs;

import ctci5th.util.tree.BTNode;

public class Ch4q1_IsBinaryTreeBalanced 
{
    public boolean binaryTreeIsBalanced(BTNode node)
    {
        int balHeight = balancedHeight(node);
        System.out.println("balHeight: " + balHeight);
        
        if (balHeight > -1) 
            return true;
        return false;
    }
    
    public int balancedHeight(BTNode n) {
        if (n == null) 
            return 0;
        
        System.out.println("n.data= " + n.data);
        int hLeft = balancedHeight(n.left);
        System.out.println("hLeft=" + hLeft);
        int hRight = balancedHeight(n.right);
        System.out.println("hRight=" + hRight);
     
        if (hLeft == -1 || hRight == -1) 
            return -1;
        
        if (Math.abs(hLeft - hRight) > 1) 
            return -1;
        
        if (hLeft > hRight) 
            return hLeft + 1;
        return hRight + 1;
    }
    
    public void test1()
    {
        BTNode testTree = getTestTree1();
        
        //make tree unbalanced
        BTNode five = new BTNode(5);
        testTree.left.right.left.right = five;
        
        boolean isBal = binaryTreeIsBalanced(testTree);
        System.out.println("isBal: " + isBal);
    }
    
    
    ///////////////////// helpers ////////////////////
    
    public BTNode getTestTree1()
    {
        BTNode two = new BTNode(2);
        BTNode three = new BTNode(3);
        BTNode four = new BTNode(4);
        BTNode six = new BTNode(6);
        BTNode eight = new BTNode(8);
        BTNode nine = new BTNode(9);
        BTNode twelve = new BTNode(12);
        
        eight.left = three;
        eight.left.left = two;
        eight.left.right = six;
        eight.left.right.left = four;
        eight.right = twelve;
        eight.right.left = nine;
        
        return eight;
    }
    
    public static void main(String[] args) {
        Ch4q1_IsBinaryTreeBalanced prob = new Ch4q1_IsBinaryTreeBalanced();
        prob.test1();
    }
}
