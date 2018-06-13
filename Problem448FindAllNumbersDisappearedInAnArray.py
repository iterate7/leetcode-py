class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
        Find all the elements of [1, n] inclusive that do not appear in this array.
        Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
        Example:
        Input:[4,3,2,7,8,2,3,1]
        Output:[5,6]

        """
        ret = []
        for item in nums:
            #print(nums)
            item = abs(item) #get value and prepare to record it using index! 我们的目标就是记录这个item值
            oldvalue = (nums[item-1])
            if(oldvalue<0):
                continue
            nums[item-1] = -oldvalue

        for i in range(len(nums)):
            if(nums[i]>0):
                ret.append(i+1)


        return ret

if __name__ == '__main__':
   so =  Solution()
   nums = [4,3,2,7,8,2,3,1]
   ret = so.findDisappearedNumbers(nums)
   print(ret)