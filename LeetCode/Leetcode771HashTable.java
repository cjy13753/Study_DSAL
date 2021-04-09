import java.util.*;

public class Leetcode771HashTable {
    public static void main(String[] args) {
        int numOfJewels = numJewelsInStones("ab", "abaaa");
        System.out.println(numOfJewels);
    }

    // Runtime: 1 ms, faster than 66.32% of Java online submissions for Jewels and Stones.
    // Memory Usage: 37.6 MB, less than 28.69% of Java online submissions for Jewels and Stones.
    public static int numJewelsInStones(String jewels, String stones) {
        int jewelCounter = 0;

        Map<Character, Character> jewelsMap = new HashMap<>();

        for (int i = 0; i < jewels.length(); i++) {
            jewelsMap.put(jewels.charAt(i), jewels.charAt(i));
        }

        for (int i = 0; i < stones.length(); i++) {
            if (jewelsMap.containsKey(stones.charAt(i))) {
                jewelCounter++;
            }
        }

        return jewelCounter;

    }

    // Runtime: 1 ms, faster than 66.32% of Java online submissions for Jewels and Stones.
    // Memory Usage: 37.1 MB, less than 84.85% of Java online submissions for Jewels and Stones.
    public int numJewelsInStonesDiscuss(String J, String S) {
        int res = 0;
        Set<Character> setJ = new HashSet<>();
        for (char j: J.toCharArray())
            setJ.add(j);
        for (char s: S.toCharArray())
            if (setJ.contains(s)) res++;
        return res;
    }
}

