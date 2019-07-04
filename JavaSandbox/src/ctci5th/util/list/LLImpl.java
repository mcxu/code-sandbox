package ctci5th.util.list;

/**
 * Linked list encapsulated in a class.
 * @author MichaelXu
 *
 */
public class LLImpl 
{
    public final LLNode head;
    private LLNode tail;
    
    public LLImpl(LLNode head)
    {
        this.head = head;
        this.tail = head;
    }
    
    public void appendToTail(LLNode llNode)
    {
        LLNode n = head;
        while(n.next != null)
        {
            n = n.next;
        }
        n.next = llNode;
        
        this.tail = llNode; //update tail
    }
    
    public void removeNode(LLNode llNode)
    {
        LLNode n = this.head;
        while(n.next != null)
        {
            if(n.next.data.equals(llNode.data))
            {
                n.next = n.next.next;
            }
            else
            {
                n = n.next;
            }
        }
    }
    
    public LLNode getTail()
    {
        LLNode n = this.head;
        while(n.next != null)
        {
            n = n.next;
        }
        this.tail = n;
        return this.tail;
    }
    
    public int length()
    {
        int len = 0;
        LLNode n  = this.head;
        while(n != null)
        {
            len++;
            n = n.next;
        }
        return len;
    }
    
    public void print()
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
        LLImpl list1 = new LLImpl(new LLNode(3));
        list1.appendToTail(new LLNode(4));
        list1.appendToTail(new LLNode(45));
        list1.appendToTail(new LLNode(8));
        list1.appendToTail(new LLNode(9));
        
        list1.print();
        System.out.println("list1 head: " + list1.head.data);
        System.out.println("list1 tail: " + list1.getTail().data);
        System.out.println("list1 length: " + list1.length());
    }

}
