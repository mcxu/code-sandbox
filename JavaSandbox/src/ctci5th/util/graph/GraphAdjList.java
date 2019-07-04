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
        int targetRow1 = vertexExists(vtx1);
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
            e.printStackTrace();
        }
    }
    
    /**
     * Remove the LLNode with the indicated data.
     * @param data
     */
    public void removeVertex(Object data)
    {
        for(int row=0; row < adjList.size(); row++)
        {
            LLImpl list = adjList.get(row);
            
            if(list.head.data.equals(data)) 
            {
                //remove row where the data is the first item
                adjList.remove(row);
            }
            else
            {
                //remove instances of the data in the other rows.
                LLNode n = list.head;
                while(n != null)
                {
                    if(n.data.equals(data))
                    {
                        list.removeNode(n);
                    }
                    n = n.next;
                }
            }
        }
    }
    
    public int vertexExists(LLNode vtx)
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
    
    private static void testAddEdges()
    {
        GraphAdjList graph = new GraphAdjList();
        
        LLNode one = new LLNode(1);
        LLNode two = new LLNode(2);
        LLNode three = new LLNode(3);
        LLNode four = new LLNode(4);
        LLNode five = new LLNode(5);
        LLNode six = new LLNode("six");
        
        graph.addEdge(one, two);
        graph.addEdge(one, three);
        graph.addEdge(three, one);
        graph.addEdge(two, two);
        graph.addEdge(three, four);
        graph.addEdge(one, five);
        graph.addEdge(five, one);
        graph.addEdge(five, six);
        
        graph.printAdjList();
    }
    
    private static void testRemoveVertices()
    {
        GraphAdjList graph = new GraphAdjList();
        
        LLNode one = new LLNode(1);
        LLNode two = new LLNode(2);
        LLNode three = new LLNode(3);
        LLNode four = new LLNode(4);
        LLNode five = new LLNode(5);
        LLNode six = new LLNode("six");
        
        graph.addEdge(one, two);
        graph.addEdge(one, three);
        graph.addEdge(three, one);
        graph.addEdge(two, two);
        graph.addEdge(three, four);
        graph.addEdge(one, five);
        graph.addEdge(five, one);
        graph.addEdge(five, six);
        
        graph.printAdjList();
        
        Object dataToRemove = 2;
        System.out.println("removing: " + dataToRemove);
        graph.removeVertex(dataToRemove);
        
        graph.printAdjList();
    }
    
    public static void main(String[] args) 
    {
        //GraphAdjList.testAddEdges();
        GraphAdjList.testRemoveVertices();
        
    }
}
