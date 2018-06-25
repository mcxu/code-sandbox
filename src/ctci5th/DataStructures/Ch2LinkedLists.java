package ctci5th.DataStructures;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import ctci5th.util.list.Node;

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
                return (int)n.data;
            }
            n = n.next;
            i++;
        }
        return (int)n.data;
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
        boolean headDataGTd = false; //head data greater than d
        if((int)head.data >= d)
        {
            headDataGTd = true;
        }
        
        Node head2 = null; //holds values >= d
        Node n = head; //first node (right pointer)
        int dCount = 0;
        while(n.next != null) 
        {
            System.out.println("=== n.data: " + n.data + " === n.next.data: " + n.next.data);
            System.out.print("curr list: "); printLinkedList(head);
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
                        head2 = new Node(n.next.data);
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
            System.out.print("after list: "); printLinkedList(head);
        }
        
        System.out.println("dCount: " + dCount);
        
        //add d to end of head for number of times d exists
        for(int i=0; i<dCount; i++)
        {
            head.appendToTail(d);
        }
        System.out.print("after append d: "); printLinkedList(head);
        
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
        
        System.out.print("head: ");printLinkedList(head);
        System.out.print("head2: ");printLinkedList(head2);
        head2 = null; //delete secondary list
        System.out.print("head2 after null: ");printLinkedList(head2);
        return head;
    }
    
    public void testQ2p4()
    {
        Node head = new Node(12);
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
        printLinkedList(head);
        
        head = partitionLinkedList(head, 4);
        System.out.println("testQ2p4 after:");
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
    
    public Node getFirstLoopNodeInCircularLinkedList(Node head)
    {
        Map<Integer, Node> nodeMap = new HashMap<>(); 
        
        Node n = head;
        
        while(n != null)
        {
            System.out.println("n.data=" + n.data + "  addr: " + n);
            
            if(nodeMap.containsKey(n.data))
            {
                Node k = nodeMap.get(n.data);
                if(k == n)
                {
                    nodeMap = null;
                    return n;
                }
            }
            else
            {
                nodeMap.put((int)n.data, n);
            }
            
            n = n.next;
            try {
                Thread.sleep(500);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        nodeMap = null;
        return n;
    }
    
    public void testQ2p6()
    {
        Node a = new Node(1);
        Node b = new Node(2);
        a.next = b;
        Node c = new Node(3);
        b.next = c;
        Node d = new Node(4);
        c.next = d;
        Node e = new Node(5);
        d.next = e;
        e.next = c;
        
        //printLinkedList(a);
        Node fln = getFirstLoopNodeInCircularLinkedList(a);
        System.out.println("fln: " + fln);
        System.out.println("fln data: " + fln.data);
    }
    
    
    public boolean isPalindrome(Node head)
    {
        int llLen = getLinkedListLength(head);
        
        //check if odd length
        int countFrom = 0;
        if(llLen % 2 == 0)
        {
            countFrom = llLen/2; //even
        }
        else
        {
            countFrom = llLen/2 + 1; //odd
        }
        
        String former = "";
        String latter = "";
        
        int i = 0;
        
        Node n = head;
        while(n != null)
        {
            //System.out.print("i=" + i);
            
            if(i < llLen/2)
            {
                //System.out.println(" in if: " + n.data);
                former = former + n.data + ",";
            }
            else
            {
                //System.out.println(" in else: " + n.data);
                if(i >= countFrom)
                {
                    System.out.println("i>=CF: " + i);
                    latter = n.data + "," + latter ;
                }
            }
            
            i++;
            n = n.next;
        }
        
        System.out.println("former: " + former);
        System.out.println("latter: " + latter);
        
        if(former.equals(latter))
        {
            return true;
        }
        
        return false;
    }
    
    public void testQ2p7()
    {
        Node head = new Node(0);
        head.appendToTail(1);
        head.appendToTail(2);
        head.appendToTail(3);
        head.appendToTail(4);
        head.appendToTail(3);
        head.appendToTail(2);
        head.appendToTail(1);
        head.appendToTail(0);
        
        boolean isPal = isPalindrome(head);
        System.out.println("isPal: " + isPal);
        
        Node head2 = new Node(0);
        head2.appendToTail(1);
        head2.appendToTail(2);
        head2.appendToTail(3);
        head2.appendToTail(0);
        head2.appendToTail(2);
        head2.appendToTail(2);
        head2.appendToTail(1);
        head2.appendToTail(0);
        
        isPal = isPalindrome(head2);
        System.out.println("isPal: " + isPal);
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
        return (int)n.data;
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
        while(n != null) 
        {
            String element = n.data + ", ";
            System.out.print(element);
            n = n.next;
        }
        System.out.print("\n");
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
        //ch2.testQ2p5();
        //ch2.testQ2p6();
        ch2.testQ2p7();
    }

}
