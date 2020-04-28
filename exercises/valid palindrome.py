def validPalindrome(s: str) -> bool:
    anchor = 0
    for i in range(len(s)//2):
        if s[i] == s[len(s)-1-i]:
            anchor += 1
        elif s[i] != s[len(s)-1-i]:
            if len(s) % 2 == 0 and (s[i+1:len(s)//2+1] == s[len(s)-1-i: len(s)//2-1: -1] or s[i:len(s)//2-1] == s[len(s)-i-2: len(s)//2-1: -1]):
                return True
            if len(s) % 2 == 1 and (s[i+1:len(s)//2+1] == s[len(s)-1-i: len(s)//2: -1] or s[i:len(s)//2] == s[len(s)-i-2: len(s)//2-1: -1]):  # 奇数个字符串存在中间位是否包含的问题
                return True
            else:
                return False

    if anchor == len(s)//2:
        return True





if __name__ == '__main__':
    string = 'abdaadbba'
    lt = string[0 + 1:len(string) // 2]
    rt = string[len(string)-1-0: len(string)//2: -1]
    lt1 = string[0:len(string) // 2]
    rt2 = string[len(string) - 1 - 2: len(string) // 2 : -1]
    print(validPalindrome(string))
