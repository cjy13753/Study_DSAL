import java.util.HashMap;


public class Leetcode1512HashTable {
    public static void main(String[] args) {
        int[] sample1 = {1,2,3,1,1,3};
        int[] sample2 = {1,1,1,1};
        int[] sample3 = {1,2,3};
        int answer1 = numIdenticalPairsMyAnswer(sample1);
        int answer2 = numIdenticalPairsMyAnswer(sample2);
        int answer3 = numIdenticalPairsMyAnswer(sample3);
        System.out.println(answer1);
        System.out.println(answer2);
        System.out.println(answer3);
    }

    public static int numIdenticalPairsMyAnswer(int[] nums) {
        int goodCounter = 0;
        int whilePosition = 0;
        while (whilePosition < nums.length - 1) {
            for (int i = whilePosition + 1; i < nums.length; i++) {
                if (nums[whilePosition] == nums[i]) {
                    goodCounter++;
                }
            }
            whilePosition++;
        }

        return goodCounter;
    }

    public int numIdenticalPairsDiscuss(int[] nums) {
        HashMap<Integer,Integer> map = new HashMap<Integer,Integer>();
        int answer = 0;
        for(int i: nums){
            if(map.containsKey(i)){ // if number has occurred before
                int temp = map.get(i);
                answer += temp; // add number of occurrences to the answer
                map.put(i,temp+1); // increment number of occurrences
            } else {
                map.put(i,1); // if it is the first time, add it to the map
            }
        }
        return answer;
    }
}