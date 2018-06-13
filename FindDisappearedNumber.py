class solution():
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """
        4 => [4, 3, 2, -7, 8, 2, 3, 1]
        3 => [4, 3, -2, -7, 8, 2, 3, 1]
        -2 => [4, -3, -2, -7, 8, 2, 3, 1]
        -7 => [4, -3, -2, -7, 8, 2, -3, 1]
        8 => [4, -3, -2, -7, 8, 2, -3, -1]
        2 => [4, -3, -2, -7, 8, 2, -3, -1]
        -3 => [4, -3, -2, -7, 8, 2, -3, -1]
        -1 => [-4, -3, -2, -7, 8, 2, -3, -1]
        [5, 6]
                                             ^
        """

        for x in nums:
            if nums[abs(x) - 1] > 0:
                nums[abs(x) - 1] *= -1
            print(x,"=>",nums)

        ans = []

        for i in range(len(nums)):
            if nums[i] > 0:
                ans.append(i + 1)
        return ans

if __name__ == "__main__":
    nums = [4,3,2,7,8,2,3,1]
    print(solution().findDisappearedNumbers(nums))
