package com;

import java.util.Hashtable;
import java.lang.Character;
import java.lang.Integer;

public class RepeatSandbox 
{
	String[] theArray;
	int arraySize;
	int itemsInArray = 0;
	
	RepeatSandbox()
	{
		
	}
	
	// returns the first nonrepeated Character in a string
	public Character findFirstNonRepeatedChar(String input) 
	{
		// create a new hashtable for the frequency that each letter appears
		Hashtable<Character, Integer> freqHash = new Hashtable<Character, Integer>();
	
		int strLength;
		Character chr = null;
		Integer hashValue;
		
		strLength = input.length( );
		
		//Tally up the total number of times each char appears
		//in the input string, and store it in the hash table.
		for (int i =0; i < strLength; i++)
		{
			chr = input.charAt(i);
			hashValue = freqHash.get(chr);
			
			if (hashValue == null) 
			{
				freqHash.put(chr, 1);
				System.out.println("integer==null:	chr=" + chr + "		hashtable: " + freqHash);
			}
			else
			{
				freqHash.put(chr, hashValue + 1);
				System.out.println("else:			chr=" + chr + "		hashtable: " + freqHash); 
			}
		}
		
		//Traverse through the input integer one more time, retrieve the
		//value from each char in the hash table. The first time there is a frequency of 1
		//means that the first non-repeating char is found.
		for(int i = 0; i<input.length(); i++)
		{
			System.out.println("i= " + i);
			chr = input.charAt(i);
			hashValue = freqHash.get(chr);
			System.out.println("hashValue: " + hashValue);
			if(hashValue == 1)
			{
				return chr;
			}
		}
		
		//return null if the check falls through
		return null;
	}


	public static void main(String[] args) 
	{
		RepeatSandbox nr = new RepeatSandbox();
		Character chr = nr.findFirstNonRepeatedChar("aweoiuakfjheoawidsafkljdsasaashjsd");
		System.out.println("main: nonrepeating char= " + chr);
		
		
	}

}
