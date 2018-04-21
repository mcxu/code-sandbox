/* 
 * http://www.careercup.com/question?id=15853663
 * http://stackoverflow.com/questions/16963405/printing-hello-and-world-multiple-times-using-two-threads-in-java
 */

package misc;

class HelloWorldRunner extends Thread
{
	String word;
	int sleep; //milliseconds
	int iterations;
	int counter;
	
	public HelloWorldRunner(String word, int sleep, int iterations)
	{
		this.word = word;
		this.sleep = sleep;
		this.iterations = iterations;
		counter = 0;
	}
	
	public synchronized void run()
	{
		while(this.counter < this.iterations)
		{
			System.out.println(this.word);
			this.counter += 1;
			try
			{
				Thread.sleep(this.sleep);
			}
			catch(InterruptedException ie)
			{
				ie.printStackTrace();
			}
		}
	}
}

public class HelloWorldThreading
{
	
	public static void main(String[] args) 
	{
		// TODO Auto-generated method stub
		HelloWorldRunner thread1 = new HelloWorldRunner("Hello", 1000, 5);
		HelloWorldRunner thread2 = new HelloWorldRunner("World", 1000, 5);
		
		thread1.start();
		thread2.start();
		
	}

}
