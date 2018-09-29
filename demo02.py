import random
import numpy as np
import time


class Demo(object):
    cases = [(2.0, 8.0, 2.0), (1.0, 1.0, 2.0), (1.0, 1.0, 5.0)]
    avg_max = []

    def __init__(self, avg_info_func, max_info_func, hero_func):
        self.intro()
        self.case = self.cases[random.randint(0, 2)]

        self.avg_func = avg_info_func
        self.max_num_func = max_info_func
        self.hero_func = hero_func

        self.exc_user_func()

    def intro(self):
        intro_info = [
            '据可靠情报, 魔王即将率领十万大军向核桃村发起毁灭性进攻;',
            '小核桃, 为了核桃村的安危, 此刻你将临危受命, 加油吧! 勇敢去战斗!',
            '你需要侦查( >计算< )并报告( >return< )敌军信息如下:',
            '\t1.敌军三大首领平均战斗力和最强最战斗力(他们的战斗力分别是num1, num2, num3)',
            f'\t2.根据上述情报信息评估我方防御等级( >return< )\n{"="*60}'
        ]
        for i in intro_info:
            print(i)
            time.sleep(1)

    def exc_user_func(self):
        self.delay('敌军平均战斗力情报收集')
        if self.avg_info():
            lv1_success = [
                '敌军平均战斗力情报信息正确, 真棒! 不愧是核桃村的小英雄',
                f'一鼓作气, 请开始最强战斗力情报信息收集任务, 加油啊, 小核桃, 全村的希望!\n{"="*60}'
            ]
            for i in lv1_success:
                print(i)
                time.sleep(1)
            self.delay('敌军最强战斗力情报收集')
            if self.max_num():
                lv2_success = [
                    '敌军最强战斗力情报信息正确, 太棒了! 你是核桃村的希望',
                    f'继续努力! 请开始防御等级评估任务, 相信自己, 即可出发吧!\n{"="*60}'
                ]
                for i in lv2_success:
                    print(i)
                    time.sleep(1)
                self.delay('防御等级评估')
                self.hero()
            else:
                print('最强战斗力情报信息有误, 刻不容缓, 核桃村的命运将有你改写!')
        else:
            print('平均战斗力情报有误, 万分危急, 请立刻重新出发!')

    def avg_info(self):
        ret_avg = self.avg_func(*self.case, len(self.case))
        avg = np.average(self.case)
        Demo.avg_max.append(avg)
        return ret_avg == avg

    def max_num(self):
        ret_max = self.max_num_func(*self.case)
        max_num = max(self.case)
        Demo.avg_max.append(max_num)
        return ret_max == max_num

    def hero(self):
        defense_lv = self.hero_func(Demo.avg_max[0], Demo.avg_max[1])
        if defense_lv == 'A':
            print(f'正在启动{defense_lv:-^5}级防御体系, ', end='')
            time.sleep(2)
            print('启动成功; 任务完成, 核桃村再次战胜了魔王... 太棒了!')
        elif defense_lv == 'B':
            print(f'正在启动{defense_lv:-^5}级防御体系, ', end='')
            time.sleep(2)
            print('启动成功; 任务完成, 核桃村再次战胜了魔王... 太棒了!')
        elif defense_lv == 'C':
            print(f'正在启动{defense_lv:-^5}级防御体系, ', end='')
            time.sleep(2)
            print('启动成功; 任务完成, 核桃村再次战胜了魔王... 太棒了!')
        else:
            print(f'防御等级{defense_lv:-^5}无效! 请重新评估... 时间不多了, 加油啊!')

    def delay(self, task):
        tmp = f"正在执行{task}任务..."
        print(f'{tmp:*^60}')
        time.sleep(3)
