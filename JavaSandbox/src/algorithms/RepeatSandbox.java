package algorithms;

import java.util.Hashtable;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.Character;
import java.lang.Integer;

public class RepeatSandbox {
    String[] theArray;
    int arraySize;
    int itemsInArray = 0;

    RepeatSandbox() {

    }

    // returns the first nonrepeated Character in a string
    public Character findFirstNonRepeatedChar(String input) {
        // create a new hashtable for the frequency that each letter appears
        Hashtable<Character, Integer> freqHash = new Hashtable<Character, Integer>();

        int strLength;
        Character chr = null;
        Integer hashValue;

        strLength = input.length();

        // Tally up the total number of times each char appears
        // in the input string, and store it in the hash table.
        for (int i = 0; i < strLength; i++) {
            chr = input.charAt(i);
            hashValue = freqHash.get(chr);

            if (hashValue == null) {
                freqHash.put(chr, 1);
                System.out.println("integer==null:	chr=" + chr + "		hashtable: " + freqHash);
            } else {
                freqHash.put(chr, hashValue + 1);
                System.out.println("else:			chr=" + chr + "		hashtable: " + freqHash);
            }
        }

        // Traverse through the input integer one more time, retrieve the
        // value from each char in the hash table. The first time there is a frequency
        // of 1
        // means that the first non-repeating char is found.
        for (int i = 0; i < input.length(); i++) {
            System.out.println("i= " + i);
            chr = input.charAt(i);
            hashValue = freqHash.get(chr);
            System.out.println("hashValue: " + hashValue);
            if (hashValue == 1) {
                return chr;
            }
        }

        // return null if the check falls through
        return null;
    }
    
    public void test_findFirstNonRepeatedChar()
    {
        Character chr = findFirstNonRepeatedChar("aweoiuakfjheoawidsafkljdsasaashjsd");
        System.out.println("first nonrepeating char= " + chr);
    }
    
    public void countCharInstances()
    {
        InputStreamReader isr = new InputStreamReader(System.in);
        BufferedReader br = new BufferedReader(isr);
        
        String input = null;
        System.out.print("Input a string: ");
        try {
            input = br.readLine();
            System.out.println("You inputted: " + input);
        } catch (IOException e) {
            e.printStackTrace();
        }
        
        char search;
        System.out.print("Enter a letter to search: ");
        try {
            search = (char) br.read();
            
            int count = 0;
            for (int i = 0; i < input.length(); i++) {
                if (input.charAt(i) == search)
                    count++;
            }
            
            System.out.println("There are " + count + " instances of the char: " + search);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    

    public static void main(String[] args) 
    {
        RepeatSandbox rs = new RepeatSandbox();
        //rs.test_findFirstNonRepeatedChar();
        rs.countCharInstances();
    }

}
