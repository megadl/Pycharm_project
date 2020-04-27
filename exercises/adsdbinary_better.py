def addBinary(a, b):
    """use Bitwise Operations on Integer Types"""
    x, y = int(a, 2), int(b, 2)  # convert binary string to integer, then use bitwise operation on integer types
    while y:  # x stores answer, y stores carry, x should add_binary y while y
        x, y = x ^ y, (x & y) << 1
    return bin(x)[2:]



if __name__ == '__main__':
    a = '11'
    b = '1'
    print(addBinary(a, b))
