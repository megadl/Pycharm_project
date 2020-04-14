def insert_sort(L):
    """sort Position of comparable elements into nondecreasing order """
    if len(L) > 1:  # 如果元素数小于1，那就无需排序。
        marker = L.first()  # marker变量表示indicate当前排序部分最右边的位置。
        while marker != L.last():  # marker运行到队尾，则排序结束
            pivot = L.after(marker)  # 维护一个紧接着marker的位置
            value = pivot.element()
            if value > marker.element():
                marker = pivot  # 如果marker的值小于之后的值，则不需要重新排序，将marker后移
            else:
                walk = marker  # 转存marker值用于插入排序
                while walk != L.first() and L.befor(walk).element() > value:
                    walk = L.before(walk)
                L.delete(pivot)
                L.add_before(walk, value)


if __name__ == '__main__':
    from .person_list import PersonList
    pl = PersonList()

    insert_sort(pl)


