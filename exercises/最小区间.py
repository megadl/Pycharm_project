import heapq


class Solution:
    def smallestRange(self, nums):
        rangeLeft, rangeRight = -10 ** 9, 10 ** 9
        maxValue = max(vec[0] for vec in nums)  # 各数组的最小值中的最大值
        priorityQueue = [(vec[0], i, 0) for i, vec in enumerate(nums)]
        heapq.heapify(priorityQueue)  # 将priorityQueue转换成一个heap
        
        while True:
            minValue, row, idx = heapq.heappop(priorityQueue)  # pop从出最小值，堆的第一个元素肯定是最小值
            if maxValue - minValue < rangeRight - rangeLeft:  # 用更小的最小值差更新范围的左右边界
                rangeLeft, rangeRight = minValue, maxValue
            if idx == len(nums[row]) - 1:  #  遍历完数据元素后就中断
                break
            maxValue = max(maxValue, nums[row][idx + 1])
            # heapq.heappush(heap, item)  # push an item on the heap
            heapq.heappush(priorityQueue, (nums[row][idx + 1], row, idx + 1))
        
        return [rangeLeft, rangeRight]


if __name__ == '__main__':
    solution = Solution()
    nums = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]
    print(solution.smallestRange(nums))
