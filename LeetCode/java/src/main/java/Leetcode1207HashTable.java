import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class Leetcode1207HashTable {
    public static void main(String[] args) {
        int[] arr1 = {1,2,2,1,1,3};
        int[] arr2 = {1,2};
        int[] arr3 = {-3,0,1,-3,1,1,1,-3,10,0};

        Map<Integer, Integer> testMap = new HashMap<>();
        for (int i : arr1) {
            testMap.put(i, testMap.getOrDefault(i, 0) + 1);
        }

        System.out.println(uniqueOccurrences(arr1));
        System.out.println(uniqueOccurrences(arr2));
        System.out.println(uniqueOccurrences(arr3));
    }

    //    Runtime: 1 ms, faster than 99.82% of Java online submissions for Unique Number of Occurrences.
    //    Memory Usage: 36.7 MB, less than 76.84% of Java online submissions for Unique Number of Occurrences.
    static boolean uniqueOccurrences(int[] arr) {
        boolean res = true;
        Map<Integer, Integer> occurrenceMap = new HashMap<>();

        for (int j : arr) {
            occurrenceMap.put(j, occurrenceMap.getOrDefault(j, 0) + 1);
        }

        Set<Integer> uniqueSet = new HashSet<>();
        for (int i : occurrenceMap.values()) {
            if (!uniqueSet.add(i)){
                res = false;
                break;
            }
        }
        return res;
    }

    static boolean uniqueOccurrences_discuss(int[] arr) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int num : arr) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }

        Set<Integer> set = new HashSet<>(map.values());
        return map.size() == set.size();
    }

}
