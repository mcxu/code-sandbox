package ctci5th.DataStructures;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Set;

import ctci5th.AlgUtils;

/**
 * Chapter 1 Arrays and Strings Book pg. 71, PDF pg. 80
 * 
 * @author MichaelXu
 */
public class Ch1ArraysAndStrings 
{
    /**
     * Question 1.1: Algorithm to determine if a string has all unique characters.
     * 
     * @param testStr
     */
    public boolean strContainsAllUniqueChar(String testStr) 
    {
        ArrayList<Character> compareList = new ArrayList<>();

        for (int i = 0; i < testStr.length(); i++) 
        {
            char ch = testStr.charAt(i);
            System.out.println("ch: " + ch);
            if (compareList.contains(ch)) 
            {
                System.out.println("repeat detected at index: " + i + " char: " + ch);
                return false;
            } 
            else {
                compareList.add(ch);
            }
        }
        return true;
    }

    public void testQ1p1() 
    {
        boolean ch1p1Test = strContainsAllUniqueChar("adhesivesssss");
        System.out.println("ch1p1Test: " + ch1p1Test);
    }

    /**
     * Question 1.2: Function to reverse string. (In Java strings are not null
     * terminated, as in C/C++)
     * 
     * @param testStr
     */
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

    public void testQ1p2() 
    {
        String reversed = reverseString("qwertyuiop");
        System.out.println("reversed: " + reversed);
    }

    /**
     * Question 1.3: Method to decide if 1 string is permutation of another.
     * 
     * @param args
     */
    public boolean stringsArePermutations(String str1, String str2) 
    {
        // build character frequency maps
        HashMap<Character, Integer> str1Freq = AlgUtils.getCharFreqInStr(str1);
        HashMap<Character, Integer> str2Freq = AlgUtils.getCharFreqInStr(str2);

        // compare keysets
        Set<Character> keyset1 = str1Freq.keySet();
        Set<Character> keyset2 = str2Freq.keySet();
        System.out.println("keysets to compare: " + keyset1 + "\t" + keyset2);

        // condition to check if sets match
        if (keyset1.containsAll(keyset2) && keyset2.containsAll(keyset1)) 
        {
            Character[] ks1Array = keyset1.toArray(new Character[0]);
            for (Character ks1Ch : ks1Array) 
            {
                if (str1Freq.get(ks1Ch) != str2Freq.get(ks1Ch)) 
                {
                    return false;
                }
            }
            // return true here b/c items in set have been iterated.
            return true;
        } 
        else {
            System.out.println("keyset1 and 2 are not the same.");
            return false;
        }
    }

    public void testQ1p3() 
    {
        boolean test1 = stringsArePermutations("qwertyuiop", "qowpeiruty");
        System.out.println("test1: " + test1);
        
        boolean test2 = stringsArePermutations("asdfg", "asdfgs");
        System.out.println("test2: " + test2);
    }

    /**
     * Question 1.4: Method to replace all spaces in a string with'%20'. You
     * may assume that the string has sufficient space at the end of the string to
     * hold the additional characters, and that you are given the "true" length of
     * the string.
     * 
     * @param str
     * @return
     */
    public String replaceSpaceWithInsert(String str, String insert) 
    {
        char[] strChars = str.toCharArray();
        System.out.println("before insert: " + Arrays.toString(strChars));
        for (int i = strChars.length - 1; i >= 0; i--) {
            System.out.print("i=" + i);
            char ch = strChars[i];
            System.out.print("	ch: " + ch);

            // only need to shift when there is a blank
            if (ch == ' ') 
            {
                System.out.print("	Blank");
                // perform shift; repeat for every char in string to insert
                for (int S = 0; S < insert.length() - 1; S++) 
                {
                    System.out.print("\tS=" + S);
                    // shift from end of char array to current index.
                    for (int j = strChars.length - 2; j > i; j--) 
                    {
                        System.out.print("\tj=" + j);
                        strChars[j + 1] = strChars[j];
                        strChars[j] = ' ';
                    }
                }
            }
            System.out.print("\n");
        }

        // for blanks insert the required string
        int k = 0;
        for (int q = 0; q < strChars.length; q++) 
        {
            if (k == 3) {k = 0;}
            if (strChars[q] == ' ') 
            {
                strChars[q] = insert.charAt(k);
                k++;
            }
        }
        System.out.println("after insert: " + Arrays.toString(strChars));

        // reconstruct char array back into string
        String result = "";
        for (char ch : strChars) 
        {
            result = result + ch;
        }
        return result;
    }

    public void testQ1p4() 
    {
        String str = "Mr John Smith    ";
        // String str = "Mr John Smith ";
        // String str = "Mr Smith ";
        String result = replaceSpaceWithInsert(str, "%20");
        System.out.println("result: " + result);
    }
    
    /**
     * Question 1.5: Method to perform basic string compression using the counts 
     * of repeated characters. If the "compressed" string would not become smaller than the original
     * string, return the original string.
     * @return
     */
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
    
    public void testQ1p5()
    {
        String test1 = compressString("aasssddfffff");
        System.out.println("compressString test1: " + test1);
        
        String test2 = compressString("qqwweerrttyytywwwuuuuuu");
        System.out.println("compressString test2: " + test2);
    }
    
    /**
     * Rotate NxN matrix 90 degrees in place in CCW direction
     * @param matrix 
     * @return
     */
    public String[][] rotateSqMatrix90DegCCW(String[][] matrix)
    {
        final int maxInd = matrix.length-1;
        
        String[] coArray = new String[3]; 
        /* stores the carry over before shift
            0: carry over from left col
            1: carry over from bottom row 
            2: carry over from right col
        */

        boolean cor = false; //carry over read, has stored the item that will be carried over
        
        //for each layer of the matrix; like an onion; lyr means coords (0,0), (1,1), (2,2)...
        for(int lyr=0; lyr<(matrix.length/2); lyr++)
        {
            //int lyr = 0; // test
            //number of times to shift for a given layer
            for(int shiftCt=lyr; shiftCt < maxInd-lyr; shiftCt++)
            {
                //perform a 1-item shift for each side
                System.out.println("##### lyr=" + lyr + "   shiftCt=" + shiftCt + " #####");
                
                //left col shift down
                for(int i=maxInd-lyr-1; i >= lyr; i--)
                {
                    if(cor == false)
                    {
                        coArray[0] = matrix[i+1][lyr];
                        cor = true;
                    }
                    matrix[i+1][lyr] = matrix[i][lyr];
                }
                cor = false;
                System.out.print("after left col shift down:\n");
                printNbyNmatrix(matrix);
                System.out.println("coArray[0]: " + coArray[0]);
                
                //bottom row shift right
                for(int i=maxInd-lyr-1; i >= lyr; i--)
                {
                    if(cor == false)
                    {
                        coArray[1] = matrix[maxInd-lyr][i+1];
                        cor = true;
                    }
                    matrix[maxInd-lyr][i+1] = matrix[maxInd-lyr][i];
                }
                matrix[maxInd-lyr][lyr+1] = coArray[0]; //add carry over from left col
                cor = false;
                System.out.print("after bottom row shift right:\n");
                printNbyNmatrix(matrix);
                System.out.println("coArray[1]: " + coArray[1]);
                
                //right col shift up
                for(int i=lyr; i <= maxInd-lyr-1; i++)
                {
                    if(cor == false)
                    {
                        coArray[2] = matrix[lyr][maxInd-lyr];
                        cor = true;
                    }
                    matrix[i][maxInd-lyr] = matrix[i+1][maxInd-lyr];
                }
                matrix[maxInd-lyr-1][maxInd-lyr] = coArray[1]; //add carry over from bottom row
                cor = false;
                System.out.print("after right col shift up:\n");
                printNbyNmatrix(matrix);
                System.out.println("coArray[2]: " + coArray[2]);
                
                //top row shift left
                for(int i=lyr; i <= maxInd-lyr-1; i++)
                {
                    matrix[lyr][i] = matrix[lyr][i+1];
                }
                matrix[lyr][maxInd-lyr-1] = coArray[2]; //add carry over from right col
                System.out.print("after top row shift left:\n");
                printNbyNmatrix(matrix);
            }
        }
        
        return matrix;
    }
    
    public void printNbyNmatrix(String[][] matrix)
    {
        for(int row=0; row < matrix.length; row++)
        {
            for(int col=0; col < matrix.length; col++)
            {
                System.out.print(matrix[row][col] + " ");
            }
            System.out.print("\n");
        }
    }
    
    public void testQ1p6()
    {
        String[][] matrix1 = new String[][] {
            {"a","b","c","d"},
            {"e","f","g","h"},
            {"i","j","k","l"},
            {"m","n","o","p"},
        };
        
        String[][] matrix2 = new String[][] {
            {"^"," "," "," "," ","Y"," "," "," ","$"},
            {" "," "," "," ","@","@"," "," "," "," "},
            {" "," "," ","@"," "," ","@"," "," "," "},
            {" "," ","@"," "," "," "," ","@"," "," "},
            {"A","@","@","@"," "," ","@","@","@","L"},
            {" "," "," ","@"," "," ","@"," "," "," "},
            {" "," "," ","@"," "," ","@"," "," "," "},
            {" "," "," ","@"," "," ","@"," "," "," "},
            {" "," "," ","@","@","@","@"," "," "," "},
            {"!"," "," "," ","V"," "," "," "," ","#"}
        };
        
        System.out.println("before rotate:");
        printNbyNmatrix(matrix2);
        String[][] out1 = rotateSqMatrix90DegCCW(matrix2); //point left
        out1 = rotateSqMatrix90DegCCW(out1); //point down
        out1 = rotateSqMatrix90DegCCW(out1); //point right
        System.out.print("end result:\n");
        printNbyNmatrix(out1);
    }

    public static void main(String[] args) 
    {
        Ch1ArraysAndStrings ch1 = new Ch1ArraysAndStrings();
        //ch1.testQ1p1();
        //ch1.testQ1p2();
        //ch1.testQ1p3();
        //ch1.testQ1p4();
        //ch1.testQ1p5();
        ch1.testQ1p6();
    }

}
