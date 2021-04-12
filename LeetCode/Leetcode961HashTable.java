import java.util.HashMap;
import java.util.Map;

public class Leetcode961HashTable {
    public static void main(String[] args) {
        int[] A1 = {1,2,3,3};
        int[] A2 = {2,1,2,5,3,2};
        int[] A3 = {5,1,5,2,5,3,5,4};

        System.out.println(repeatedNTimes(A1));
        System.out.println(repeatedNTimes(A2));
        System.out.println(repeatedNTimes(A3));
    }

    // Runtime: 0 ms, faster than 100.00% of Java online submissions for N-Repeated Element in Size 2N Array.
    // Memory Usage: 39.8 MB, less than 60.71% of Java online submissions for N-Repeated Element in Size 2N Array.
    public static int repeatedNTimes(int[] A) {
        Map<Integer, Integer> AMap = new HashMap<>();
        int res = 0;

        for (int i = 0; i < A.length; i++) {
            AMap.put(A[i], AMap.getOrDefault(A[i], 0) + 1);
            if (AMap.get(A[i]) == 2) {
                res = A[i];
                break;
            }
        }

        return res;
    }
}
