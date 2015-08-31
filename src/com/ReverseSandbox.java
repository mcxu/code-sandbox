package com;

import java.util.Arrays;

public class ReverseSandbox 
{
	public int[] reverseArray(int[] input)
	{
		int inputLen = input.length;
		int temp = 0;
		
		for(int i = 0; i<inputLen/2; i++)
		{
			temp = input[i];
			input[i] = input[inputLen-i-1];
			input[inputLen-i-1] = temp;
		}
		
		return input;
	}
	
	public static void main(String[] args) 
	{
		// TODO Auto-generated method stub
		ReverseSandbox rev = new ReverseSandbox();
		int[] input = {1,2,3,4};
		int[] output = rev.reverseArray(input);
		System.out.println("output: " + Arrays.toString(output));
	}

}
