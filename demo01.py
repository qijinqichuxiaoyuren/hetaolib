"""
根据不同情报信息,报告不同防御等级A, B, C
1.第一题: 情报收集
    1.平均数: 平均战斗力 (不能轻敌因此 *2返回)
    2.最大数: Boss
2.第二题: 根据情报派遣英雄迎战
    1.avg*2 > max: 防御等级A
    2.avg*2 = max: 防御等级B
    3.avg*2 < max: 防御等级C
"""
from demo02 import Demo


def avg_info(num1, num2, num3, n):  # 收集平均战斗力信息
    summation = num1 + num2 + num3
    avg = summation / n
    return avg


def max_info(num1, num2, num3):    # 收集最强战斗力信息
    pass
    if num1 >= num2 >= num3:
        return num1
    elif num1 >= num3 >= num2:
        return num1
    elif num2 >= num1 >= num3:
        return num2
    elif num2 >= num3 >= num1:
        return num2
    elif num3 >= num1 >= num2:
        return num3
    elif num3 >= num2 >= num1:
        return num3
    return num1


def defense_level(avg, max_num):
    """为"""
    pass
    avg = avg * 2
    if avg > max_num:
        return 'A'
    elif avg == max_num:
        return 'B'
    else:
        return 'C'


if __name__ == '__main__':
    Demo(avg_info, max_info, defense_level)
