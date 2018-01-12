def main():
    # res = count_1s_basically(26)
    # res = count_1s_enhanced(26)
    # res = count_1s_simultaneously(26)
    res = count_1s_simultaneously_enhanced(26)
    print(res)


def count_1s_basically(x):
    count = 0
    while x > 0:
        if x & 1:
            count += 1
        x >>= 1
    return count


def count_1s_enhanced(x):
    count = 0
    while x > 0:
        count += 1
        x = x & (x - 1)
    return count


def count_1s_simultaneously(x):
    count = 0
    operators = [0xff000000, 0x00ff0000, 0x0000ff00, 0x000000ff]
    blocks = [x & operator for operator in operators]  # 列表推导
    for block in blocks:
        count += count_1s_enhanced(block)
    return count


def count_1s_simultaneously_enhanced(x):
    val = 0
    for index in range(8):
        val += x & 0x0101010101010101
        x >>= 1
    val += val >> 32
    val += val >> 16
    val += val >> 8
    return val & 0xff


if __name__ == "__main__":
    main()
