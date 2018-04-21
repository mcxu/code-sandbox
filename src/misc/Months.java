package misc;

import java.util.Calendar;
import java.util.GregorianCalendar;

public class Months 
{
	public static void main(String[] args) 
	{
		// TODO Auto-generated method stub
		Calendar startDate = new GregorianCalendar(2010,5,8);
		Calendar endDate = new GregorianCalendar(2011,3,1);
		
		//Get necessary information from dates
		int numYrs = endDate.get(Calendar.YEAR) - startDate.get(Calendar.YEAR);
		int numMo = endDate.get(Calendar.MONTH) - startDate.get(Calendar.MONTH);
		int numDy = endDate.get(Calendar.DAY_OF_MONTH) - startDate.get(Calendar.DAY_OF_MONTH);
		
		//Calculate total number of months
		int elapsedMo = numYrs * 12 + numMo;
		
		System.out.println(elapsedMo);
		
	}

}
