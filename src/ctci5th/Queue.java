package ctci5th;

public class Queue 
{
    public Node first, last;
    
    public void enqueue(int item)
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
    
    public int dequeue()
    {
        if(first != null)
        {
            int item = first.data;
            first = first.next;
            return item;
        }
        return -1000000;
    }

}
