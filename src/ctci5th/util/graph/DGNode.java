package ctci5th.util.graph;

import java.util.Iterator;

/**
 * Directed Graph Node
 * @author MichaelXu
 *
 */
public class DGNode extends GraphNode 
{
    public DGNode(Object data)
    {
        super(data);
    }
    
    @Override
    public void printConnections()
    {
        Iterator<GraphNode> iter = super.connections.iterator();
        
        System.out.println("this node: " + this + "\tdata: " + this.data);
        while(iter.hasNext())
        {
            DGNode toNode = (DGNode) iter.next();
            System.out.println("\tpoints to " + toNode + "\tdata: " + toNode.data);
        }
    }
    
    public static void main(String[] args) {
        DGNode a = new DGNode(1);
        DGNode b = new DGNode(2);
        DGNode c = new DGNode(3);
        DGNode d = new DGNode(4);
        DGNode e = new DGNode(5);
        
        a.addNode(b);
        b.addNode(c);
        c.addNode(a);
        c.addNode(d);
        e.addNode(c);
        e.addNode(d);
        
        a.printConnections();
        b.printConnections();
        c.printConnections();
        e.printConnections();
    }

}
