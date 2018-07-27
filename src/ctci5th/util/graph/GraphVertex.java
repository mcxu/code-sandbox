package ctci5th.util.graph;

import java.util.HashSet;
import java.util.Iterator;
import java.util.Set;

/**
 * Graph Node
 * @author MichaelXu
 *
 */
public class GraphVertex
{
    public Object data;
    public boolean visited;
    
    public GraphVertex(Object data)
    {
        this.data = data;
        visited = true;
    }
}
