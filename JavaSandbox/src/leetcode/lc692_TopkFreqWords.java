package leetcode;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;

public class lc692_TopkFreqWords {
    public List<String> topKFrequent(String[] words, int k) {
        Map<String, Integer> m = new HashMap<>();
        for(int i=0; i < words.length; i++) {
            String w = words[i];
            if(m.containsKey(w)) {
                m.put(w, m.get(w)+1);
            } else {
                m.put(w, 1);
            }
        }
        
        PriorityQueue<String> heap = new PriorityQueue<>(
            (w1, w2) -> m.get(w1).equals(m.get(w2)) ?
            w1.compareTo(w2): -1*(m.get(w1)-m.get(w2))
        );
        
        for(String w: m.keySet()) {
            heap.offer(w);
        }
        //System.out.println("heap:" + heap);
        
        List<String> topk = new ArrayList<>();
        for(int i=0; i < k; i++) {
            topk.add(heap.remove());
        }
        return topk;
    }
}
