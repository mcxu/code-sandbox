package ctci5th.DataStructures.Ch2LinkedLists;

import ctci5th.util.list.LLNode;
import ctci5th.util.list.LLUtils;

public class Ch2q3_DeleteNodeInMiddleOfLL 
{
    public void deleteNodeInMiddle(LLNode head, int d)
    {
        LLNode n = head;
        while(n.next != null)
        {
            if((int)n.next.data == d)
            {
                n.next = n.next.next;
            }
            else
            {
                n = n.next;
            }
        }
    }
    
    public void test1()
    {
        LLNode head = new LLNode(1);
        head.appendToTail(2);
        head.appendToTail(3);
        head.appendToTail(4);
        head.appendToTail(5);
        head.appendToTail(6);
        
        System.out.println("before delete");
        LLUtils.printLinkedList(head);
        
        deleteNodeInMiddle(head, 6);
        System.out.println("after delete");
        LLUtils.printLinkedList(head);
    }
    
    public static void main(String[] args) {
        Ch2q3_DeleteNodeInMiddleOfLL prob = new Ch2q3_DeleteNodeInMiddleOfLL();
        prob.test1();

    }

}
