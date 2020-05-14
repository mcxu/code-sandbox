/*
 * Question 1.7: Algorithm such that if an element in an MxN matrix is 0, 
 * its entire row and column are set to 0.
 */
package ctci5th.DataStructures.Ch1ArraysAndStrings;
import java.util.Arrays;
import java.util.ArrayList;
import ctci5th.util.AlgUtils;

public class Ch1q7_IfMxNMatrix0 
{
    public Integer[][] setRowAndColTo0(Integer[][] matrix)
    {
        ArrayList<int[]> initialZerosList = new ArrayList<>();
        
        // Identify all initial zeros
        System.out.print("entered setRowAndColTo0\n");
        for(int row=0; row < matrix.length; row++)
        {
            for(int col=0; col < matrix[0].length; col++)
            {
                int currInt = matrix[row][col];
                if(currInt == 0)
                {
                    initialZerosList.add(new int[] {row, col});
                }
            }
        }
        System.out.println("initialZerosList after identifying:\n" + initialZerosList);
        
        for(int k=0; k < initialZerosList.size(); k++)
        {
            int[] coord = initialZerosList.remove(k);
            
            System.out.println("coord: " + Arrays.toString(coord));
            //change a column to 0
            for(int m=0; m < matrix.length; m++)
            {
                matrix[m][coord[1]] = 0;
            }
            
            //change a row to 0
            for(int n=0; n < matrix[0].length; n++)
            {
                matrix[coord[0]][n] = 0;
            }
        }

        return matrix;
    }

    public void test1()
    {
        Integer[][] test1 = new Integer[][] {
            {1,1,1,1,1,1,1,1,1,1,1,9,1,1,1},
            {1,1,5,1,1,1,1,1,1,1,1,9,1,1,1},
            {1,1,1,1,1,1,1,1,1,1,1,9,1,1,1},
            {1,0,1,1,1,8,1,1,7,1,1,9,1,1,1},
            {9,9,9,9,9,9,9,9,9,9,9,9,9,9,9},
            {1,1,1,1,1,1,1,1,1,1,1,9,1,1,1},
            {1,1,1,1,1,1,1,1,3,1,1,9,0,1,1},
            {1,1,9,1,0,1,1,1,1,1,1,9,1,1,1},
            {1,1,1,1,1,1,1,1,1,1,1,9,1,5,1},
            {1,1,1,8,1,1,1,1,1,1,1,9,1,1,1},
            {1,1,4,1,1,1,0,1,1,1,1,9,1,1,1}
        };
        
        System.out.println("before setRowAndColTo0:");
        AlgUtils.printMatrix(test1);
        Integer[][] result = setRowAndColTo0(test1);
        System.out.println("after setRowAndColTo0:");
        AlgUtils.printMatrix(result);
    }

    public static void main(String[] args)
    {
        Ch1q7_IfMxNMatrix0 prob = new Ch1q7_IfMxNMatrix0();
        prob.test1();
    }
}