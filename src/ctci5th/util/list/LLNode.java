package ctci5th.util.list;

//Node class for linked list
public class LLNode 
{
    public LLNode next = null;
    public Object data;
    public boolean visited = false;
    
    public LLNode(Object data)
    {
        this.data = data;
    }
    
    public void appendToTail(Object d)
    {
        LLNode end = new LLNode(d);
        LLNode n = this;
        while(n.next != null)
        {
            n = n.next;
        }
        n.next = end;
    }
}