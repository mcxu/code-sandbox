// https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
package leetcode;

public class lc1249_MinRemoveValidParenthesis {
    public String minRemoveToMakeValid(String s) {
        char[] sArr = s.toCharArray();
        Stack<Object[]> stack = new Stack<>();
        for(int i=0; i < s.length(); i++) {
            char ch = s.charAt(i);
            if(ch == '(') {
                stack.push(new Object[]{ch, i});
            } else if (ch == ')') {
                if(!stack.empty() && stack.peek()[0].equals('(')) {
                    stack.pop();
                } else {
                    stack.push(new Object[]{ch, i});
                }
            }
        }
        Iterator<Object[]> stackIter = stack.iterator();
        while(stackIter.hasNext()) {
            Object[] item = stackIter.next();
            sArr[(int)item[1]] = (char)0;
        }
        
        //System.out.println("sArr final: " + Arrays.toString(sArr));
        String out = "";
        for(int i=0; i < sArr.length; i++) { 
            if(sArr[i] != (char)0)
                out += Character.toString(sArr[i]);
        }
        return out;
    }
}
