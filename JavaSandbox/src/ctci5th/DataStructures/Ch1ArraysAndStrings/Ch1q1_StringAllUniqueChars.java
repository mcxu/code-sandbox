/**
 * Question 1.1: Algorithm to determine if a string has all unique characters.
 */
package ctci5th.DataStructures.Ch1ArraysAndStrings;
import java.util.Set;
import java.util.HashSet;

public class Ch1q1_StringAllUniqueChars 
{
    public boolean strContainsAllUniqueChar(String testStr) 
    {
        Set<Character> compareSet = new HashSet<>();
        for (int i = 0; i < testStr.length(); i++) 
        {
            char ch = testStr.charAt(i);
            if (compareSet.contains(ch)) {
                return false;
            } 
            else {
                compareSet.add(ch);
            }
        }
        return true;
    }


    public void test1()
    {
        boolean ch1p1Test = strContainsAllUniqueChar("adhesivesssss");
        System.out.println("ch1p1Test: " + ch1p1Test);
    }

    public static void main(String[] args)
    {
        Ch1q1_StringAllUniqueChars prob = new Ch1q1_StringAllUniqueChars();
        prob.test1();
    }
}