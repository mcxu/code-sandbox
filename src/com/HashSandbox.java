package com;

import java.util.Enumeration;
import java.util.Hashtable;
import java.util.Random;

public class HashSandbox 
{
	public HashSandbox(int size)
	{
		
	}
	
	public static void main (String args[]) throws Exception 
	{
	    // Start with ten, expand by ten when limit reached
	    Hashtable<Integer, Integer> hash = new Hashtable<Integer, Integer>();

	    Random rand = new Random();
	    for (int i = 0; i <= 5; i++)
	    {
			Integer integer = new Integer ( i );
			hash.put(integer, rand.nextInt(100));
	    }
	    
	    System.out.println("hash:" + hash);
	    int response = hash.get(1) + hash.get(2);
	    System.out.println("specific num: " + response);
	    
	    
	    // Get value out again
	    System.out.println (hash.get(5));
	    /*
	    // Get value out again
	    System.out.println (hash.get(new Integer(21)));

	    System.in.read();
	    
	    // Get all values
	    for (Enumeration e = hash.keys(); e.hasMoreElements();)
	    {
	    	System.out.println (hash.get(e.nextElement()));
	    }
	    */
	 }
}
