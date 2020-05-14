/**
You have two numbers represented by a linked list, where each node contains a
single digit. The digits are stored in reverse order, such that the Ts digit is at the
head of the list. Write a function that adds the two numbers and returns the sum
as a linked list.
EXAMPLE
Input: (7-> 1 -> 6) + (5 -> 9 -> 2).That is, 617 + 295.
Output: 2 -> 1 -> 9.That is, 912.
 */
package ctci5th.DataStructures.Ch2LinkedLists;

import ctci5th.util.list.LLNode;
import ctci5th.util.list.LLUtils;

public class Ch2q5_Sum2LLElementWise 
{
    public LLNode addLinkedListNums(LLNode head1, LLNode head2, String direction)
    {
        String str1 = "";
        LLNode n1 = head1;
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
        LLNode n2 = head2;
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
        LLNode sumValuesList = null;
        String sumStr = Integer.toString(sum);
        for(int i=0; i < sumStr.length(); i++)
        {
            String chStr = Character.toString(sumStr.charAt(i));
            int val = Integer.parseInt(chStr);
            
            if(sumValuesList == null)
            {
               sumValuesList = new LLNode(val);
            }
            else
            {
                sumValuesList.appendToTail(val);
            }
        }
        
        return sumValuesList;
    }
    
    public void test1()
    {
        LLNode head1 = new LLNode(1);
        head1.appendToTail(8);
        head1.appendToTail(3);
        
        LLNode head2 = new LLNode(0);
        head2.appendToTail(0);
        head2.appendToTail(1);
        
        LLNode sumValuesList = addLinkedListNums(head1, head2, "r");
        System.out.println("sumValuesList: ");
        LLUtils.printLinkedList(sumValuesList);
    }
    
    public static void main(String[] args) 
    {
        Ch2q5_Sum2LLElementWise prob = new Ch2q5_Sum2LLElementWise();
        prob.test1();
    }

}
