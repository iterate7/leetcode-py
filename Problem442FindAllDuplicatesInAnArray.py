class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
       Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
       Find all the elements that appear twice in this array.Could you do it without extra space and in O(n) runtime?
       Example:
       Input:[4,3,2,7,8,2,3,1]
       Output:[2,3]

        """
        ret = []
        for i in range(len(nums)):
            #print(nums)
            item = nums[i]
            item = abs(item) #get value and prepare to record it using index! 我们的目标就是记录这个item值
            oldvalue = (nums[item-1])
            if(oldvalue<0): #说明已经此索引位置已经被用过了，现在是第二次使用！
                ret.append(item)
            nums[item-1] = -oldvalue




        return ret

if __name__ == '__main__':
   so =  Solution()
   nums = [4,3,2,7,8,2,3,1]
   ret = so.findDuplicates(nums)
   print(ret)