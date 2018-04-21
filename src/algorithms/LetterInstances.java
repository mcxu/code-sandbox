package algorithms;

import java.io.*;

public class LetterInstances {
	
	static InputStreamReader isr = new InputStreamReader(System.in);
	static BufferedReader br = new BufferedReader(isr);
	
	public static void main(String[] args) throws IOException
	{
		
		int num = 0;
		
		String input;
		System.out.print("Input a string: ");
		input = br.readLine();
		System.out.println("You inputted: " + input);
		
		char search;
		System.out.print("Enter a letter to search: ");
		search = (char)br.read();
		
		int count = 0;
		for(int i=0; i < input.length(); i++)
		{
			if(input.charAt(i)  == search)
				count++;
		}
		
		System.out.println("There are " + count + " instances of the letter " + search);
		
		
	}
}
