package leetcode;

import java.util.ArrayList;
import java.util.Arrays;

public class lc1471_kStrongestValuesInArray {
    public int[] getStrongest(int[] arr, int k) {
        Arrays.sort(arr);
        int m = arr[(int) (arr.length - 1) / 2];
        ArrayList<Integer> strongest = new ArrayList<>();
        
        int i = 0;
        int j = arr.length-1;
        for(int n=0; n<k; n++) {
            int ival = arr[i];
            int jval = arr[j];
            if(Math.abs(ival-m) > Math.abs(jval-m)){
                strongest.add(ival);
                i += 1;
            } else {
                strongest.add(jval);
                j -= 1;
            }
        }

        int[] strongestArr = new int[strongest.size()];
        for(int q=0; q<strongestArr.length; q++) {
            strongestArr[q] = strongest.get(q);
        }
        return strongestArr;
    } 

    public void test1() {
        int[] arr = {6,7,11,7,6,8};
        int k = 5;
        int[] res = getStrongest(arr, k);
        System.out.println("res: " + Arrays.toString(res));
    }

    public static void main(String[] args) {
        lc1471_kStrongestValuesInArray s = new lc1471_kStrongestValuesInArray();
        s.test1();
    }
}