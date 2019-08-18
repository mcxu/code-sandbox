package ctci5th.util.queue;

import ctci5th.util.list.LLNode;
import ctci5th.util.stack.Stack;

/**
 * Question 3.5: Queue using 2 stacks
 */
public class MyQueue 
{
    private Stack inStack;
    private Stack outStack;
    
    public MyQueue()
    {
        inStack = new Stack();
        outStack = new Stack();
    }
    
    public void enqueue(Object item)
    {
        inStack.push(item);
    }
    
    public Object dequeue()
    {
        while(!inStack.isEmpty()) {
            outStack.push(inStack.pop());
        }
            
        return outStack.pop();
    }
    
    private void printInStack()
    {
        LLNode printHeadIn = inStack.peekNode();
        while(printHeadIn != null) {
            System.out.println("printHeadIn: " + printHeadIn.data);
            printHeadIn = printHeadIn.next;
        }
    }
    
    private void printOutStack()
    {
        LLNode printHeadOut = outStack.peekNode();
        while(printHeadOut != null) {
            System.out.println("printHeadOut: " + printHeadOut.data);
            printHeadOut = printHeadOut.next;
        }
    }
    
    public static void main(String[] args) 
    {
        MyQueue mq = new MyQueue();
        mq.enqueue(0);
        mq.enqueue(1);
        mq.enqueue(2);
        mq.enqueue(3);
        mq.printInStack();
        mq.printOutStack();
        
        Object a = mq.dequeue();
        System.out.println("dequeued: " + a);
        mq.printInStack();
        mq.printOutStack();
        
        Object b = mq.dequeue();
        System.out.println("dequeued: " + b);
    }

}
