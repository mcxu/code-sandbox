/**
 * Question 1.3: Method to decide if 1 string is permutation of another.
 */
package ctci5th.DataStructures.Ch1ArraysAndStrings;

public class Ch1q3_1StrPermutationOfOther 
{
    public boolean stringsArePermutations(String str1, String str2) 
    {
        if(str1.length() != str2.length())
        {
            return false;
        }

        for(int i=0; i < str1.length(); i++)
        {
            if(str1.charAt(i) != str2.charAt(str2.length()-1-i))
                return false;
        }
        return true;
    }

    public void test1() 
    {
        boolean test1 = stringsArePermutations("qwertyuiop", "qowpeiruty");
        System.out.println("test1: " + test1);
        
        boolean test2 = stringsArePermutations("asdfg", "gfdsa");
        System.out.println("test2: " + test2);
    }

    public static void main(String[] args)
    {
        Ch1q3_1StrPermutationOfOther prob = new Ch1q3_1StrPermutationOfOther();
        prob.test1();
    }
}