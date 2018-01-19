def main():
    value = 20
    count = generating_func(value)
    print(count)


"""
    1. 计算给定最大价值邮票数额, 计算出小于给定价值的邮票的组成方案数的集合.
    2. 我们不保存幂函数的次幂, 只保存幂函数的系数. 因为次幂可以通过下标的枚举来控制.
"""


def generating_func(value):
    value += 1  # 我们在数组中需要使用到价值为 value的组成方案数, 故需要防止溢出
    count = [1] * value  # 由表达式可知, 第一个表达式的每一个幂函数的系数都为 1
    temp = [0] * value  # 存储中间结果
    for expression_index in range(2, value):  # 只需要计算第二个表达式以及之后的表达式
        for item_index in range(0, value):  # 枚举当前表达式所有幂函数的系数
            for mul_item_index in range(0, value, expression_index): # 枚举相乘的表达式的幂函数的所有系数
                if item_index + mul_item_index < value:
                    temp[mul_item_index + item_index] += count[item_index]  # 更新对应次幂的系数值
        count = temp.copy()  # 保存计算完前 expression_index 个表达式的计算结果.
        temp = [0] * value
    return count


if __name__ == "__main__":
    main()
