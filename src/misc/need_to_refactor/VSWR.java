package misc.need_to_refactor;

import java.io.Console;

public class VSWR {
	public static void main(String [] args)
	{
		System.out.println("Enter parameters: ");
		
		Console c = System.console();
		
		String Z_0 = c.readLine("Z_0 = ");
		//System.out.println("The impedance you entered was a string converted to this double: ");
		double Z_0_doub = Double.parseDouble(Z_0);
		System.out.println("User entered Z_0 = " + Z_0_doub);
		
		String Z_L_re = c.readLine("Z_L(Re) = ");
		double Z_L_re_doub = Double.parseDouble(Z_L_re);
		String Z_L_im = c.readLine("Z_L(Im) = ");
		double Z_L_im_doub = Double.parseDouble(Z_L_im);
		
		String sign;
		if(Z_L_im_doub < 0)
			sign = " - j";
		else
			sign = " + j";
			
		System.out.println("User entered for Z_L = " + Z_L_re_doub + sign + Math.abs(Z_L_im_doub));
		
		int i = 0;
	}
		
}