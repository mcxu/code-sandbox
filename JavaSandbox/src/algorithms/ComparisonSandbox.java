package algorithms;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Hashtable;

public class ComparisonSandbox 
{
    /**
     * Algorithm to find all common elements in 2 sorted lists of numbers. For
     * example, 2,5,5,5 and 2,2,3,5,5,7 should give 2,5,5.
     * http://www.careercup.com/question?id=4886983698546688
     * @param aList
     * @param bList
     * @return
     */
    public List<Integer> commonElementsInTwoSortedLists(List<Integer> aList, List<Integer> bList) 
    {
        List<Integer> commonElementsList = new ArrayList<Integer>();
        int aIndex = 0; // index marker for aList
        int bIndex = 0; // index marker for bList

        while (aIndex < aList.size() && bIndex < bList.size()) 
        {
            if (aList.get(aIndex) < bList.get(bIndex)) 
            {
                aIndex += 1;
            } 
            else if (aList.get(aIndex) > bList.get(bIndex)) 
            {
                bIndex += 1;
            } 
            else if (aList.get(aIndex) == bList.get(bIndex)) 
            {
                // found a common
                commonElementsList.add(aList.get(aIndex));
                aIndex += 1;
                bIndex += 1;
            }
            System.out.println("aIndex=" + aIndex + "	bIndex=" + bIndex);
        }

        return commonElementsList;
    }

    public void test_commonElementsInTwoSortedLists() 
    {
        // List<Integer> aList = new ArrayList<Integer>(Arrays.asList(2,5,5,5));
        // List<Integer> bList = new ArrayList<Integer>(Arrays.asList(2,2,3,5,5,7));
        List<Integer> aList = new ArrayList<Integer>(Arrays.asList(1, 2, 3, 4));
        List<Integer> bList = new ArrayList<Integer>(Arrays.asList(2, 4, 9, 10));
        List<Integer> commonElementsList = new ArrayList<Integer>();

        commonElementsList = this.commonElementsInTwoSortedLists(aList, bList);
        System.out.println(commonElementsList.toString());
    }

    public static void main(String[] args) 
    {
        ComparisonSandbox cbox = new ComparisonSandbox();
        cbox.test_commonElementsInTwoSortedLists();
    }

}
