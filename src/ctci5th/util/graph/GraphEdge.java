package ctci5th.util.graph;

import ctci5th.util.graph.GraphVertex;

public class GraphEdge 
{
    public GraphVertex v1;
    public GraphVertex v2;
    
    /**
     * Convention: v1 points to v2. For undirected graph, need both directions.
     * @param v1
     * @param v2
     */
    public GraphEdge(GraphVertex v1, GraphVertex v2)
    {
        this.v1 = v1;
        this.v2 = v2;
    }
    
    public static void main(String[] args) 
    {
        GraphEdge edge1 = new GraphEdge(new GraphVertex(32), new GraphVertex(64));
        System.out.println("edge1: " + edge1);
        System.out.println("edge1.v1: " + edge1.v1.data);
        System.out.println("edge1.v2: " + edge1.v2.data);
    }

}
