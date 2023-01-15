/*
https://leetcode.com/problems/intersection-of-three-sorted-arrays/

1213. Intersection of 3 sorted arrays

Complexity analysis of arraysIntersection only.
Time complexity: 
O(n) where n is the number of values in the smallest array.

Space complexity:
O(n) 
*/

package leetcode;

import java.util.List;
import java.util.Map;
import java.util.HashMap;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Set;
import java.util.Arrays;
import java.util.stream.Collectors;

class lc1213_IntersectionOf3SortedArrays {
    public List<Integer> arraysIntersection(int[] arr1, int[] arr2, int[] arr3) {
        Map<Integer, Integer> freqMap = new HashMap<Integer, Integer>();

        for(int a : arr1) {
            freqMap.putIfAbsent(a, 1);
        }

        for(int b : arr2) {
            if(freqMap.containsKey(b)){
                freqMap.computeIfPresent(b, (key, val) -> val + 1);
            }
        }

        for(int c : arr3) {
            if(freqMap.containsKey(c)) {
                freqMap.computeIfPresent(c, (key, val) -> val + 1);
            }
        }

        List<Integer> commonNums = new ArrayList<Integer>();
        for(int k : freqMap.keySet()) {
            if(freqMap.get(k) == 3) {
                commonNums.add(k);
            }
        }
        Collections.sort(commonNums);
        return commonNums;
    }

    public List<Integer> arraysIntersection2(int[] arr1, int[] arr2, int[] arr3) {
        Set<Integer> arr1Set = Arrays.stream(arr1).boxed().collect(Collectors.toSet());
        Set<Integer> arr2Set = Arrays.stream(arr2).boxed().collect(Collectors.toSet());
        Set<Integer> arr3Set = Arrays.stream(arr3).boxed().collect(Collectors.toSet());
        arr1Set.retainAll(arr2Set);
        arr1Set.retainAll(arr3Set);
        
        List<Integer> output = new ArrayList<Integer>(arr1Set);
        Collections.sort(output);
        return output;
    }
}