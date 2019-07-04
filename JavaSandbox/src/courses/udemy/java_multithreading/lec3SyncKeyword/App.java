package courses.udemy.java_multithreading.lec3SyncKeyword;
import java.lang.Runnable;

public class App 
{
	private int count = 0;
	
	public synchronized void increment()
	{
		this.count = this.count + 1;
	}
	
	public void doWork()
	{
		Thread t1 = new Thread(new Runnable() 
		{
			public void run()
			{
				for(int i=0; i<10; i++)
				{
					//count = count + 1;
					increment();
				}
			}
		});
		
		Thread t2 = new Thread(new Runnable() 
		{
			public void run()
			{
				for(int i=0; i<10; i++)
				{
					//count = count + 1;
					increment();
				}
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
			e.printStackTrace();
		}
		
		
		System.out.println("Count is: " + count);
	}
	
	public static void main(String[] args)
	{
		App app = new App();
		app.doWork();
	}
	
}
