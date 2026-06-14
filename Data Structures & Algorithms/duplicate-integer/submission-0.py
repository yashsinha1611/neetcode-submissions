class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         countS ={}

         for i in range(len(nums)):
            countS[nums[i]]= 1 + countS.get(nums[i],0)
         for c in countS:
            if countS[c] >1:
                return True

         return False