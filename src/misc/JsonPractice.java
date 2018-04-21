package misc;

import java.io.File;
import java.io.IOException;
import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.Scanner;

import org.json.JSONArray;
import org.json.JSONObject;

public class JsonPractice 
{
	String jsonText = null;
	JSONObject jsonObj;
	JSONArray transactionsArray;
	int transArrLength = 0;
	
	public JsonPractice()
	{
		
	}
	
	/**
	 * Read json from file as a String.
	 * @throws IOException 
	 */
	public void jsonRead() throws IOException
	{
		String path = "./jsonFiles/transactions.json";
		File file = new File(path);
		Scanner scanner = new Scanner(file);
		this.jsonText = scanner.useDelimiter("\\Z").next();
		//System.out.println(this.jsonText); //print out the text
	}
	
	/**
	 * Convert the Json string that was read into an actual Json object.
	 */
	public void convertJsonStrToObj()
	{
		if(this.jsonText != null)
		{
			//Convert json string to json object
			this.jsonObj = new JSONObject(this.jsonText);
		}
		else
		{
			throw new IllegalArgumentException("this.jsonText is null.");
		}
	}
	
	/**
	 * Perform the calculations:
	 * 	Debit: add
	 * 	Credit: subtract
	 */
	public void performCalculations()
	{
		this.transactionsArray = this.jsonObj.getJSONArray("transactions");
		this.transArrLength = transactionsArray.length();
		System.out.println(this.transactionsArray); //print out transactions list
		
		JSONObject transaction = null;
		String typeStr = null;
		String amtStr = null;
		BigDecimal amtBD = new BigDecimal("0");
		System.out.println("performCalculations");
		for(int i=0; i<this.transArrLength; i++)
		{
			System.out.println("------ top of for loop ------");
			transaction = this.transactionsArray.getJSONObject(i);
			System.out.println("individual transaction: " + transaction);
			typeStr = transaction.getString("type");
			System.out.println("type: " + typeStr);
			amtStr = transaction.getString("amount");
			System.out.println("amount: " + amtStr);
			
			if(typeStr.contains("DEBIT"))
			{
				System.out.println("typeStr == DEBIT");
				amtBD = amtBD.add(new BigDecimal(amtStr));
			}
			else if(typeStr.contains("CREDIT"))
			{
				System.out.println("typeStr == CREDIT");
				amtBD = amtBD.subtract(new BigDecimal(amtStr));
			}
		}
		//Display the final calculated amount
		System.out.println("final calculated amount= " + amtBD);
	}
	
	
	public static void main(String[] args) 
	{
		JsonPractice jp = new JsonPractice();
		try
		{
			jp.jsonRead();
			jp.convertJsonStrToObj();
			jp.performCalculations();
		}
		catch (IOException ex)
		{
			System.err.println(ex.getMessage());
		}
	}
}
