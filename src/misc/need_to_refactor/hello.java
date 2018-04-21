package misc.need_to_refactor;
public class hello{
	public static void main(String[] args){
		System.out.println("Hello Youtube!");
		
		String[] greeting = new String[3];
		greeting[0] = "oo ee oo a a";
		greeting[1] = "ting tang";
		greeting[2] = "walla walla bing bang!";
		
		for(int i=0; i<greeting.length; i++)
		{
			System.out.println(greeting[i]);
		}
		
		//alot to 1
		for(int j=10; j>0; j--)
		{
			for(int k=0; k<j; k++)
			{
				System.out.print("*");
			}
			System.out.print("\n");
		}
		
		//1 to alot
		for(int j=2; j<=10; j++)
		{
			for(int k=0; k<j; k++)
			{
				System.out.print("*");
			}
			System.out.print("\n");
		}
		
		double x = 9.997;
		int nx = (int)x;
		
		System.out.println("converted to an int is: " + nx);
		
		int num = 0;
		while(num < 10)
		{
			System.out.println(num);
			num++;
		}
		
		boolean state = true;
		System.out.print(state + "\n");
		
		final double val = 123.456;
		System.out.println(val + " " + nx);
		
		int foo = 1000;
		int fourthBitFromRight = (foo & 4)/4;
		System.out.println(fourthBitFromRight);
		
		String g = "Hello How Are You Doing?";
		System.out.println("before: " + g);
		System.out.println("length of g: " + g.length());
		
		int c1 = 0;
		int c2 = 0;
		char achar;
		while(c1 < g.length());
		{
			achar = g.charAt(c1);
			/*
			if(achar == ' ')
			{
				System.out.print("lol \n");
			}
			*/
			
			c1=c1+1;
		}
		
	}
}