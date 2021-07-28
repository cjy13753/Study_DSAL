/* Maximus Product of Two Elements in an Array */

public class Leetcode1464EasyHeap {

    public static void main(String[] args) {
        int[] testCase = {3, 4, 5, 2};
        Solution s = new Solution();
        System.out.println(s.maxProduct(testCase));
    }
}

class Solution {
    public int maxProduct(int[] nums) {
        buildHeap(nums);

        int biggest = extractMax(nums);
        int secondBiggest = extractMax(nums);

        return (biggest - 1) * (secondBiggest - 1);
    }

    private void buildHeap(int[] nums) {
        for (int i = nums.length / 2 - 1; i >= 0; i--) {
            heapify(i, nums);
        }
    }

    private int extractMax(int[] nums) {
        int popped = nums[0];
        nums[0] = nums[nums.length - 1];
        heapify(0, nums);
        return popped;
    }

    private void heapify(int pos, int[] nums) {
        if (pos * 2 + 1 == nums.length - 1) {
            if (nums[pos] < nums[pos * 2 + 1]) {
                swap(pos, pos * 2 + 1, nums);
            }
        } else if (pos * 2 + 1 < nums.length - 1) {
            if (nums[pos] < nums[pos * 2 + 1] || nums[pos] < nums[pos * 2 + 2]) {
                if (nums[pos * 2 + 1] > nums[pos * 2 + 2]) {
                    swap(pos, pos * 2 + 1, nums);
                    heapify(pos * 2 + 1, nums);
                } else {
                    swap(pos, pos * 2 + 2, nums);
                    heapify(pos * 2 + 2, nums);
                }
            }
        }
    }

    private void swap(int pos1, int pos2, int[] nums) {
        int temp = nums[pos1];
        nums[pos1] = nums[pos2];
        nums[pos2] = temp;
    }
}