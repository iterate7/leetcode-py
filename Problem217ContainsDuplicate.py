class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        Given an array of integers, find if the array contains any duplicates.
        Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
        Example 1:
        Input: [1,2,3,1]
        Output: true

        """
        setnums = set(nums)
        return len(nums) != len(setnums)
    def containsDuplicateBaseSet(self,nums):
        setnums = set(nums)
        return len(nums) != len(setnums)

    def containsDuplicateBaseSetContains(self,nums):
        newSet = set()
        for item in nums:
            if(newSet.__contains__(item)):
                return True
            newSet.add(item)
        return False



if __name__ == '__main__':
   so =  Solution()
   nums = [4,3,2,7,8,2,3,1]
   print(so.containsDuplicate(nums))
   print(so.containsDuplicateBaseSetContains(nums))