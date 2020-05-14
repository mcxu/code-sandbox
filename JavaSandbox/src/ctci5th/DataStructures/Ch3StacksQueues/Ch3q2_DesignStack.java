package ctci5th.DataStructures.Ch3StacksQueues;

import ctci5th.util.list.LLNode;

/**
 * Question 3.2: Stack which also returns min element in O(1) time.
 * @author MichaelXu
 *
 */
public class Ch3q2_DesignStack
{
    public LLNode top;
    private LLNode minNode;
    
    Object pop()
    {
        if(top != null)
        {
            if(top == minNode)
            {
                System.out.println("match found: top=" + top + "   minNode=" + minNode);
                LLNode n = top.next;
                minNode = n;
                while(n != null)
                {
                    System.out.println("n.data: " + n.data);
                    
                    if((int)n.data <= (int)minNode.data)
                    {
                        minNode = n;
                    }
                    
                    n = n.next;
                }
                System.out.println("minNode after pop: " + minNode.data);
            }
            
            int item = (int)top.data;
            top = top.next;
            return item;
        }
        return null;
    }
    
    void push(int item)
    {
        LLNode t = new LLNode(item);
        System.out.println("curr top: " + top);
        System.out.println("t data: " + t.data);
        if((top == null) || ((int)t.data < (int)minNode.data))
        {
            minNode = t;
        }
        
        t.next = top;
        top = t;
        System.out.println("top: " + top.data);
        System.out.println("minNode: " + minNode.data);
    }
    
    LLNode min()
    {
        return minNode;
    }
    
    void printStack()
    {
        LLNode n = top;
        while(n != null)
        {
            System.out.print(n.data + ", ");
            n = n.next;
        }
        System.out.print("\n");
    }
    
    public static void main(String[] args) {
        Ch3q2_DesignStack stack = new Ch3q2_DesignStack();
        stack.push(3);
        stack.push(1);
        stack.push(5);
        stack.push(0);
        stack.push(2);
        stack.push(4);
        System.out.print("stack: "); stack.printStack();
        
        System.out.println("=== popping ===");
        System.out.println("pop1: " + stack.pop());
        System.out.print("stack after pop1: "); stack.printStack();
        System.out.println("pop2: " + stack.pop());
        System.out.println("pop3: " + stack.pop());
        System.out.println("pop4: " + stack.pop());
        System.out.println("pop5: " + stack.pop());
        System.out.println("minNode is: " + stack.min().data);
    }

}
