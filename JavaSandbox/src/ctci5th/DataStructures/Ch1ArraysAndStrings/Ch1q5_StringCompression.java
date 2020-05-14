/**
 * Question 1.5: Method to perform basic string compression using the counts 
 * of repeated characters. If the "compressed" string would not become smaller than the original
 * string, return the original string. 
 */
package ctci5th.DataStructures.Ch1ArraysAndStrings;

public class Ch1q5_StringCompression 
{
    public String compressString(String inputStr)
    {
        //do compression
        int ct = 1; //count num of chars in substring of same chars
        String compressedStr = "";
        for(int i=1; i<inputStr.length(); i++)
        {
            System.out.print("i= " + i);
            char prevChar = inputStr.charAt(i-1);
            System.out.print("  prev: " + prevChar);
            char currChar = inputStr.charAt(i);
            System.out.print("  curr: " + currChar);
            
            if(prevChar == currChar)
            {
                ct++;
                System.out.print("  ct=" + ct);
            }
            else
            {
                //need to generate compressed string
                compressedStr = compressedStr + prevChar + ct;

                ct = 1; //reset the counter
            }
            System.out.print("\n");
            
            //handle last section of string
            if(i == inputStr.length()-1)
            {
                compressedStr = compressedStr + prevChar + ct;
            }
        }
        
        //compare lengths
        if(compressedStr.length() < inputStr.length())
        {
            return compressedStr;
        }
        return inputStr;
    }
    
    public void test1()
    {
        String test1 = compressString("aasssddfffff");
        System.out.println("compressString test1: " + test1);
        
        String test2 = compressString("qqwweerrttyytywwwuuuuuu");
        System.out.println("compressString test2: " + test2);
    }

    public static void main(String[] args)
    {
        Ch1q5_StringCompression prob = new Ch1q5_StringCompression();
        prob.test1();
    }
}