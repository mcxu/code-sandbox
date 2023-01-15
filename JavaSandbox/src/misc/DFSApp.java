// https://thecodingsimplified.com/depth-first-search-dfs-on-graph-with-implementation/
package misc;

import java.util.Stack;

class Vertex {
  public char label;
  public boolean wasVisited;
  
  public Vertex(char lab) {
    label = lab;
    wasVisited = false;
  }
}

class Graph {

    private final int MAX_VERTS = 20;
    private Vertex vertexList[];
    private int adjMat[][];
    private int nVerts;
    private Stack<Integer> s;

    public Graph() {
        vertexList = new Vertex[MAX_VERTS];
        adjMat = new int[MAX_VERTS][MAX_VERTS];
        nVerts = 0;
        s = new Stack<Integer>();
    }

    public void addVertex(char lab) {
        vertexList[nVerts++] = new Vertex(lab);
    }

    public void addEdge(int start, int end) {
        adjMat[start][end] = 1;
        adjMat[end][start] = 1;
    }

    public void displayVertex(int v) {
        System.out.println(vertexList[v].label + " ");
    }

    public int getAdjUnvisitedVertex (int v) {
        for(int j = 0; j < nVerts; j++) {
            if(adjMat[v][j] == 1 && vertexList[j].wasVisited == false) {
                return j;
            }
        }
        return -1;
    }

    public void dfs() {
        vertexList[0].wasVisited = true;
        displayVertex(0);
        s.push(0);

        while(!s.isEmpty()) {    
            int v = getAdjUnvisitedVertex(s.peek());
            System.out.println("v: " + v + " stack: " + s);
            if(v == -1) {
                s.pop();
            } else {
                vertexList[v].wasVisited = true;
                displayVertex(v);
                s.push(v);
            }
        }
    }
}

public class DFSApp {
    public static void main(String[] args) {
        Graph theGraph = new Graph();
        theGraph.addVertex('A');
        theGraph.addVertex('B');
        theGraph.addVertex('C');
        theGraph.addVertex('D');
        theGraph.addVertex('E');
        theGraph.addVertex('F');

        theGraph.addEdge(0, 1);
        theGraph.addEdge(1, 2);
        theGraph.addEdge(0, 3);
        theGraph.addEdge(3, 4);
        theGraph.addEdge(4, 5);
        theGraph.addEdge(1, 3);

        System.out.println("Visits: ");
        theGraph.dfs();
        System.out.println();
    }
}