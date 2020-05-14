package ctci5th.DataStructures.Ch3StacksQueues;

import ctci5th.util.stack.Stack;

public class Ch3q6_SortStackAscending {
    
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
        Ch3q6_SortStackAscending prob = new Ch3q6_SortStackAscending();
        //prob.testQuestion3p6();
        prob.testQuestion3p6_2();
    }

}
