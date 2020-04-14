def insertion_sort(data):
    """Sort list of comparable elements into nondecreasing order"""
    for i in range(len(data)):  # i可以取值0也可以不取值0，若i取值0则在while函数条件里会被过滤
        cur = data[i]
        k = i
        while k > 0 and cur < data[k - 1]:
            data[k] = data[k - 1]
            k -= 1
        data[k] = cur  # while 条件不成立的时候应该是当前位置赋值为cur，而不是当前位置的前一个位置赋值为cur！！！
    print(data)


if __name__ == '__main__':
    data = ['a', 'f', 'd', 'e', 'c', 'b', 'g', 'a', 'b', '1']
    insertion_sort(data)
