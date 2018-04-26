package misc;

import java.lang.Thread;

/**
 *
 * @author Michael
 */
public class CalculationThread extends Thread
{
    private final String label;
    private final int delay;
    private final int repetitions;
    private final int incrementer; 
    
    public CalculationThread(String label, int delay, int repetitions, int incrementer)
    {
        this.label = label;
        this.delay = delay;
        this.repetitions = repetitions;
        this.incrementer = incrementer;
    }
    
    public void run()
    {
        
    }

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) 
    {
        // TODO code application logic here
    }
    
}
