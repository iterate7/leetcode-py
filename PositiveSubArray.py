class solution:
    def findPositiveSubArray(self,nums):
        '''

        :param nums:
        :return:
        '''
        print(nums)
        s = [[0, ] * len(nums)]*len(nums)
        print(s)

        for i in range(len(nums)):
            for j in range(len(nums)):
                if(i==j):
                    s[i][j] = nums[i]
        print(s)
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                s[i][j] = s[i][j-1]+nums[j%len(nums)]

        return s


if(__name__=='__main__'):
    so = solution()
    nums = [1,-1,2,2]
    print(so.findPositiveSubArray(nums))