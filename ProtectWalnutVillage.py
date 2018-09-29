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
from hetaolib import ProtectWalnutVillage01


def avg_info(num1, num2, num3, n):  # 收集平均战斗力信息
    pass
    # ↓ write your code below


def max_info(num1, num2, num3):    # 收集最强战斗力信息
    pass
    # ↓ write your code below


def defense_level(avg, max_num):
    pass
    # ↓ write your code below


if __name__ == '__main__':
    ProtectWalnutVillage01(avg_info, max_info, defense_level)
