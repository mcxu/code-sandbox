package courses.udemy.java_multithreading.lec1StartingThreads;

class Runner2 implements Runnable
{
    public void run()
    {
        for(int i=0; i<10; i++)
        {
            System.out.println("Hello " + i);
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
}

public class Lec1Demo2 
{
	public static void main(String[] args) 
	{
		// TODO Auto-generated method stub
		Thread t1 = new Thread(new Runner2());
		Thread t2 = new Thread(new Runner2());
		
		t1.start();
		t2.start();
	}
}
