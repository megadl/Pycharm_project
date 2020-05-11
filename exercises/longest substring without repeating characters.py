def lengthOfLongestSubstring(s: str) -> int:
    temp = s[0]
    max_len = 1
    for letter in s[1:]:
        if letter in temp:
            cur = s.find(letter)  # mark where repeating alpha appears
            temp = temp[cur+1:]  # remove repeating letter in temp.出现重复单词，则cur前的原子字符串就结束了。
        temp += letter  # add new repeating letter whose duplicating is deleted in the previous line. temp grows.
        if len(temp) > max_len:
            max_len = len(temp)
    return max_len


if __name__ == '__main__':
    s = 'abcabcbb'
    print(lengthOfLongestSubstring(s))
