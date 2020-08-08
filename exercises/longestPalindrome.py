class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 直接扫描整个s，每次s增加1个字符，最大回文串P仅存在两种情况：
        # 1.最大回文串长度增加1（最左侧指针不动）且新增字符包含在新最大回文串中；
        # 2.最大回文串长度增加2（最左侧指针向左移动一位，即原字符串中最靠近回文串头的字符与新字符构         # 成新的最大回文串）且新增字符包含在新最大回文串中；
        if len(s) == 0:
            return ''
        maxLen = 1  # 单个字符肯定是palindrome
        start = 0
        for i in range(len(s)):
            # 特别注意
            # 这里判别回文串的过程中切片的头索引一直在根据回文串的长度进行移动。仔细体会！
            # 特别注意
            # i-maxLen意味着就是当前最大长度比当前遍历的字符串长度小1
            if i - maxLen >= 0 and s[i - maxLen:i + 1] == s[i - maxLen:i + 1][::-1]:
                print(f'current substring is: {s[i - maxLen:i + 1]}')
                start = i - maxLen
                maxLen += 1
                print(f'after maxLen+1, the modified substring is: {s[i - maxLen:i + 1]}')
            if i - maxLen >= 1 and s[i - maxLen - 1:i + 1] == s[i - maxLen - 1:i + 1][::-1]:
                print(f'current substring is: {s[i - maxLen:i + 1]}')
                start = i - maxLen - 1
                maxLen += 2
                print(f'after maxLen+2, the modified substring is: {s[i - maxLen:i + 1]}')
                # continue
        return s[start:start + maxLen]


"""
说明：
    case1.新加入的字符s[i]与当前最大回文串构成新的最大回文串，则新最大回文串长度在原基础上+1，新的最大回文串包含s[i]
    case2.新加入的字符串s[i]与当前最大回文串及其首元素的前一个元素这两者构成新的最大回文串，则新最大回文串长度在原基础上+2（配对了嘛），
    则新的最大回文串的起始字符是s[i-maxLen-1],最后一个字符是s[i]，也就是那个新增的字符"""

if __name__ == '__main__':
    test = Solution()
    s = 'cbabaddcc'
    print(test.longestPalindrome(s))
