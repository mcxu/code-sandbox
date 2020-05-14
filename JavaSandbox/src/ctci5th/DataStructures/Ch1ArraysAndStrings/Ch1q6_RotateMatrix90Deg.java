/**
* Rotate NxN matrix 90 degrees in place in CCW direction
*/
package ctci5th.DataStructures.Ch1ArraysAndStrings;
import ctci5th.util.AlgUtils;

public class Ch1q6_RotateMatrix90Deg
{
    public String[][] rotateSqMatrix90DegCCW(String[][] matrix)
    {
        final int maxInd = matrix.length-1;
        
        String[] coArray = new String[3]; 
        /* stores the carry over before shift
            0: carry over from left col
            1: carry over from bottom row 
            2: carry over from right col
        */
    
        boolean cor = false; //carry over read, has stored the item that will be carried over
        
        //for each layer of the matrix; like an onion; lyr means coords (0,0), (1,1), (2,2)...
        for(int lyr=0; lyr<(matrix.length/2); lyr++)
        {
            //int lyr = 0; // test
            //number of times to shift for a given layer
            for(int shiftCt=lyr; shiftCt < maxInd-lyr; shiftCt++)
            {
                //perform a 1-item shift for each side
                System.out.println("##### lyr=" + lyr + "   shiftCt=" + shiftCt + " #####");
                
                //left col shift down
                for(int i=maxInd-lyr-1; i >= lyr; i--)
                {
                    if(cor == false)
                    {
                        coArray[0] = matrix[i+1][lyr];
                        cor = true;
                    }
                    matrix[i+1][lyr] = matrix[i][lyr];
                }
                cor = false;
                System.out.print("after left col shift down:\n");
                AlgUtils.printMatrix(matrix);
                System.out.println("coArray[0]: " + coArray[0]);
                
                //bottom row shift right
                for(int i=maxInd-lyr-1; i >= lyr; i--)
                {
                    if(cor == false)
                    {
                        coArray[1] = matrix[maxInd-lyr][i+1];
                        cor = true;
                    }
                    matrix[maxInd-lyr][i+1] = matrix[maxInd-lyr][i];
                }
                matrix[maxInd-lyr][lyr+1] = coArray[0]; //add carry over from left col
                cor = false;
                System.out.print("after bottom row shift right:\n");
                AlgUtils.printMatrix(matrix);
                System.out.println("coArray[1]: " + coArray[1]);
                
                //right col shift up
                for(int i=lyr; i <= maxInd-lyr-1; i++)
                {
                    if(cor == false)
                    {
                        coArray[2] = matrix[lyr][maxInd-lyr];
                        cor = true;
                    }
                    matrix[i][maxInd-lyr] = matrix[i+1][maxInd-lyr];
                }
                matrix[maxInd-lyr-1][maxInd-lyr] = coArray[1]; //add carry over from bottom row
                cor = false;
                System.out.print("after right col shift up:\n");
                AlgUtils.printMatrix(matrix);
                System.out.println("coArray[2]: " + coArray[2]);
                
                //top row shift left
                for(int i=lyr; i <= maxInd-lyr-1; i++)
                {
                    matrix[lyr][i] = matrix[lyr][i+1];
                }
                matrix[lyr][maxInd-lyr-1] = coArray[2]; //add carry over from right col
                System.out.print("after top row shift left:\n");
                AlgUtils.printMatrix(matrix);
            }
        }
        
        return matrix;
    }
    
    public void test1()
    {
        String[][] matrix1 = new String[][] {
            {"a","b","c","d"},
            {"e","f","g","h"},
            {"i","j","k","l"},
            {"m","n","o","p"},
        };
        
        String[][] matrix2 = new String[][] {
            {"^"," "," "," "," ","Y"," "," "," ","$"},
            {" "," "," "," ","@","@"," "," "," "," "},
            {" "," "," ","@"," "," ","@"," "," "," "},
            {" "," ","@"," "," "," "," ","@"," "," "},
            {"A","@","@","@"," "," ","@","@","@","L"},
            {" "," "," ","@"," "," ","@"," "," "," "},
            {" "," "," ","@"," "," ","@"," "," "," "},
            {" "," "," ","@"," "," ","@"," "," "," "},
            {" "," "," ","@","@","@","@"," "," "," "},
            {"!"," "," "," ","V"," "," "," "," ","#"}
        };
        
        System.out.println("before rotate:");
        AlgUtils.printMatrix(matrix2);
        String[][] out1 = rotateSqMatrix90DegCCW(matrix2); //point left
    //        out1 = rotateSqMatrix90DegCCW(out1); //point down
    //        out1 = rotateSqMatrix90DegCCW(out1); //point right
        System.out.print("end result:\n");
        AlgUtils.printMatrix(out1);
    }

    public static void main(String[] args)
    {
        Ch1q6_RotateMatrix90Deg prog = new Ch1q6_RotateMatrix90Deg();
        prog.test1();
    }
}
