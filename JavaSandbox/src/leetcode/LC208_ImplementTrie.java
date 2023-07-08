package leetcode;
// https://leetcode.com/problems/implement-trie-prefix-tree/description/

import java.util.*;

public class LC208_ImplementTrie {
    HashMap<Character, HashMap> trie;

    public LC208_ImplementTrie() {
        trie = new HashMap<Character, HashMap>();
    }
    
    public void insert(String word) {
        HashMap<Character, HashMap> n = trie;
        for(Character currChar: word.toCharArray()) {
            if(n.keySet().contains(currChar)) {
                n = n.get(currChar);
            } else {
                n.put(currChar, new HashMap<Character, HashMap>());
                n = n.get(currChar);
            }
        }
        n.put('*', new HashMap<Character, HashMap>());
    }
    
    public boolean search(String word) {
        HashMap<Character, HashMap> n = trie;
        for(Character currChar: word.toCharArray()) {
            if(n.keySet().contains(currChar)) {
                n = n.get(currChar);
            } else {
                return false;
            }
        }

        if(n.keySet().contains('*') || n.isEmpty()) {
            return true;
        }
        return false;
    }
    
    public boolean startsWith(String prefix) {
        HashMap<Character, HashMap> n = trie;
        for(Character currChar: prefix.toCharArray()) {
            if(n.keySet().contains(currChar)) {
                n = n.get(currChar);
            } else {
                return false;
            }
        }
        return true;
    }
}
