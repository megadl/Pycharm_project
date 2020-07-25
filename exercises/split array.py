class Solution:
    def splitArray(self, nums, m):
        n = len(nums)
        f = [[10 ** 18] * (m + 1) for _ in range(n + 1)]
        sub = [0]
        for elem in nums:
            sub.append(sub[-1] + elem)

        f[0][0] = 0
        for i in range(1, n + 1):
            for j in range(1, min(i, m) + 1):
                for k in range(i):
                    f[i][j] = min(f[i][j], max(f[k][j - 1], sub[i] - sub[k]))

        return f[n][m]

    def bisplitArray(self, nums, m):
        """使用二分法，将数组所有元素和作为二分法上限，元素最大值作为下限，寻找合适mid即为要求的最大和的最小值"""

        def bichecker(x):
            total, count = 0, 1
            for num in nums:
                if total + num > x:
                    count += 1
                    total = num  # 创建新的subarray， 并初始化新的head
                else:
                    total += num
            return count <= m

        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            if bichecker(mid):
                right = mid
            else:
                left = mid + 1  # 必须加1，为left大于等于right创造条件（退出while循环)
        return left


if __name__ == '__main__':
    solution = Solution()
    nums = [7, 2, 8]
    m = 2
    print(solution.bisplitArray(nums, m))
