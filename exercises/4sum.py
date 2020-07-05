class Solution:
    def fourSum(self, nums, target):
        n = len(nums)
        nums.sort()
        ans = list()
        
        # 枚举 a
        for first in range(n):
            # 需要和上一次枚举的数不相同
            # first = 0 or nums[first] != nums[first-1]的'非'就是first > 0 and nums[first] == nums[first-1]
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            # c 对应的指针初始指向数组的最右端
            if n >= 4 and (nums[first] + nums[first + 1] + nums[first + 2] + nums[first + 3] > target or nums[n - 1] + nums[n -
                                                                                                                2] + \
                    nums[n - 3] + nums[n - 4] < target):
                break
            target1 = target - nums[first]
            # 枚举 b
            for second in range(first + 1, n):
                # 需要和上一次枚举的数不相同
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                forth = n - 1
                for third in range(second + 1, n):
                    if third > second + 1 and nums[third] == nums[third - 1]:
                        continue
                    
                    while third < forth and nums[second] + nums[third] + nums[forth] > target1:
                        forth -= 1
                    
                    if third == forth:
                        break
                    if nums[second] + nums[third] + nums[forth] == target1:
                        ans.append([nums[first], nums[second], nums[third], nums[forth]])
        
        return ans


if __name__ == '__main__':
    solution = Solution()
    nums = [-3, -2, -1, 0, 0, 1, 2, 3]
    nums1 = [0]
    target = 0
    print(solution.fourSum(nums1, target))
