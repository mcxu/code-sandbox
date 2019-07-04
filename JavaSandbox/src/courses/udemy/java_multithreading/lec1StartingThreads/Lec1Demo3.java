package courses.udemy.java_multithreading.lec1StartingThreads;

public class Lec1Demo3 
{

	public static void main(String[] args) 
	{
		// TODO Auto-generated method stub
		Thread t1 = new Thread(new Runnable() 
			{
				@Override
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
		);
		
		t1.start();
	}

}
