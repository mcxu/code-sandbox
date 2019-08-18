package ctci5th.util.stack;

import ctci5th.util.list.LLNode;

@SuppressWarnings("unchecked")
public class Stack<T>
{
    private LLNode top;
    
    public Stack() 
    {
    }
    
    public T pop()
    {
        if(top != null)
        {
            Object item = (T) top.data;
            top = top.next;
            return (T) item;
        }
        return null;
    }
    
    public void push(Object item)
    {
        LLNode t = new LLNode(item);
        t.next = top;
        top = t;
    }
    
    public T peek()
    {
        return (T) top.data;
    }
    
    public LLNode peekNode()
    {
        return top;
    }
    
    public boolean isEmpty()
    {
        if(top == null) {
            return true;
        }
        return false;
    }
}
