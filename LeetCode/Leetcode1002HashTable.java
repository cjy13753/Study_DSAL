import java.util.*;

// #helpful, refer to discuss answers below
public class Leetcode1002HashTable {
    public static void main(String[] args) {
        String[] A = {"bella", "label", "roller"};
        String[] B = {"cool","lock","cook"};

        System.out.println(commonChars(A));
        System.out.println(commonChars(B));
    }

    // Runtime: 27 ms, faster than 5.09% of Java online submissions for Find Common Characters.
    // Memory Usage: 39.5 MB, less than 22.73% of Java online submissions for Find Common Characters.
    public static List<String> commonChars(String[] A) {
        Map<String, HashMap<Integer, Integer>> charCount = new HashMap<>();

        for (int j = 0; j < A.length; j++) {
            String s = A[j];
            for (int i = 0; i < s.length(); i++) {
                String stringS = Character.toString(s.charAt(i));

                charCount.putIfAbsent(stringS, new HashMap<>());
                charCount.get(stringS).putIfAbsent(j, 0);
                charCount.get(stringS).put(j, charCount.get(stringS).get(j) + 1);
            }
        }

        List<String> res = new ArrayList<>();
        for (String c : charCount.keySet()) {
            if (charCount.get(c).size() == A.length) {
                for (int i = 0; i < Collections.min(charCount.get(c).values()); i++) {
                    res.add(c);
                }
            }
        }

        return res;
    }

    // Runtime: 8 ms, faster than 37.43% of Java online submissions for Find Common Characters.
    // Memory Usage: 38.9 MB, less than 89.03% of Java online submissions for Find Common Characters.
    public List<String> commonChars_discuss1(String[] A) {
        List<String> ans = new ArrayList<>();
        int[] count = new int[26];
        Arrays.fill(count, Integer.MAX_VALUE);
        for (String str : A) {
            int[] cnt = new int[26];
            str.chars().forEach(c -> ++cnt[c - 'a']); // count each char's frequency in string str.
            for (int i = 0; i < 26; ++i) { count[i] = Math.min(cnt[i], count[i]); } // update minimum frequency.
        }
        for (char c = 'a'; c <= 'z'; ++c) {
            while (count[c - 'a']-- > 0) { ans.add("" + c); }
        }
        return ans;
    }

    // Runtime: 1 ms, faster than 100.00% of Java online submissions for Find Common Characters.
    // Memory Usage: 39.1 MB, less than 52.65% of Java online submissions for Find Common Characters.
    public List<String> commonChars_discuss2(String[] A) {
        int[] last = count(A[0]);
        for (int i = 1; i < A.length; i++) {
            last = intersection(last, count(A[i]));
        }
        List<String> arr = new ArrayList<>();
        for (int i = 0; i < 26; i++) {
            if (last[i] != 0) {
                char a = 'a';
                a += i;
                String s = String.valueOf(a);
                while (last[i] > 0) {
                    arr.add(s);
                    last[i]--;
                }
            }
        }
        return arr;
    }

    int[] intersection(int[] a, int[] b) {
        int[] t = new int[26];
        for (int i = 0; i < 26; i++) {
            t[i] = Math.min(a[i], b[i]);
        }
        return t;
    }

    int[] count(String str) {
        int[] t = new int[26];
        for (char c : str.toCharArray()) t[c - 'a']++;
        return t;
    }

    // Runtime: 16 ms, faster than 13.91% of Java online submissions for Find Common Characters.
    // Memory Usage: 39.2 MB, less than 52.65% of Java online submissions for Find Common Characters.
    public List<String> commonChars_discuss3(String[] A) {
        Map<Character,Integer> map=new HashMap<>();
        for(char c:A[0].toCharArray()){
            map.put(c,map.getOrDefault(c,0)+1);
        }

        for(int i=1;i<A.length;i++){
            Map<Character,Integer> tmp=new HashMap<>();
            for(int j=0;j<A[i].length();j++){
                char c=A[i].charAt(j);
                if(map.containsKey(c) && map.get(c)>0){
                    tmp.put(c,tmp.getOrDefault(c,0)+1);
                    map.put(c,map.get(c)-1);
                }
            }
            map=tmp;
            if(map.size()==0)break;
        }
        List<String> res=new ArrayList<>();
        for(Character c:map.keySet()){
            for(int k=0;k<map.get(c);k++){
                res.add(""+c);
            }
        }
        return res;
    }
}
