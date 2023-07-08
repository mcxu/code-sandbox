package leetcode;

public class LC141_LinkedListCycle {
    public boolean hasCycle(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;

        while(slow != null && fast != null) {
            
            fast = fast.next;

            if(fast == null) {
                return false;
            }

            fast = fast.next;
            slow = slow.next;

            if(slow == fast) {
                return true;
            }
        }

        return false;
    }
}

class ListNode {
    int val;
    ListNode next;
    ListNode(int x) {
        val = x;
        next = null;
    }
}