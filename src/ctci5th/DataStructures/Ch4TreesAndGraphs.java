package ctci5th.DataStructures;

import ctci5th.BTNode;

public class Ch4TreesAndGraphs 
{   
    //in-order traversal
    void traverseTreeInOrder(BTNode root)
    {
        if(root == null)
        {
            return;
        }
        traverseTreeInOrder(root.left);
        System.out.println("root.data: " + root.data);
        traverseTreeInOrder(root.right);
    }
    
    void test_traverseTreeInOrder()
    {
        BTNode testTree = getTestTree1();
        
        traverseTreeInOrder(testTree);
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
        ch4.test_traverseTreeInOrder();

    }

}
