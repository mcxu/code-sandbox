package ctci5th.util.stack;

import ctci5th.util.list.LLNode;

public class Stack 
{
    public LLNode top;
    
    Object pop()
    {
        if(top != null)
        {
            Object item = top.data;
            top = top.next;
            return item;
        }
        return null;
    }
    
    void push(int item)
    {
        LLNode t = new LLNode(item);
        t.next = top;
        top = t;
    }
    
    Object peek()
    {
        return top.data;
    }
}
