package misc.need_to_refactor;

public class testing {	
	
	public static void hex2int(String hex_value)
	{
		System.out.println("Hello");
	}
	
	
	public static void main(String[] args)
	{
		String reg_hex_val = "1B";
		int translation = 0;
		
		switch(reg_hex_val)
		{	
			case "1A": translation = -3; break;
			case "1B": translation = -2; break;	
		}
		
		System.out.println("Translated value: " + translation);
	}
	
	
}