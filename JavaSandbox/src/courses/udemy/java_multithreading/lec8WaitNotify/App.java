package courses.udemy.java_multithreading.lec8WaitNotify;

import java.util.Random;
import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.BlockingQueue;

public class App 
{
	private BlockingQueue<Integer> queue = new ArrayBlockingQueue<Integer>(10);
	Random random = new Random();
	/**
	 * loops indefinitely
	 */
	private void producer() throws InterruptedException
	{
		//Random random = new Random();
		
		while(true)
		{
			this.queue.put(this.random.nextInt(100));
		}
	}
	
	/**
	 * only take integers off once in a while
	 */
	private void consumer() throws InterruptedException
	{
		//Random random = new Random();
		
		while(true)
		{
			Thread.sleep(100);
			if(this.random.nextInt(10) == 0)
			{
				Integer value = this.queue.take();
				System.out.println("Taken value: " + value + "; Queue size: " + this.queue.size());
				System.out.println("Queue: "+ this.queue.toString());
			}
		}
	}
	
	public static void main(String[] args) throws InterruptedException
	{
		// TODO Auto-generated method stub
		App app = new App();
		
		Thread t1 = new Thread(new Runnable()
		{
			public void run()
			{
				try
				{
					app.producer();
				} 
				catch (InterruptedException e) 
				{
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			}
		});
		
		Thread t2 = new Thread(new Runnable()
		{
			public void run()
			{
				try
				{
					app.consumer();
				} 
				catch (InterruptedException e) 
				{
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			}
		});
		
		t1.start();
		t2.start();
		
		t1.join();
		t2.join();
	}
}
