package courses.udemy.java_multithreading.lec2ThreadSync;

import java.util.Scanner;


class Processor extends Thread
{
	private volatile boolean running = true; //caching variables
	
	public void run()
	{
		while(running)
		{
			System.out.println("Hello");
			
			try
			{
				Thread.sleep(1000);
			}
			catch (InterruptedException e)
			{
				e.printStackTrace();
			}
		}
	}
	
	public void shutdown()
	{
		running = false;
	}
	
}


public class App 
{

	public static void main(String[] args) 
	{
		// TODO Auto-generated method stub
		Processor proc1 = new Processor();
		proc1.start();
		
		System.out.println("Press return to stop");
		Scanner scanner = new Scanner(System.in);
		scanner.nextLine();
		scanner.close();
		proc1.shutdown();
	}

}
