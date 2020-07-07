class Solution:
    def kthSmallest(self, matrix, k):
        rec = sorted(sum(matrix, []))
        return rec[k-1]


if __name__ == '__main__':
    solution = Solution()
    matrix = [[1,5,9],[10,11,13],[12,13,15]]
    k = 8
    print(solution.kthSmallest(matrix, k))
