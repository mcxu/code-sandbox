package courses.udemy.java_multithreading.lec5ThreadPools;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

class Processor implements Runnable
{
	private int id;
	
	public Processor(int id)
	{
		this.id = id;
	}
	
	public void run()
	{
		System.out.println("Starting: " + this.id);
		try
		{
			Thread.sleep(1000);
		}
		catch (InterruptedException e)
		{
			e.printStackTrace();
		}
		System.out.println("Completed: " + this.id);
	}
}


public class Apps 
{

	public static void main(String[] args) 
	{
		// TODO Auto-generated method stub
		ExecutorService executor = Executors.newFixedThreadPool(2);
		
		//need to submit tasks to executor
		for(int i=0; i<5; i++)
		{
			executor.submit(new Processor(i)); //Processor is the class above
		}
		
		//After accepted tasks, shut down. This will wait for all threads to
		//finish loading before shutting down.
		executor.shutdown();
		
		System.out.println("All tasks submitted.");
		
		try 
		{
			executor.awaitTermination(1, TimeUnit.DAYS);
		} 
		catch (InterruptedException e) 
		{
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

}
