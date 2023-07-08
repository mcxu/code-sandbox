package leetcode;

// import java.util.Collections;
// import java.util.stream.Collectors;
// import java.util.List;
// import java.util.ArrayList;
import java.util.*;

class LC49_GroupAnagrams {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>();
        //System.out.println("map: " + map);

        for(String str: strs) {
            // List<String> sortedStr = Collections.sort(str);
            char[] strChars = str.toCharArray();
            Arrays.sort(strChars);
            String sortedStr = new String(strChars);
            //System.out.println("sortedStr: " + sortedStr);

            if(map.keySet().contains(sortedStr)) {
                map.get(sortedStr).add(str);
            } else {
                map.put(sortedStr, new ArrayList<>(Arrays.asList(str)));
            }
        }

        List<List<String>> output = new ArrayList<List<String>>();
        for(String sortedStr: map.keySet()) {
            List<String> listOfWords = map.get(sortedStr);
            output.add(listOfWords);
        }
        return output;
    }
}