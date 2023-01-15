package leetcode;

public class lc214_ShortestPalindrome {
    public String shortestPalindrome(String s) {
        String srev = new StringBuilder(s).reverse().toString();

        for(int i=0; i<s.length(); i++) {
            if(s.substring(0, s.length()-i).equals(srev.substring(i, srev.length()))) {
                return srev.substring(0, i) + s;
            }
        }

        return "";
    }
}
