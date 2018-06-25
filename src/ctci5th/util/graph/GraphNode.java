package ctci5th.util.graph;

import java.util.Set;
import java.util.HashSet;
import java.util.Iterator;

public class GraphNode 
{
    public Set<GraphNode> connections;
    
    public Object data;
    public boolean visited;
    
    public GraphNode(Object data)
    {
        this.data = data;
        this.visited = false;
        connections = new HashSet<GraphNode>();
    }
    
    public void addNode(GraphNode node)
    {
        connections.add(node);
    }
    
    public void printConnections()
    {
        Iterator<GraphNode> iter = connections.iterator();
        
        System.out.println("this node: " + this + "\tdata: " + this.data);
        while(iter.hasNext())
        {
            GraphNode toNode = iter.next();
            System.out.println("\tconnects to " + toNode + "\tdata: " + toNode.data);
        }
    }
    
    public static void main(String[] args) {
        GraphNode a = new GraphNode(1);
        GraphNode b = new GraphNode(2);
        GraphNode c = new GraphNode(3);
        GraphNode d = new GraphNode(4);
        GraphNode e = new GraphNode(5);

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
