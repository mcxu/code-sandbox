package ctci5th.util;

import java.util.HashMap;

public class AlgUtils 
{
    public static HashMap<Character, Integer> getCharFreqInStr(String testStr) 
    {
        HashMap<Character, Integer> strFreqMap = new HashMap<>();

        for (char ch : testStr.toCharArray()) 
        {
            if (strFreqMap.containsKey(ch)) 
            {
                strFreqMap.put(ch, strFreqMap.get(ch) + 1);
            } 
            else 
            {
                strFreqMap.put(ch, 1);
            }
        }

        return strFreqMap;
    }

    public static void test_getCharFreqInStr() 
    {
        System.out.println(getCharFreqInStr("asdff")); // {a=1, s=1, d=1, f=2}
    }
    
    public static void printMatrix(Object[][] matrix)
    {
        for(int row=0; row < matrix.length; row++)
        {
            for(int col=0; col < matrix[0].length; col++)
            {
                System.out.print(matrix[row][col] + " ");
            }
            System.out.print("\n");
        }
    }
    
    public static void test_parseInt()
    {
        System.out.println((int) 'a');
        System.out.println((int) 'b');
    }

    public static void main(String[] args) 
    {
        //test_getCharFreqInStr();
        test_parseInt();
    }

}
