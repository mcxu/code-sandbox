package ctci5th;

public class Queue 
{
    public Node first, last;
    
    public void enqueue(Object item)
    {
        if(first == null)
        {
            last = new Node(item);
            first = last;
        }
        else
        {
            last.next = new Node(item);
            last = last.next;
        }
    }
    
    public Object dequeue()
    {
        if(first != null)
        {
            Object item = first.dataObj;
            first = first.next;
            return item;
        }
        return null;
    }

}
