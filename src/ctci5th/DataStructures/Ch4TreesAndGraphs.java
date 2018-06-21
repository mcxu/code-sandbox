package ctci5th.DataStructures;

import ctci5th.BTNode;

public class Ch4TreesAndGraphs 
{   
    //in-order, post-order, and pre-order traversals
    public static enum TraversalType {INORDER, POSTORDER, PREORDER};
    void traverseBinaryTree(BTNode root, TraversalType traversalType)
    {
        if(root == null)
        {
            return;
        }
        
        if(traversalType == TraversalType.PREORDER)
        {
            System.out.println("root.data: " + root.data);
        }
        traverseBinaryTree(root.left, traversalType);
        if(traversalType == TraversalType.INORDER)
        {
            System.out.println("root.data: " + root.data);
        } 
        traverseBinaryTree(root.right, traversalType);
        if(traversalType == TraversalType.POSTORDER)
        {
            System.out.println("root.data: " + root.data);
        } 
    }
    
    void test_traverseBinaryTree()
    {
        BTNode testTree = getTestTree1();
        System.out.println("In order:");
        traverseBinaryTree(testTree, TraversalType.INORDER);
        
        System.out.println("Post order:");
        traverseBinaryTree(testTree, TraversalType.POSTORDER);
        
        System.out.println("Pre order:");
        traverseBinaryTree(testTree, TraversalType.PREORDER);
    }
    
    
    public boolean isBalanced(BTNode root)
    {
        
        
        return false;
    }
    
//    void search(BTNode root)
//    {
//        if(root == null)
//        {
//            return;
//        }
//        visit(root);
//        
//        while(BTNode n in root.adja)
//    }
    
    public void printBinaryTree(BTNode root)
    {
        
    }
    
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
        Ch4TreesAndGraphs ch4 = new Ch4TreesAndGraphs();
        ch4.test_traverseBinaryTree();
    }

}
