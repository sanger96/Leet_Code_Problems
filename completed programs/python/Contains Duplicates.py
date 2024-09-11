class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #sort the list and look for duplicates
        nums.sort()
        for x in range(len(nums)) :
            #skip the first element
            if x > 0 :
                if nums[x-1] == nums[x] :
                    return True
        return False
