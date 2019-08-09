package ctci5th.util.stack;

import ctci5th.util.list.LLNode;

public class Stack 
{
    public LLNode top;
    
    public Object pop()
    {
        if(top != null)
        {
            Object item = top.data;
            top = top.next;
            return item;
        }
        return null;
    }
    
    public void push(Object item)
    {
        LLNode t = new LLNode(item);
        t.next = top;
        top = t;
    }
    
    public Object peek()
    {
        return top.data;
    }
}
