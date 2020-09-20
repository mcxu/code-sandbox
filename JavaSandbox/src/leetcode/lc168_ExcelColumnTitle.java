/*
https://leetcode.com/problems/excel-sheet-column-title/
*/
package leetcode;

public class lc168_ExcelColumnTitle {
    public String convertToTitle(int n) {
        
        char[] letters = new char[26];
        for(char c='A'; c <= 'Z'; c++) {
            letters[c-'A'] = c;
        }
        //System.out.println("letters: " + Arrays.toString(letters));
        
        String title = "";
        while(n>0) {
            int mod = n%26;
            if(mod > 0) {
                title += letters[mod-1];
                n -= mod;
            } else {
                title += 'Z';
                n -= 1;
            }
            n = n/26;
        }
        return new StringBuilder(title).reverse().toString();
    }
}
