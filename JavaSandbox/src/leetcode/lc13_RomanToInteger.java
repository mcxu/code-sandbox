package leetcode;

import java.util.HashMap;

public class lc13_RomanToInteger {
    public HashMap<Character, Integer> rti;
    
    public lc13_RomanToInteger() {
        this.rti = new HashMap<>();
        rti.put('I', 1);
        rti.put('V', 5);
        rti.put('X', 10);
        rti.put('L', 50);
        rti.put('C', 100);
        rti.put('D', 500);
        rti.put('M', 1000);
    }
    
    public int romanToInt(String s) {
        int tot = 0;
        int i = s.length()-1;
        while(i >= 0) {
            if(i==0) {
                tot += rti.get(s.charAt(i));
                break;
            }
            if(rti.get(s.charAt(i)) > rti.get(s.charAt(i-1))) {
                int diff = rti.get(s.charAt(i))-rti.get(s.charAt(i-1));
                tot += diff;
                i -= 1;
            } else {
                tot += rti.get(s.charAt(i));
            }
            
            i -= 1;
        }
        
        return tot;
    }
}
