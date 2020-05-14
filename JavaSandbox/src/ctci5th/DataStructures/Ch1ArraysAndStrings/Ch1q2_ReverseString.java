/**
 * Question 1.2: Function to reverse string. (In Java strings are not null terminated)
 */
package ctci5th.DataStructures.Ch1ArraysAndStrings;

public class Ch1q2_ReverseString {

    public String reverseString(String testStr) 
    {
        String out = "";
        for (int i = testStr.length() - 1; i >= 0; i--) 
        {
            char ch = testStr.charAt(i);
            out = out + ch;
        }
        return out;
    }

    public void test1() 
    {
        String reversed = reverseString("qwertyuiop");
        System.out.println("reversed: " + reversed);
    }

    public static void main(String[] args)
    {
        Ch1q2_ReverseString prob = new Ch1q2_ReverseString();
        prob.test1();
    }
}