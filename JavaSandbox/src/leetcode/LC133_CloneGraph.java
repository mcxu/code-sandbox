package leetcode;

import java.util.List;
import java.util.ArrayList;
import java.util.HashMap;

// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}

class LC133_CloneGraph {
    public Node cloneGraph(Node node) {
        if(node == null) {
            return null;
        }

        List<Node> q = new ArrayList<>();
        q.add(node);
        HashMap<Integer, Node> copyMap = new HashMap<>();
        copyMap.put(node.val, new Node(node.val));

        while(q.size() > 0) {
            Node currNode = q.get(0);
            q.remove(0);
            //System.out.println("currNode removed: " + currNode);
            Node currNodeCopy = copyMap.get(currNode.val);

            for(Node neighbor: currNode.neighbors) {
                if(!copyMap.keySet().contains(neighbor.val)) {
                    copyMap.put(neighbor.val, new Node(neighbor.val));
                    q.add(neighbor);
                }

                Node neighborCopy = copyMap.get(neighbor.val);
                currNodeCopy.neighbors.add(neighborCopy);
            }
        }

        return copyMap.get(node.val);
    }
}
