package courses.udemy.java_multithreading.lec1StartingThreads;

import java.lang.Thread;

class Runner extends Thread 
{
	public void run()
	{
		for(int i=0; i<10; i++)
		{
			System.out.println("Hello " + i);
			try
			{
				Thread.sleep(100);
			}
			catch (InterruptedException e)
			{
				e.printStackTrace();
			}
		}
	}
}

public class Lec1Demo1 
{
	public static void main(String[] args)
	{
		Runner runner1 = new Runner();
		runner1.start();
		
		Runner runner2 = new Runner();
		runner2.start();
	}
}
