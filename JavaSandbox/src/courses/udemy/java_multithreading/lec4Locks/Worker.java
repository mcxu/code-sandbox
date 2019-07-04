package courses.udemy.java_multithreading.lec4Locks;

import java.util.List;
import java.util.ArrayList;
import java.lang.Integer;
import java.util.Random;

public class Worker 
{
	//Rand num generator
	private Random random = new Random();
	
	//Create different locks, since writing to different lists
	private Object lock1 = new Object();
	private Object lock2 = new Object();
	
	private List<Integer> list1 = new ArrayList<Integer>();
	private List<Integer> list2 = new ArrayList<Integer>();
	
	public void stageOne()
	{
		synchronized (lock1)
		{
			try
			{
				Thread.sleep(1);
			}
			catch (InterruptedException e)
			{
				e.printStackTrace();
			}
			
			this.list1.add(random.nextInt(100));
		}
	}
	
	public void stageTwo()
	{
		synchronized (lock2)
		{
			try
			{
				Thread.sleep(1);
			}
			catch (InterruptedException e)
			{
				e.printStackTrace();
			}
			
			this.list2.add(random.nextInt(100));			
		}
	}
	
	public void processStageOne()
	{
		for(int i=0; i<1000; i++)
		{
			this.stageOne();
		}
	}
	
	public void processStageTwo()
	{
		for(int i=0; i<1000; i++)
		{
			this.stageTwo();
		}
	}
	
	public void process()
	{
		this.processStageOne();
		this.processStageTwo();
	}
	
	
	public static void main(String[] args) 
	{
		// TODO Auto-generated method stub
		System.out.println("Hello");
		Worker worker = new Worker();
		
		long start = System.currentTimeMillis();
		//worker.process();
		
		Thread t1 = new Thread(new Runnable() 
		{
			public void run()
			{
				//worker.process();
				worker.processStageOne();
			}
		});
		
		
		Thread t2 = new Thread(new Runnable() 
		{
			public void run()
			{
				//worker.process();
				worker.processStageTwo();
			}
		});
		
		
		t1.start();
		t2.start();
		try
		{
			t1.join();
			t2.join();
		}
		catch (InterruptedException e)
		{
			System.err.println(e.toString());
		}
		
		long end = System.currentTimeMillis();
		
		System.out.println("Time taken: " + (end-start));
		System.out.println("List1: " + worker.list1.size() + " List2: " + worker.list2.size());
	}
}
