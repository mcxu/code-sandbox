package ctci5th.DataStructures.Ch4TreesGraphs;
import ctci5th.util.tree.BTNode;

public class TreeTraversalTypes 
{   
    //in-order, post-order, and pre-order traversals
    public static enum TraversalType {INORDER, POSTORDER, PREORDER};
    void traverseBinaryTree(BTNode node, TraversalType traversalType)
    {
        if(node == null)
        {
            return;
        }
        
        if(traversalType == TraversalType.PREORDER)
        {
            System.out.println("node.data: " + node.data);
        }
        traverseBinaryTree(node.left, traversalType);
        if(traversalType == TraversalType.INORDER)
        {
            System.out.println("node.data: " + node.data);
        } 
        traverseBinaryTree(node.right, traversalType);
        if(traversalType == TraversalType.POSTORDER)
        {
            System.out.println("node.data: " + node.data);
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
        TreeTraversalTypes prob = new TreeTraversalTypes();
        prob.test_traverseBinaryTree();
    }
}
