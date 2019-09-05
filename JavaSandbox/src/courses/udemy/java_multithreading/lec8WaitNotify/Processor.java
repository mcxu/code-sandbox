package courses.udemy.java_multithreading.lec8WaitNotify;

import java.util.Scanner;

public class Processor 
{
	public void produce() throws InterruptedException
	{
		synchronized(this)
		{
			System.out.println("Producer thread running ....");
			wait();
			System.out.println("Resumed.");
		}
	}
	
	public void consume() throws InterruptedException
	{
		Scanner scanner = new Scanner(System.in);
		Thread.sleep(2000);
		scanner.close();
		synchronized(this)
		{
			System.out.println("Waiting for return key.");
			scanner.nextLine();
			System.out.println("Return key pressed.");
			notify();
		}
	}
	
	/*
	public static void main(String[] args) 
	{
		// TODO Auto-generated method stub
		
	}
	*/

}
