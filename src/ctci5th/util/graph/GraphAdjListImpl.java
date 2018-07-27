package ctci5th.util.graph;

import java.util.ArrayList;
import java.util.HashMap;

import ctci5th.util.list.LLImpl;
import ctci5th.util.list.LLNode;

/**
 * Directed graph in adjacency list representation
 */
public class GraphAdjListImpl 
{
    private ArrayList<LLImpl> adjList;
    
    /**
     * Takes the chosen node in a graph
     * @param node
     */
    public GraphAdjListImpl()
    {
        adjList = new ArrayList<LLImpl>();
    }
    
    public void addVertex(LLNode vertex)
    {
        for(LLImpl list : adjList)
        {
            if(vertex == list.head)
            {
                return;
            }
        }
        adjList.add(new LLImpl(vertex));
    }
    
    public boolean checkVertexExists(LLNode vertex)
    {
        for(LLImpl list : adjList)
        {
            if(vertex == list.head)
            {
                return true;
            }
        }
        return false;
    }
    
    public static void main(String[] args) 
    {
        GraphAdjListImpl graphAL = new GraphAdjListImpl();
        LLNode a = new LLNode(1);
        graphAL.addVertex(a);
        boolean exist = graphAL.checkVertexExists(a);
        System.out.println("exist: " + exist);
    }

}
