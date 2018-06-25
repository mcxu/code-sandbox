package ctci5th.DataStructures;

import ctci5th.util.graph.GraphNode;

import java.util.Iterator;

import ctci5th.util.graph.DGNode;
import ctci5th.util.tree.BTNode;

public class Ch4TreesAndGraphs 
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
    
    
    public void searchDFS(GraphNode root)
    {
        if(root == null)
        {
            return;
        }
        
        visit(root);
        root.visited = true;
        
        Iterator<GraphNode> adjNodes = root.connections.iterator();
        while(adjNodes.hasNext())
        {
            GraphNode adjNode = adjNodes.next();
            if(adjNode.visited == false)
            {
                searchDFS(adjNode);
            }
        }
    }
    
    public void visit(GraphNode vertex)
    {
        System.out.println("visited: " + vertex.data);
    }
    
    public void test_searchDFS()
    {
        GraphNode initVertex = getGraph1();
        searchDFS(initVertex);
    }
    
    
    /**
     * Question 4.1: Function to check if binary tree is balanced.
     * @param root
     * @return
     */
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
    
    void testCh4p1()
    {
        BTNode testTree = getTestTree1();
        
        //make tree unbalanced
        BTNode five = new BTNode(5);
        testTree.left.right.left.right = five;
        
        boolean isBal = binaryTreeIsBalanced(testTree);
        System.out.println("isBal: " + isBal);
    }
    
    
    public boolean isRouteBetweenNodes(DGNode node)
    {
        return false; //TODO
    }
    
    ///////////////////// helpers ////////////////////

    public GraphNode getGraph1()
    {
        GraphNode a = new GraphNode("a");
        GraphNode b = new GraphNode("b");
        GraphNode c = new GraphNode("c");
        GraphNode d = new GraphNode("d");
        GraphNode e = new GraphNode("e");
        GraphNode f = new GraphNode("f");
        GraphNode g = new GraphNode("g");

        a.addNode(b); a.addNode(c);
        b.addNode(a); b.addNode(c);
        c.addNode(a); c.addNode(b); c.addNode(d);
        d.addNode(c); d.addNode(e);
        e.addNode(c); e.addNode(d); e.addNode(f);
        f.addNode(g);
        System.out.println("con: " + f.connections);
        g.printConnections();
        
        return g;
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
        //ch4.test_traverseBinaryTree();
        ch4.test_searchDFS();
        //ch4.testCh4p1();
        
    }

}
