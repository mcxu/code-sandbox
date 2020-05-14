/**
 * Question 1.4: Method to replace all spaces in a string with'%20'. You
 * may assume that the string has sufficient space at the end of the string to
 * hold the additional characters, and that you are given the "true" length of
 * the string.
 */
package ctci5th.DataStructures.Ch1ArraysAndStrings;
 
public class Ch1q4_ReplaceSpacesWithP20
{
    public String replaceSpaceWithP20(String str) 
    {
        char[] charArray = str.toCharArray();
        int i = 0;
        while(i < charArray.length)
        {
            if(charArray[i] == ' ')
            {
                charArray[i] = '%';
                i++;
                for(int n=0; n < 2; n++)
                {   int j = str.length()-1;
                    while(j > i)
                    {
                        charArray[j] = charArray[j-1];
                        j--;
                    }
                    if(n==0)
                        charArray[i] = '2';
                    else if(n==1)
                        charArray[i] = '0';
                    i++;
                }
            }
            else
                i++;
        }

        return new String(charArray);
    }

    public void test1() 
    {
        String str = "Mr John Smith    ";
        //String str = "Mr John Smith ";
        //String str = "Mr Smith ";
        String result = replaceSpaceWithP20(str);
        System.out.println("result: " + result);
    }

    public static void main(String[] args)
    {
        Ch1q4_ReplaceSpacesWithP20 prob = new Ch1q4_ReplaceSpacesWithP20();
        prob.test1();
    }
}
