package ctci5th.DataStructures.Ch2LinkedLists;

import ctci5th.util.list.LLNode;
import ctci5th.util.list.LLUtils;

public class Ch2q7_IsLLPalindrome 
{
    public boolean isPalindrome(LLNode head)
    {
        int llLen = LLUtils.getLinkedListLength(head);
        
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
        
        LLNode n = head;
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
    
    public void test1()
    {
        LLNode head = new LLNode(0);
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
        
        LLNode head2 = new LLNode(0);
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
    public static void main(String[] args) {
        Ch2q7_IsLLPalindrome prob = new Ch2q7_IsLLPalindrome();
        prob.test1();
    }

}
