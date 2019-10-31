package ctci5th.DataStructures;

import java.util.ArrayList;
import java.util.Arrays;

import ctci5th.util.stack.Stack;

public class Ch3StacksAndQueues 
{
    //Question 3.2: See ../util/stack/Stack3p2.java

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

    //Question 3.5: ../util/queue/MyQueue.java
    
    //sort stack in ascending order
    public Stack<Integer> question3p6(Stack<Integer> stackA)
    {
        if(stackA == null || stackA.isEmpty()) 
        {
            return stackA;
        }
        
        Stack<Integer> stackB = new Stack<Integer>();
        Integer temp = null;
        System.out.println("stackA initial top: " + stackA.peek());
        stackB.push(stackA.pop()); //move top value from stackA to stackB
        while(!stackA.isEmpty())
        {
            temp = stackA.pop();
            System.out.println("temp: " + temp);
            
//            //case that temp is <= top of stackB
//            if(temp <= stackB.peek()) 
//            {
//                System.out.println("if statement");
//                stackB.push(temp);
//            } 
//            //case that temp is > top of stackB
//            else 
//            {
//                System.out.println("else statement");
//                while(!stackB.isEmpty() && temp > stackB.peek()) 
//                {
//                    stackA.push(stackB.pop());
//                }
//                stackB.push(temp);
//            }
            //note: it can be seen that the 'if' is actually not needed,
            //so we have:
            while(!stackB.isEmpty() && temp > stackB.peek()) 
            {
                stackA.push(stackB.pop());
            }
            stackB.push(temp);
        }
        
        //move values from stackB into stackA for greatest value on top in A
        while(!stackB.isEmpty()) 
        {
            int b = stackB.pop();
            stackA.push(b);
            System.out.println("stackB item: " + b);
        }
        
        return stackA;
    }
    
    public void testQuestion3p6()
    {
        Stack<Integer> s = new Stack<Integer>();
        System.out.println("testQuestion3p6: s address: " + s);
        for(int i=10; i >= 1; i--)
        {
            s.push(i);
        }
        
        s = question3p6(s);
        
        while(!s.isEmpty()) {
            System.out.println("testQuestion3p6: s: " + s.pop());
        }
        System.out.println("testQuestion3p6: verify s address: " + s);
    }
    
    
    public void testQuestion3p6_2()
    {
        Stack<Integer> s = new Stack<Integer>();
        System.out.println("testQuestion3p6_2: s address: " + s);
        s.push(2);
        s.push(1);
        s.push(4);
        s.push(3);
        s.push(5);
        
        s = question3p6(s);
        
        while(!s.isEmpty()) {
            System.out.println("testQuestion3p6_2: s: " + s.pop());
        }
        System.out.println("testQuestion3p6_2: verify s address: " + s);
    }
    
    
    public static void main(String[] args) 
    {
        Ch3StacksAndQueues ch3 = new Ch3StacksAndQueues();
        //ch3.testQuestion3p6();
        //ch3.testQuestion3p6_2();
        ch3.testHanoi();
    }

}

