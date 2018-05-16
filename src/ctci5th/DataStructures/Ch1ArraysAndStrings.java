package ctci5th.DataStructures;

import java.util.ArrayList;
import java.util.HashMap;

import ctci5th.AlgUtils;

/**
 * Chapter 1 Arrays and Strings
 * Book pg. 71, PDF pg. 80
 * @author MichaelXu
 */
public class Ch1ArraysAndStrings 
{	
	/**
	 * Question 1.1: Algorithm to determine if a string has all unique characters.
	 * @param testStr
	 */
	public boolean strContainsAllUniqueChar(String testStr)
	{
		ArrayList<Character> compareList = new ArrayList<>();
		
		for(int i=0; i<testStr.length(); i++)
		{
			char ch = testStr.charAt(i);
			System.out.println("ch: " + ch);
			if(compareList.contains(ch))
			{
				System.out.println("repeat detected at index: " + i + " char: " + ch);
				return false;
			}
			else
			{
				compareList.add(ch);
			}
		}
		return true;
	}
	
	public void testCh1p1()
	{
		boolean ch1p1Test = strContainsAllUniqueChar("adhesivesssss");
		System.out.println("ch1p1Test: " + ch1p1Test);
	}
	
	/**
	 * Question 1.2: Function to reverse string.
	 * (In Java strings are not null terminated, as in C/C++)
	 * @param testStr
	 */
	public String reverseString(String testStr)
	{
		String out = "";
		for(int i=testStr.length()-1; i>=0; i--)
		{
			char ch = testStr.charAt(i);
			out = out + ch;
		}
		return out;
	}
	
	public void testCh1p2()
	{
		String reversed = reverseString("qwertyuiop");
		System.out.println("reversed: " + reversed);
	}
	
	/**
	 * Question 1.3: Method to decide if 1 string is permutation of another.
	 * @param args
	 */
	public boolean stringsArePermutations(String str1, String str2)
	{
		// build character frequency maps
		HashMap<Character, Integer> str1Freq = AlgUtils.getCharFreqInStr(str1);
		HashMap<Character, Integer> str2Freq = AlgUtils.getCharFreqInStr(str2);
		
		// compare keysets
		str1Freq.keySet();
		
		return false;
	}
	
	
	public static void main(String[] args) {
		Ch1ArraysAndStrings ch1 = new Ch1ArraysAndStrings();
		//ch1.testCh1p1();
		ch1.testCh1p2();
	}

}
