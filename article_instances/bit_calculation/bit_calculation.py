def main():
    # res = count_1s_basically(26)
    res = count_1s_enhanced(26)
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


if __name__ == "__main__":
    main()
