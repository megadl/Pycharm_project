def addBinary(a, b):
    n = max(len(a), len(b))  # find the max length of a and b
    a, b = a.zfill(n), b.zfill(n)  # return a copy of string left filled with Ascii '0' to make a string of lenth width
    carry = 0  # record the result of int(a[i]) + int(b[i])
    answer = []  # empty list stores the final result list
    for i in range(n - 1, -1, -1):  # iterate over the list with reversed order
        # 处理当前位的值
        carry += int(a[i]) + int(b[i])

        if carry % 2 == 1:
            answer.append('1')
        else:
            answer.append('0')
        # 当前值使用floored quotient判断进位后再参与下一位的计算
        carry //= 2
    # a和b相加后首位需要进位，则answer的位数需要增加一位。
    if carry == 1:
        answer.append('1')
    answer.reverse()
    return ''.join(answer)


if __name__ == '__main__':
    a = '11'
    b = '1'
    print(addBinary(a,b))
