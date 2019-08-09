package ctci5th.util.queue;

import ctci5th.util.list.LLNode;

public class Queue 
{
    public LLNode first, last;
    
    public void enqueue(Object item)
    {
        if(first == null)
        {
            last = new LLNode(item);
            first = last;
        }
        else
        {
            last.next = new LLNode(item);
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
        return null;
    }

}
