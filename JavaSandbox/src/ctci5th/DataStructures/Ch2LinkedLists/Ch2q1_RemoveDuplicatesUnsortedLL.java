/*
Question 2.1: Remove duplicates from unsorted linked list
*/
package ctci5th.DataStructures.Ch2LinkedLists;
import ctci5th.util.list.LLNode;

public class Ch2q1_RemoveDuplicatesUnsortedLL
{
    public LLNode removeDuplicates(LLNode head)
    {
        System.out.print("entered removeDuplicates. ");
        
        LLNode k = head; //for every element, go through n
        LLNode n = k; //single iteration through whole list
        
        System.out.println("head.data: " + head.data);
        while(k.next != null)
        {
            System.out.print("starting with: "); printLinkedList(head);
            System.out.println("k.data= " + k.data);
            while(n.next != null)
            {   
                System.out.println("  n.data= " + n.data);
                if(n.next.data == k.data)
                {
                    n.next = n.next.next; //remove the duplicate
                } 
                else
                {
                    n = n.next;
                }
            }
            
            if(k.next == null)
            {
                return head;
            }
            
            k = k.next;
            n = k;
        }
        return head;
    }
    
    public void test1()
    {
        //create linked list
        LLNode head = new LLNode(1);
        head.appendToTail(2);
        head.appendToTail(3);
        head.appendToTail(6);
        head.appendToTail(4);
        head.appendToTail(4);
        head.appendToTail(3);
        head.appendToTail(5);
        head.appendToTail(6);
        head.appendToTail(7);
        head.appendToTail(7);
        head.appendToTail(7);
        head.appendToTail(8);
        head.appendToTail(9);
        head.appendToTail(10);
        
        printLinkedList(head);
        
        LLNode result = removeDuplicates(head);
        System.out.println("linked list with duplicates removed:");
        printLinkedList(result);
    }

    void printLinkedList(LLNode head)
    {
        LLNode n = head;
        while(n != null) 
        {
            String element = n.data + ", ";
            System.out.print(element);
            n = n.next;
        }
        System.out.print("\n");
    }

    public static void main(String[] args)
    {
        Ch2q1_RemoveDuplicatesUnsortedLL prob = new Ch2q1_RemoveDuplicatesUnsortedLL();
        prob.test1();
    }
}
