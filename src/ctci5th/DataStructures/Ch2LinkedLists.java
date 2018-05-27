package ctci5th.DataStructures;

import java.util.ArrayList;
import java.util.List;

import ctci5th.Node;

/**
 * Linked Lists
 * Book pg. 75. PDF pg. 84
 * @author MichaelXu
 */
public class Ch2LinkedLists 
{
    /**
     * Question 2.1: Remove duplicates from unsorted linked list
     * @param head head of the linked list
     * @return
     */
    public Node removeDuplicates(Node head)
    {
        System.out.print("entered removeDuplicates. ");
        
        Node k = head; //for every element, go through n
        Node n = k; //single iteration through whole list
        
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
    
    public void testQ2p1()
    {
        //create linked list
        Node head = new Node(1);
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
        
        Node result = removeDuplicates(head);
        System.out.println("linked list with duplicates removed:");
        printLinkedList(result);
    }
    
    /**
     * Question 2.2: find kth to last element of singly linked list.
     * @param head
     * @param k
     * @return
     */
    public int getKthToLastElement(Node head, int k)
    {
        int j = getLinkedListLength(head) - k;
        int i= 0;
        Node n = head;
        while(n.next != null)
        {
            if(i == j) {
                return n.data;
            }
            n = n.next;
            i++;
        }
        return n.data;
    }
    
    public void testQ2p2()
    {
        Node head = new Node(1);
        head.appendToTail(2);
        head.appendToTail(3);
        head.appendToTail(4);
        head.appendToTail(5);
        head.appendToTail(6);
        
        int len = getLinkedListLength(head);
        System.out.println("len: " + len);
        
        int kthToLast = getKthToLastElement(head, 4);
        System.out.println("kthToLast: " + kthToLast);
    }
    
    /**
     * Question 2.3: Delete node in middle of singly linked list.
     * @param head
     * @param d
     */
    public void deleteNodeInMiddle(Node head, int d)
    {
        Node n = head;
        while(n.next != null)
        {
            if(n.next.data == d)
            {
                n.next = n.next.next;
            }
            else
            {
                n = n.next;
            }
        }
    }
    
    public void testQ2p3()
    {
        Node head = new Node(1);
        head.appendToTail(2);
        head.appendToTail(3);
        head.appendToTail(4);
        head.appendToTail(5);
        head.appendToTail(6);
        
        System.out.println("before delete");
        printLinkedList(head);
        
        deleteNodeInMiddle(head, 3);
        System.out.println("after delete");
        printLinkedList(head);
    }
    
    /**
     * Question 2.4: partition linked list such that all nodes less than
     * x come before all nodes greater than or equal to x.
     * @param head
     * @param d
     * @return
     */
    public Node partitionLinkedList(Node head, int d)
    {   
        Node GEdList = null; //holds values >= d
        
        Node n = head; //first node (right pointer)
        while(n != null) 
        {
            System.out.println("curr n.data: " + n.data);
            
            if(n.data >= d)
            {
                if(GEdList == null)
                {
                    GEdList = new Node(n.data);
                }
                else
                {
                    GEdList.appendToTail(n.data);
                }
                //remove the element from the head list
                deleteNodeInMiddle(head, n.data);
            }
            n = n.next;
        }
        
        //add d to end of head
        head.appendToTail(d);
        
        //add all elements but d from GEdList to end of head
        n = GEdList;
        while(n != null)
        {
            if(n.data != d)
            {
                head.appendToTail(n.data);
            }
            n = n.next;
        }
        
        System.out.print("head: ");printLinkedList(head);
        System.out.print("GEdList: ");printLinkedList(GEdList);
        GEdList = null; //delete GEdList
        System.out.print("GEdList after null: ");printLinkedList(GEdList);
        return head;
    }
    
    public void testQ2p4()
    {
        Node head = new Node(1);
        head.appendToTail(8);
        head.appendToTail(3);
        head.appendToTail(5);
        head.appendToTail(4);
        head.appendToTail(6);
        head.appendToTail(2);
        
        head = partitionLinkedList(head, 2);
        System.out.println("testQ2p4:");
        printLinkedList(head);
    }
    
    /**
     * Write a function that adds the two numbers and returns the sum 
     * as a linked list.
     * @param head1
     * @param head2
     * @param direction "f" if linked list values in forward order, "r" in reverse.
     * @return
     */
    public Node addLinkedListNums(Node head1, Node head2, String direction)
    {
        String str1 = "";
        Node n1 = head1;
        while(n1 != null)
        {
            if(direction.equals("r"))
                str1 = n1.data + str1;
            else if(direction.equals("f"))
                str1 = str1 + n1.data;
            n1 = n1.next;
        }
        System.out.println("str1: " + str1);
        
        String str2 = "";
        Node n2 = head2;
        while(n2 != null)
        {
            if(direction.equals("r"))
                str2 = n2.data + str2;
            else if(direction.equals("f"))
                str2 = str2 + n2.data;
            n2 = n2.next;
        }
        System.out.println("str2: " + str2);
        
        //sum
        int sum = Integer.parseInt(str1) + Integer.parseInt(str2);
        System.out.println("sum= " + sum);
        
        //create linked list for sum
        Node sumValuesList = null;
        String sumStr = Integer.toString(sum);
        for(int i=0; i < sumStr.length(); i++)
        {
            String chStr = Character.toString(sumStr.charAt(i));
            int val = Integer.parseInt(chStr);
            
            if(sumValuesList == null)
            {
               sumValuesList = new Node(val);
            }
            else
            {
                sumValuesList.appendToTail(val);
            }
        }
        
        return sumValuesList;
    }
    
    public void testQ2p5()
    {
        Node head1 = new Node(1);
        head1.appendToTail(8);
        head1.appendToTail(3);
        
        Node head2 = new Node(0);
        head2.appendToTail(0);
        head2.appendToTail(1);
        
        Node sumValuesList = addLinkedListNums(head1, head2, "r");
        System.out.println("sumValuesList: ");
        printLinkedList(sumValuesList);
    }
    
    ////////////// helpers ///////////////
    
    public int getDataFromLinkedList(Node head, int index)
    {
        Node n = head;
        int j = 0;
        try
        {
            while(n.next != null && j<index)
            {
                j++;
                n = n.next;
            }
        }
        catch(NullPointerException ex)
        {
            System.out.println("n pointer is null.");
            ex.printStackTrace();
        }
        return n.data;
    }
    
    public void test_getDataFromLinkedList()
    {
        Node head = new Node(1);
        head.appendToTail(8);
        head.appendToTail(3);
        head.appendToTail(5);
        head.appendToTail(4);
        head.appendToTail(6);
        head.appendToTail(2);
        
        int data = getDataFromLinkedList(head, 3);
        System.out.println("data: " + data);
    }
    
    public int getLinkedListLength(Node head)
    {
        Node n = head;
        int i = 0;
        while(n != null)
        {
            n = n.next;
            i++;
        }
        return i;
    }
    
    void printLinkedList(Node head)
    {
        Node n = head;
        String llStr = "";
        while(n != null) 
        {
            llStr = llStr + n.data + ", ";
            n = n.next;
        }
        if(llStr.endsWith(", "))
        {
            llStr = llStr.substring(0, llStr.length()-2);
        }
        System.out.println(llStr);
    }
    
//    Node deleteNode(Node head, int d) 
//    {
//        Node n = head;
//        
//        if(n.data == d) 
//        {
//            return head.next;
//        }
//        
//        while(n.next != null)
//        {
//            if(n.next.data == d)
//            {
//                n.next = n.next.next;
//                return head;
//            }
//            n = n.next;
//        }
//        
//        return head;
//    }
    
    
    public static void main(String[] args) 
    {
        Ch2LinkedLists ch2 = new Ch2LinkedLists();
        //ch2.testQ2p1();
        //ch2.testQ2p2();
        //ch2.testQ2p3();
        //ch2.test_getDataFromLinkedList();
        //ch2.testQ2p4();
        ch2.testQ2p5();
    }

}
