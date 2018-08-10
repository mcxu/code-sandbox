package ctci5th.util.graph;

import java.util.ArrayList;
import java.util.HashMap;

import ctci5th.util.list.LLImpl;
import ctci5th.util.list.LLNode;

/**
 * Directed graph in adjacency list representation
 */
public class GraphAdjList 
{
    private ArrayList<LLImpl> adjList;
    
    /**
     * Takes the chosen node in a graph
     * @param node
     */
    public GraphAdjList()
    {
        adjList = new ArrayList<LLImpl>();
    }
    
    public void addEdge(LLNode vtx1, LLNode vtx2)
    {
        int targetRow1 = vtxExists(vtx1);
        System.out.print("targetRow1: " + targetRow1 + "  ");
        
        if(targetRow1 >= 0)
        {
            System.out.println("A");
            //vertex 1 already exists, add vertex 2 to end of list where vertex 1 is head.
            adjList.get(targetRow1).appendToTail(new LLNode(vtx2.data));
        }
        else
        {
            System.out.println("B");
            //add new head (vertex 1) and append vertex 2
            adjList.add(new LLImpl(vtx1));
            adjList.get(adjList.size()-1).appendToTail(new LLNode(vtx2.data));
        }
        
        try {
            Thread.sleep(500);
        } catch (InterruptedException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
    }
    
    public int vtxExists(LLNode vtx)
    {
        for(int row=0; row < adjList.size(); row++)
        {
            LLImpl list = adjList.get(row);
            
            if(vtx == list.head)
            {
                return row;
            }
        }
        return -1;
    }
    
    public void printAdjList()
    {
        
        for(int i=0; i < adjList.size(); i++)
        {   
            LLImpl llImpl = adjList.get(i);
            System.out.print("list addr: " + llImpl + "   values:  ");
            llImpl.print();
        }
    }
    
    public static void main(String[] args) 
    {
        GraphAdjList graph = new GraphAdjList();
        
        LLNode one = new LLNode(1);
        LLNode two = new LLNode(2);
        LLNode three = new LLNode(3);
        LLNode four = new LLNode(4);
        LLNode five = new LLNode(5);
        
        graph.addEdge(one, two);
        graph.addEdge(one, three);
        graph.addEdge(three, one);
        graph.addEdge(two, two);
        graph.addEdge(three, four);
        graph.addEdge(one, five);
        graph.addEdge(five, one);
        
        graph.printAdjList();
        
    }
}
