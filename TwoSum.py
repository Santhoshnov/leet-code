#bruteforce approach
class Solution:
   def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return [i,j]
    return []

#time complexity:O(n^2)
#space complexity:O(1)


#optimized approach using hashmap
class Solution:
   def twoSum(self, nums: List[int], target: int) -> List[int]:
    dict = {}
    for i,value in enumerate(nums):
        diff = target - nums[i]

        if diff in dict:
            return [dict[diff],i]

        else:
            dict[value] = i

#time complexity:O(n)
#space complexity:O(n)






