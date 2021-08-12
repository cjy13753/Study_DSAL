import java.util.HashMap;
import java.util.Map;

public class Leetcode1748HashTable {
    public static void main(String[] args) {
        int[] nums1 = {1,2,3,2};
        int[] nums2 = {1,1,1,1,1};
        int[] nums3 = {1,2,3,4,5};

        System.out.println(sumOfUnique(nums1));
        System.out.println(sumOfUnique(nums2));
        System.out.println(sumOfUnique(nums3));
    }

    // Runtime: 1 ms, faster than 66.95% of Java online submissions for Sum of Unique Elements.
    // Memory Usage: 36.9 MB, less than 12.16% of Java online submissions for Sum of Unique Elements.
    public static int sumOfUnique(int[] nums) {
        int res = 0;
        Map<Integer, Integer> numsMap = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            numsMap.putIfAbsent(nums[i], 0);
            numsMap.put(nums[i], numsMap.get(nums[i]) + 1);
        }

        for (int i = 0; i < nums.length; i++) {
            if (numsMap.get(nums[i]) == 1) {
                res += nums[i];
            }
        }

        return res;
    }

    // Runtime: 1 ms, faster than 66.95% of Java online submissions for Sum of Unique Elements.
    // Memory Usage: 36.5 MB, less than 60.52% of Java online submissions for Sum of Unique Elements.
    public static int sumOfUnique_discuss(int[] nums) {
        int res = 0;
        Map<Integer,Integer> map = new HashMap<>();
        for(int i = 0;i<nums.length;i++){
            map.put(nums[i],map.getOrDefault(nums[i],0)+1);
            if(map.get(nums[i]) == 1)res+=nums[i];
            else if(map.get(nums[i]) == 2)res-=nums[i];
        }
        return res;
    }
}
