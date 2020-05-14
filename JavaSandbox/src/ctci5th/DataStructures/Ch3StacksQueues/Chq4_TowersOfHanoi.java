package ctci5th.DataStructures.Ch3StacksQueues;

import java.util.ArrayList;
import java.util.Arrays;

public class Chq4_TowersOfHanoi 
{
    //Question 3.4: Towers of Hanoi
    //n:num discs, f:from, a:auxilary, t:to
    //returns: list of [from, to] moves
    public ArrayList<String[]> hanoi(int n, String f, String a, String t) 
    {
        ArrayList<String[]> moves = new ArrayList<>();
        this.hanoiHelper(n, f, a, t, moves);
        return moves;
    }

    public void hanoiHelper(int n, String f, String a, String t, ArrayList<String[]> moves) 
    {
        if(n == 0) {
            return;
        }
        //moves A->B (assuming f->t movement from root call, then f->a is A->B)
        hanoiHelper(n-1, f, t, a, moves); 
        //moves A->C (assuming f->t movement from root call, then f->t is A->C)
        moves.add(new String[]{f, t}); 
        //moves B->C (assuming f->t movement from root call, then a->t is B->C)
        hanoiHelper(n-1, a, f, t, moves); 
    }

    public void testHanoi()
    {
        ArrayList<String[]> result = hanoi(4, "A", "B", "C");
        for(int i=0; i<result.size(); i++)
        {
            System.out.printf("move %s: %s\n", i+1, Arrays.asList(result.get(i)));
        }
    }
    
    public static void main(String[] args) 
    {
        Chq4_TowersOfHanoi prob = new Chq4_TowersOfHanoi();
        prob.testHanoi();
    }
    
}
