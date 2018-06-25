package ctci5th.util.queue;

import ctci5th.util.list.Node;

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
            Object item = first.data;
            first = first.next;
            return item;
        }
        return -1000000;
    }

}
