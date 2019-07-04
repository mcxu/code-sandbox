package courses.udemy.java_multithreading.lec6CountdownLatches;

import java.util.concurrent.CountDownLatch;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;


class Processor implements Runnable
{
	private CountDownLatch latch;
	
	public Processor(CountDownLatch latch)
	{
		this.latch = latch;
	}
	
	public void run()
	{
		System.out.println("Started.");
		
		try
		{
			Thread.sleep(3000);
		}
		catch (InterruptedException e)
		{
			e.printStackTrace();
		}
		
		this.latch.countDown();
	}
}


public class App 
{
	public static void main(String[] args) 
	{
		// TODO Auto-generated method stub
		CountDownLatch latch = new CountDownLatch(3);
		ExecutorService executor = Executors.newFixedThreadPool(3);
		
		for(int i=0; i<3; i++)
		{
			executor.submit(new Processor(latch));
		}
		
		try 
		{
			latch.await(); //waits till countdown reaches 0
		} 
		catch (InterruptedException e) 
		{
			// TODO Auto-generated catch block
			e.printStackTrace();
		} 
		System.out.println("Completed");
	}

}
