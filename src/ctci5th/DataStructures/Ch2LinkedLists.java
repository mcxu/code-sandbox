package ctci5th.DataStructures;

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
                    System.out.println("    duplicate: " + n.next.data);
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
    
    
    
    ////////////// helpers ///////////////
    
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
    
    Node deleteNode(Node head, int d) 
    {
        Node n = head;
        
        if(n.data == d) 
        {
            return head.next;
        }
        
        while(n.next != null)
        {
            if(n.next.data == d)
            {
                n.next = n.next.next;
                return head;
            }
            n = n.next;
        }
        
        return head;
    }
    
    public static void main(String[] args) 
    {
        Ch2LinkedLists ch2 = new Ch2LinkedLists();
        //ch2.testQ2p1();
        ch2.testQ2p2();
    }

}

//Node class for linked list
class Node {
    Node next = null;
    int data;
    
    public Node(int d)
    {
        data = d;   
    }
    
    void appendToTail(int d)
    {
        Node end = new Node(d);
        Node n = this;
        while(n.next != null)
        {
            n = n.next;
        }
        n.next = end;
    }
}