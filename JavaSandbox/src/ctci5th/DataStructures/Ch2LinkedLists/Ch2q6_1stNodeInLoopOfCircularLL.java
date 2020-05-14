/*
Given a circular linked list, implement an algorithm which returns the node at
the beginning of the loop.
 */
package ctci5th.DataStructures.Ch2LinkedLists;

import java.util.HashMap;
import java.util.Map;
import ctci5th.util.list.LLNode;

public class Ch2q6_1stNodeInLoopOfCircularLL 
{
    public LLNode getFirstLoopNodeInCircularLinkedList(LLNode head)
    {
        Map<Integer, LLNode> nodeMap = new HashMap<>(); 
        
        LLNode n = head;
        
        while(n != null)
        {
            System.out.println("n.data=" + n.data + "  addr: " + n);
            
            if(nodeMap.containsKey(n.data))
            {
                LLNode k = nodeMap.get(n.data);
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
                Thread.sleep(500); //Test
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        nodeMap = null;
        return n;
    }
    
    public void test1()
    {
        LLNode a = new LLNode(1);
        LLNode b = new LLNode(2);
        a.next = b;
        LLNode c = new LLNode(3);
        b.next = c;
        LLNode d = new LLNode(4);
        c.next = d;
        LLNode e = new LLNode(5);
        d.next = e;
        e.next = c;
        
        //printLinkedList(a);
        LLNode fln = getFirstLoopNodeInCircularLinkedList(a);
        System.out.println("fln: " + fln);
        System.out.println("fln data: " + fln.data);
    }
    
    public static void main(String[] args) {
        Ch2q6_1stNodeInLoopOfCircularLL prob = new Ch2q6_1stNodeInLoopOfCircularLL();
        prob.test1();
    }

}
