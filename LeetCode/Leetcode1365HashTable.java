import java.util.Arrays;
import java.util.Map;
import java.util.HashMap;

public class Leetcode1365HashTable {
    public static void main(String[] args) {
        int[] nums = {8,1,2,2,3};
        int[] copyNums = Arrays.copyOf(nums, nums.length);
        Arrays.sort(copyNums);
        
        int[] res = smallerNumbersThanCurrent(nums);
        System.out.println(Arrays.asList(Arrays.stream(res).boxed().toArray(Integer[]::new)));

    }

    public static int[] smallerNumbersThanCurrent(int[] nums) {
        
        int[] copyNums = Arrays.copyOf(nums, nums.length);
        int[] res = new int[nums.length];
        
        Arrays.sort(copyNums);
        Map<Integer, Integer> numsMap = new HashMap<>();
        numsMap.put(copyNums[0], 0);

        for (int i = 1; i < copyNums.length; i++) {
            if (copyNums[i] > copyNums[i-1]) {
                    numsMap.put(copyNums[i], i);
            }
        }

        for (int i = 0; i < nums.length; i++) {
            res[i] = numsMap.get(nums[i]);
        }

        return res;
    }

    /* This approach is O(nlogn) time, O(n) space, good thing is that it works for all integer values 
    whereas the most upvoted approach only works for the range of values stated in this problem's description (0 <= nums[i] <= 100). */
    public static int[] smallerNumbersThanCurrent_discuss1(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();
        int[] copy = nums.clone();
        
        Arrays.sort(copy);
        
        for (int i = 0; i < nums.length; i++) {
            map.putIfAbsent(copy[i], i);
        }
        
        for (int i = 0; i < nums.length; i++) {
            copy[i] = map.get(nums[i]);
        }
        
        return copy;
    }
    
    // only works for the range of values stated in this problem's description (0 <= nums[i] <= 100)
    public static int[] smallerNumbersThanCurrent_discuss2(int[] nums) {
        int[] count = new int[101];
        int[] res = new int[nums.length];
        
        for (int i =0; i < nums.length; i++) {
            count[nums[i]]++;
        }
        
        for (int i = 1 ; i <= 100; i++) {
            count[i] += count[i-1];    
        }
        
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 0)
                res[i] = 0;
            else 
                res[i] = count[nums[i] - 1];
        }
        
        return res; 
    }
}
