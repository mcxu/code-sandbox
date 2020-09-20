/*
https://leetcode.com/problems/excel-sheet-column-number/
*/
package leetcode;

import java.util.HashMap;

public class lc171_ExcelColumnNumber {
    public int titleToNumber(String s) {
        HashMap<Character, Integer> chMap = new HashMap<>();
        for(char c='A'; c <= 'Z'; c++) {
            chMap.put(c, c-'A'+1);
        }
        //System.out.println("chMap: " + chMap);
        
        int n = 0;
        for(int i=0; i<s.length(); i++) {
            n += (chMap.get(s.charAt(s.length()-1-i)) * Math.pow(26, i));
        }
        
        return n;
    }
}
