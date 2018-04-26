package misc;

/**
 *
 * @author Michael
 */
public class StringOperations 
{
    
    public String reverseString(String inputString)
    {
        int inputStringLength = inputString.length();
        
        String reversedString = "";
        for(int i=inputStringLength-1; i>=0; i--)
        {
            reversedString = reversedString + inputString.charAt(i);
        }
        return reversedString;
    }
    
    
    /////////////// Helpers /////////////////
    
    
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) 
    {
        // TODO code application logic here
        StringOperations so = new StringOperations();
        String test = "The quick brown fox jumped over.";
        String revStr = so.reverseString(test);
        System.out.println("reversed string " + revStr);
    }
    
}
