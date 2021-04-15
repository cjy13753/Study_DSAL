import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class Leetcode1160HashTable {
    public static void main(String[] args) {

        String[] words1 = {"cat","bt","hat","tree"};
        String chars1 = "atach";

        String[] words2 = {"hello","world","leetcode"};
        String chars2 = "welldonehoneyr";

        System.out.println(countCharacters(words1, chars1));
        System.out.println(countCharacters(words2, chars2));

        System.out.println(countCharactersMyTry2(words1, chars1));
        System.out.println(countCharactersMyTry2(words2, chars2));
    }

    // Runtime: 46 ms, faster than 16.72% of Java online submissions for Find Words That Can Be Formed by Characters.
    // Memory Usage: 39.4 MB, less than 66.04% of Java online submissions for Find Words That Can Be Formed by Characters.
    static int countCharacters(String[] words, String chars) {
        Map<Character, Integer> charsMap = new HashMap<>();
        for (Character c : chars.toCharArray()) {
            charsMap.put(c, charsMap.getOrDefault(c, 0) + 1);
        }

        int count = 0;

        for (String word : words) {
            Map<Character, Integer> wordMap = new HashMap<>();
            for (Character c : word.toCharArray()) {
                wordMap.put(c, wordMap.getOrDefault(c, 0) + 1);
            }

            int match = 0;
            for (Character c : wordMap.keySet()) {
                if (charsMap.containsKey(c)) {
                    if (wordMap.get(c) <= charsMap.get(c)) {
                        match++;
                    } else {
                        break;
                    }
                } else {
                    break;
                }
            }

            if (match == wordMap.size()) {
                count += word.length();
            }
        }

        return count;
    }

    // Runtime: 11 ms, faster than 52.43% of Java online submissions for Find Words That Can Be Formed by Characters.
    // Memory Usage: 39.5 MB, less than 50.15% of Java online submissions for Find Words That Can Be Formed by Characters.
    static int countCharactersMyTry2(String[] words, String chars) {
        int[] charsCount = new int[26];
        chars.chars().forEach(c -> ++charsCount[c - 'a']);

        int count = 0;

        for (String word : words) {
            int[] wordCount = new int[26];
            word.chars().forEach(c -> ++wordCount[c - 'a']);

            int verification = 0;
            for (int i = 0; i < 26; i++) {
                if (wordCount[i] > charsCount[i]) {
                    verification++;
                    break;
                }
            }
            if (verification == 0) {
                count += word.length();
            }
        }

        return count;
    }

    // Runtime: 8 ms, faster than 65.98% of Java online submissions for Find Words That Can Be Formed by Characters.
    // Memory Usage: 39.7 MB, less than 26.98% of Java online submissions for Find Words That Can Be Formed by Characters.
    static int countCharactersDiscuss1(String[] words, String chars) {
        int count = 0;
        int[] seen = new int[26];
        //Count char of Chars String
        for (char c : chars.toCharArray())
            seen[c - 'a']++;
        // Comparing each word in words
        for (String word : words) {
            // simple making copy of seen arr
            int[] tSeen = Arrays.copyOf(seen, seen.length);
            int Tcount = 0;
            for (char c : word.toCharArray()) {
                if (tSeen[c - 'a'] > 0) {
                    tSeen[c - 'a']--;
                    Tcount++;
                }
            }
            if (Tcount == word.length())
                count += Tcount;
        }
        return count;
    }

    // Runtime: 7 ms, faster than 74.08% of Java online submissions for Find Words That Can Be Formed by Characters.
    // Memory Usage: 39.5 MB, less than 50.15% of Java online submissions for Find Words That Can Be Formed by Characters.
    static int countCharactersDiscuss2(String[] words, String chars) {
        int cnt[] = new int[26], ans = 0;
        chars.chars().forEach(c -> ++cnt[c - 'a']); // count chars.

    outer:
        for (String w : words) {
            int[] count = cnt.clone();
            for (char c : w.toCharArray())
                if (--count[c - 'a'] < 0) // not enough, continue next word in words.
                    continue outer;
            ans += w.length();
        }
        return ans;

    }

    // Runtime: 30 ms, faster than 26.51% of Java online submissions for Find Words That Can Be Formed by Characters.
    // Memory Usage: 39.7 MB, less than 26.98% of Java online submissions for Find Words That Can Be Formed by Characters.
    static int countCharactersDiscuss3(String[] words, String chars) {
        HashMap<Character, Integer> countMap = new HashMap<>();
        for (char c : chars.toCharArray()) {
            countMap.put(c, countMap.getOrDefault(c, 0) + 1);
        }
        int res = 0;
        HashMap<Character, Integer> copyMap;
        for (String word : words) {
            copyMap = (HashMap<Character, Integer>) countMap.clone();
            boolean fail = false;
            for (char c : word.toCharArray()) {
                if (copyMap.get(c) == null || copyMap.get(c) <= 0) {
                    fail = true;
                    break;
                } else {
                    copyMap.put(c, copyMap.get(c) - 1);
                }
            }
            if (!fail) res += word.length();
        }
        return res;
    }
}
