package ctci5th;

/**
 * Node class for a binary tree (Chapter 4 Trees and Graphs)
 * @author MichaelXu
 *
 */
public class BTNode
{
    public BTNode left = null;
    public BTNode right = null;
    
    //node data
    public boolean visited = false;
    public Object data;
    
    public BTNode(Object data)
    {
        this.data = data;
    }
    
    public static void main(String[] args) 
    {
        BTNode root = new BTNode(1);
        BTNode n2 = new BTNode(2);
        BTNode n3 = new BTNode(3);
        BTNode n4 = new BTNode(4);
        BTNode n5 = new BTNode(5);
        
        root.left = n2;
        root.right = n3;
        root.left.left = n4;
        root.left.right = n5;
        
        System.out.println("root: " + root.data);
        System.out.println("root->left: " + root.left.data);
        
        System.out.println("n4: " + n4.data);
    } 

}
