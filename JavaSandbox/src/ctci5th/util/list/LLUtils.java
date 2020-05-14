package ctci5th.util.list;

public class LLUtils 
{
    public static int getLinkedListLength(LLNode head)
    {
        LLNode n = head;
        int i = 0;
        while(n != null)
        {
            n = n.next;
            i++;
        }
        return i;
    }
    
    public static void printLinkedList(LLNode head)
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
    
    public LLNode quickSortLinkedList(LLNode head)
    {
        //TODO
        
        return head;
    }
    
    public void test_sortLinkedList()
    {
        LLNode head = new LLNode(1);
        head.appendToTail(2);
        head.appendToTail(3);
        head.appendToTail(4);
        head.appendToTail(5);
        head.appendToTail(6);
    }
    
    public static void main(String[] args) {
        // TODO Auto-generated method stub

    }

}
