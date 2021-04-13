import java.util.*;
import java.util.regex.Pattern;

public class Leetcode811HashTable {
    public static void main(String[] args) {
        String[] cpdomains1 = {"900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"};
        String[] cpdomains2 = {"9001 discuss.leetcode.com"};

        System.out.println(subdomainVisits(cpdomains1));
        System.out.println(subdomainVisits(cpdomains2));

    }
    // Runtime: 25 ms, faster than 32.94% of Java online submissions for Subdomain Visit Count.
    // Memory Usage: 40.8 MB, less than 26.46% of Java online submissions for Subdomain Visit Count.
    public static List<String> subdomainVisits(String[] cpdomains) {
        Map<String, Integer> visitCountForSubdomain = new HashMap<>();

        for (String str : cpdomains) {
            String[] spaceSeparatedArr = str.split(Pattern.quote(" "));
            int countVisited = Integer.parseInt(spaceSeparatedArr[0]);
            String[] periodSeparatedArr = spaceSeparatedArr[1].split(Pattern.quote("."));

            List<String> subdomainStringList = new ArrayList<>();

            for (int i = 0; i < periodSeparatedArr.length; i++) {
                StringBuilder s = new StringBuilder(periodSeparatedArr[i]);
                for (int j = i + 1; j < periodSeparatedArr.length; j++) {
                    s.append(".").append(periodSeparatedArr[j]);
                }
                subdomainStringList.add(s.toString());
            }

            for (String s : subdomainStringList) {
                visitCountForSubdomain.put(s, visitCountForSubdomain.getOrDefault(s, 0) + countVisited);
            }
        }

        List<String> res = new ArrayList<>();
        for (String subdomain : visitCountForSubdomain.keySet()) {
            res.add(visitCountForSubdomain.get(subdomain) + " " + subdomain);
        }

        return res;
    }

    // Runtime: 14 ms, faster than 85.25% of Java online submissions for Subdomain Visit Count.
    // Memory Usage: 40.2 MB, less than 45.19% of Java online submissions for Subdomain Visit Count.
    public static List<String> subdomainVisits_discuss1(String[] cpdomains) {
        Map<String, Integer> count = new HashMap<>();
        for (String cd : cpdomains) {
            int i = cd.indexOf(' ');
            int n = Integer.parseInt(cd.substring(0, i));
            String s = cd.substring(i + 1);
            for (i = 0; i < s.length(); ++i) {
                if (s.charAt(i) == '.') {
                    String d = s.substring(i + 1);
                    count.put(d, count.getOrDefault(d, 0) + n);
                }
            }
            count.put(s, count.getOrDefault(s, 0) + n);
        }

        List<String> res = new ArrayList<>();
        for (String d : count.keySet()) res.add(count.get(d) + " " + d);
        return res;
    }
}
