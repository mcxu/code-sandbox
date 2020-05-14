/**
 * Question 2.2: find kth to last element of singly linked list.
 */
package ctci5th.DataStructures.Ch2LinkedLists;
import ctci5th.util.list.LLNode;
import ctci5th.util.list.LLUtils;

public class Ch2q2_KthToLastInLL 
{
    public int getKthToLastElement(LLNode head, int k)
    {
        int j = LLUtils.getLinkedListLength(head) - k;
        int i= 0;
        LLNode n = head;
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
    
    public void test1()
    {
        LLNode head = new LLNode(1);
        head.appendToTail(2);
        head.appendToTail(3);
        head.appendToTail(4);
        head.appendToTail(5);
        head.appendToTail(6);
        
        int len = LLUtils.getLinkedListLength(head);
        System.out.println("len: " + len);
        
        int kthToLast = getKthToLastElement(head, 4);
        System.out.println("kthToLast: " + kthToLast);
    }
    
    public static void main(String[] args)
    {
        Ch2q2_KthToLastInLL prob = new Ch2q2_KthToLastInLL();
        prob.test1();
    }
}