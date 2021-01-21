from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if len(nums) < 1 or len(nums) > 1000:
            raise ValueError('1 <= nums.length <= 1000')
        else:
            temp_list = []
            temp_num = 0
            for i in range(len(nums)):
                if not isinstance(nums[i], int):
                    raise ValueError
                
                if nums[i] < (-10**6) or nums[i] > (10**6):
                    raise ValueError('-10^6 <= nums[i] <= 10^6')
                
                temp_num += nums[i]
                temp_list.append(temp_num)
            return temp_list


solution = Solution()
print(solution.runningSum([1,2,3,4]))