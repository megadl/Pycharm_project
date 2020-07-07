class Solution:
    def findLength(self, A, B) -> int:
        max_ = 0
        for i, vA in enumerate(A):
            for j, vB in enumerate(B):
                if vA == vB:
                    res = offset = 0
                    while i + offset < len(A) and j + offset < len(B) and A[i + offset] == B[j + offset]:
                        res += 1
                        offset += 1
                    max_ = max(max_, res)

        return max_


class DPSolution:
    def findLength(self, A, B):
        n, m = len(A), len(B)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        ans = 0
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                dp[i][j] = dp[i + 1][j + 1] + 1 if A[i] == B[j] else 0
                ans = max(ans, dp[i][j])
        return ans


if __name__ == '__main__':
    solution = Solution()
    dpsolution = DPSolution()
    A = [1, 0, 0, 0, 1]
    B = [1, 0, 0, 1, 1]
    target = 0
    # print(solution.findLength(A, B))
    print(dpsolution.findLength(A, B))
