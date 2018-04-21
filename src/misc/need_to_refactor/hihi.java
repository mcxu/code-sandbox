package misc.need_to_refactor;
import java.util.Scanner;

public class hihi {
	
	static Scanner sc = new Scanner(System.in);
	
	public static void main(String args[]){
		double base, height;
		
		System.out.print("Enter the base: ");
		base = sc.nextDouble();
		System.out.print("Enter the height: ");
		height = sc.nextDouble();
		
		System.out.println("Area: " + (.5*base*height));
	}
	
	
}
