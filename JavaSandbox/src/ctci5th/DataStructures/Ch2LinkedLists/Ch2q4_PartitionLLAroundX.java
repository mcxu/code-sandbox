/*
* Question 2.4: partition linked list such that all nodes less than
* x come before all nodes greater than or equal to x.
*/
package ctci5th.DataStructures.Ch2LinkedLists;

import ctci5th.util.list.LLNode;
import ctci5th.util.list.LLUtils;

public class Ch2q4_PartitionLLAroundX 
{
    public LLNode partitionLinkedList(LLNode head, int d)
    {   
        boolean headDataGTd = false; //head data greater than d
        if((int)head.data >= d)
        {
            headDataGTd = true;
        }
        
        LLNode head2 = null; //holds values >= d
        LLNode n = head; //first node (right pointer)
        int dCount = 0;
        while(n.next != null) 
        {
            System.out.println("=== n.data: " + n.data + " === n.next.data: " + n.next.data);
            System.out.print("curr list: "); 
            LLUtils.printLinkedList(head);
            if((int)n.next.data >= d)
            {
                System.out.println("found: " + n.next.data);
                
                if((int)n.next.data == d)
                {
                    dCount++;
                }
                else
                {
                    if(head2 == null)
                    {
                        head2 = new LLNode(n.next.data);
                    }
                    else
                    {
                        head2.appendToTail(n.next.data);
                    }
                }
                
                //remove element
                n.next = n.next.next;
            }
            else 
            {
                n = n.next;
            }
            System.out.print("after list: "); LLUtils.printLinkedList(head);
        }
        
        System.out.println("dCount: " + dCount);
        
        //add d to end of head for number of times d exists
        for(int i=0; i<dCount; i++)
        {
            head.appendToTail(d);
        }
        System.out.print("after append d: "); LLUtils.printLinkedList(head);
        
        //move head data to end of head list if needed
        if(headDataGTd == true)
        {
            n = head;
            while(n.next != null)
            {
                int temp = (int)n.next.data;
                n.next.data = n.data;
                n.data = temp;
                n = n.next;
            }
        }
        
        //add all elements but d from head2 to end of head
        n = head2;
        while(n != null)
        {
            if((int)n.data != d)
            {
                head.appendToTail(n.data);
            }
            n = n.next;
        }
        
        System.out.print("head: ");LLUtils.printLinkedList(head);
        System.out.print("head2: ");LLUtils.printLinkedList(head2);
        head2 = null; //delete secondary list
        System.out.print("head2 after null: ");LLUtils.printLinkedList(head2);
        return head;
    }
    
    public void test1()
    {
        LLNode head = new LLNode(12);
        head.appendToTail(12);
        head.appendToTail(5);
        head.appendToTail(1);
        head.appendToTail(8);
        head.appendToTail(-50);
        head.appendToTail(3);
        head.appendToTail(5);
        head.appendToTail(4);
        head.appendToTail(1);
        head.appendToTail(6);
        head.appendToTail(4);
        head.appendToTail(100);
        head.appendToTail(6);
        head.appendToTail(2);
        head.appendToTail(1);
        System.out.println("testQ2p4 before: ");
        LLUtils.printLinkedList(head);
        
        head = partitionLinkedList(head, 4);
        System.out.println("testQ2p4 after:");
        LLUtils.printLinkedList(head);
    }
    
    public static void main(String[] args) {
        Ch2q4_PartitionLLAroundX prob = new Ch2q4_PartitionLLAroundX();
        prob.test1();
    }

}
