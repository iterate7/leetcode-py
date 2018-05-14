#import numpy as np
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
        Example:
        Input: [-2,1,-3,4,-1,2,1,-5,4],
        Output: 6
        Explanation: [4,-1,2,1] has the largest sum = 6.
        analysis:
        我们是求解数组中的子数组，其和最大。 最原始的解法：把所有的子数组遍历出来，求和，看看那个是最大值，这个是最慢的，也是不回出错的。
        我们可以作为base来实验。
        设：dp[i]如果设置为以nums[i]为结尾的；So I change the format of the sub problem into something like: maxSubArray(int A[], int i), which means the maxSubArray for A[0:i ] which must has A[i] as the end element.
        那么dp[n]如何求解呢？
        dp[n] = dp[n-1]>0? dp[n-1]+nums[n]: nums[n];
        这就是动态规划的最小的一个例子，找到分解方法；这样通过求解子问题来反推出最终的问题！
        最终的结果则是：max（dp）; 相当于所有的结尾都遍历一遍！
        """
        maxValue = 0
        size = len(nums)
        #dp = np.zeros(size)
        dp = []
        for i in range(size):
            dp.append(0)
        dp[0] = nums[0]
        for i in range(1,size):

            history = dp[i-1]
            if(dp[i-1] <0):
                history = 0
            dp[i] = nums[i] + history
            print(i, nums[i], dp[i])

        return  max(dp)

    def maxSubArray(self, A):
        if not A:
            return 0

        curSum = maxSum = A[0]
        for num in A[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)
        return maxSum

    def maxSubArrayBase(self,nums):
        maxValue = 0
        size = len(nums)
        for i in range(size):
            for j in range(i,size):
                #print(i,j)
                tempValue = sum(nums[i:j])
                if(tempValue>maxValue):
                    maxValue = tempValue
                    print(i,j,"=>",nums[i:j],"=>",maxValue)
        return maxValue

if(__name__=='__main__'):
    sl = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    #maxValue = sl.maxSubArrayBase(nums)
    #print("maxValue:",maxValue)
    print("maxValueDP:", sl.maxSubArray(nums))

