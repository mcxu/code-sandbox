// https://leetcode.com/problems/decode-string/
package leetcode;

public class lc394_DecodeString {
    public String decodeString(String s) {
        ArrayList<Character> stack = new ArrayList<>();
        
        for(int i=0; i < s.length(); i++) {
            Character ch = s.charAt(i);
            stack.add(ch);
            
            //System.out.println("stack A: " + stack);
            if(stack.get(stack.size()-1).equals(']')) {
                stack.remove(stack.size()-1); //pop off closing bracket
                String backtrackedStr = backtrackStr(stack);
                backtrackedStr = new StringBuilder(backtrackedStr).reverse().toString();
                //System.out.println("backtrackedStr: " + backtrackedStr);
                stack.remove(stack.size()-1); //pop off opening bracket
                //System.out.println("stack B: " + stack);
                
                // get k
                int k = 1;
                String kStr = "";
                while(!stack.isEmpty() && Character.isDigit(stack.get(stack.size()-1))) {
                    kStr = stack.remove(stack.size()-1).toString() + kStr;
                }
                if(!kStr.isEmpty())
                    k = Integer.parseInt(kStr);
                
                String section = backtrackedStr.repeat(k);
                //System.out.println("section: " + section);
                
                //put section back on stack
                for(int j=0; j < section.length(); j++) {
                    stack.add(section.charAt(j));
                }
                //System.out.println("stack end of iter: " + stack);
            } 
        }
        
        String sdecoded = "";
        while(!stack.isEmpty()) {
            sdecoded += stack.remove(0);
        }
        return sdecoded;
    }
    
    public String backtrackStr(ArrayList<Character> stack) {
        String s = "";
        while(!stack.isEmpty() && !(stack.get(stack.size()-1).equals('['))) {
            Character ch = stack.remove(stack.size()-1);
            s = s.concat(ch.toString());
        }
        
        return s;
    }
}
