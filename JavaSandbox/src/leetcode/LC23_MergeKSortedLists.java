package leetcode;
// https://leetcode.com/problems/merge-k-sorted-lists/

import java.util.*;

public class LC23_MergeKSortedLists {
    public ListNode mergeKLists(ListNode[] lists) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();

        for(int i=0; i<lists.length; i++) {
            ListNode n = lists[i];
            while(n != null) {
                pq.offer(n.val);
                n = n.next;
            }
        }

        //System.out.println("pq after inserting: " + pq);

        ListNode newHead = null;
        ListNode n = newHead;

        while(pq.size() > 0) {
            Integer pqVal = pq.poll();

            if(newHead == null) {
                newHead = new ListNode(pqVal);
                n = newHead;
            } else {
                n.next = new ListNode(pqVal);
                n = n.next;
            }
        }

        return newHead;
    }
}
