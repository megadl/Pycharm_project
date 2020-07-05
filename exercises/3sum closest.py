class Solution:
    def threeSumClosest(self, nums, target):
        """与threeSum做法其实是相同的，排序+双指针==>在一重循环中嵌套双指针，完美解决原本需要三重循环的问题"""
        nums.sort()
        n = len(nums)
        best = float('inf')

        def update(s):
            nonlocal best
            if abs(s-target) < abs(best-target):
                best = s

        for i in range(n):
            # 过滤重复的值
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 确定双指针数值
            j, k = i + 1, n - 1
            while j < k:
                s = nums[i] + nums[k] + nums[j]
                update(s)
                if s < target:
                    k1 = k - 1
                    while j < k1 and nums[k1] == nums[k]:
                        k1 -= 1
                    k = k1
                else:
                    j1 = j + 1
                    while j1 < k and nums[j1] == nums[j]:
                        j1 -= 1
                    j = j1
        return best


if __name__ == '__main__':
    solution = Solution()
    nums = [-1, 2, 1, -4]
    target = 1
    print(solution.threeSumClosest(nums, target))
