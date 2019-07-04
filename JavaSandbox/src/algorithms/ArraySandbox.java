package algorithms;

import java.util.Arrays;

public class ArraySandbox {
    public int[] reverseArray(int[] input) {
        int inputLen = input.length;
        int temp = 0;

        for (int i = 0; i < inputLen / 2; i++) {
            temp = input[i];
            input[i] = input[inputLen - i - 1];
            input[inputLen - i - 1] = temp;
        }

        return input;
    }
    
    public void test_reverseArray()
    {
        int[] input = { 1, 2, 3, 4 };
        int[] output = reverseArray(input);
        System.out.println("output: " + Arrays.toString(output));
    }
    
    public boolean allCharsUnique(String inStr)
    {
        int[] chArray = new int[128];
        
        for(int i=0; i < inStr.length(); i++)
        {
            char ch = inStr.charAt(i);
            int asciiInt = (int) ch;
            if(chArray[asciiInt] == 0)
            {
                chArray[asciiInt] = 1;
            }
            else
            {
                return false;
            }
        }
        
        return true;
    }
    
    public void test_allCharsUnique()
    {
        System.out.println("; to int = " + (int)';');
        String test = "qwertyuasdfejkl";
        boolean result = allCharsUnique(test);
        System.out.println("result: " + result);
    }

    public static void main(String[] args) {
        ArraySandbox as = new ArraySandbox();
        //as.test_reverseArray();
        as.test_allCharsUnique();
    }

}
