import time
import threading
import sys
import traceback
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np


class TimeOutError(Exception):
    def __init__(self, *args):
        self.args = args
        
    
class Dispacher(threading.Thread):
    def __init__(self, fun, args):
        threading.Thread.__init__(self)
        self.setDaemon(True)
        self.result = None
        self.error = None
        self.fun = fun
        self.args = args
        self.start()
        
    def run(self):
        try:
            a = self.args
            if type(a) == tuple:
                l = len(a)
                if l == 0:
                    self.result = self.fun()
                elif l == 1:
                    self.result = self.fun(a[0])
                elif l == 2:
                    self.result = self.fun(a[0], a[1])
                elif l == 3:
                    self.result = self.fun(a[0], a[1], a[2])
                elif l == 4:
                    self.result = self.fun(a[0], a[1], a[2], a[3])
                elif l == 5:
                    self.result = self.fun(a[0], a[1], a[2], a[3], a[4])
            else:
                 self.result = self.fun(self.args)
            
        except Exception as e:
            info = sys.exc_info()
            file, lineNo, function, text = traceback.extract_tb(info[2])[-1]
            #err_log = traceback.format_exc()
            self.error = e
            self.translate_err(lineNo, function, text, e)
            
    def translate_err(self, lineNo, function, text, e):
        print("*" * 40)
        print("出错了!")
        print("*" * 40)
        print("错误发生在这一句:")
        print(text)
        print("它在第 %d 行, 函数 %s 中" % (lineNo, function))
        print("错误信息是:")
        print(e)
        print("*" * 40)

def tryUserFunction(uf, timeout, args):
    c = Dispacher(uf, args)
    c.join(timeout)
    if c.isAlive():
        return TimeOutError('TimeOut')
    elif c.error:
        return c.error
    return c.result


def drawfigure(rate, grade, title):
    grade = np.abs(grade)
    if rate < 0.1:
        rate = 0.1
    if rate > 10:
        rate = 10
    if grade < 0.1:
        grade = 0.1
    if grade > 1:
        grade = 1 
    grade *= np.sqrt(rate)
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    X = np.arange(-5, 5.1, grade)
    Y = np.arange(-5 * rate, 5.1 * rate, grade)
    X, Y = np.meshgrid(X, Y)
    Z = X**2 + Y**2
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
    ax.set_title(title)
    plt.show()


#0你是第一次来核桃村吗？欢迎
#学会使用print()函数
class Welcome_to_hetao_village(object):
    speech = ['欢迎来到核桃村',
              '我是村子里的长老',
              '既然你已经看到这段话',
              '就说明你已经会使用print()了',
              '你做得很好',
              'print()函数可以帮你把我们的话打印在屏幕上，是重要的道具',
              'python是我们生存的工具',
              '一定要学好python',
              '才能一起保护好核桃村',
              '加油，孩子']
    timeOut = 2
    
    def __init__(self, uf):
        speech = self.speech
        timeOut = self.timeOut
        for i in range(len(speech)):
            time.sleep(1)
            ans = tryUserFunction(uf, timeOut, speech[i])
            if isinstance(ans, Exception):
                if isinstance(ans, TimeOutError):
                    print("有什么卡住了？")
                else:
                    print("试试找到错误原因吧")
                return
        time.sleep(2)


#1李奶奶的眼睛花了，不能分辨数据的类型，李奶奶家里很乱，需要整理一下，快帮李奶奶看看数据是什么类型吧
#理解变量的类型要素，并学会使用type()函数
class Help_grandma_Lee(object):
    cases = [2, 1.6666666, -1 , True ,"'apple'" ,"'left'" ,"'2.0'", 2.0, 2.010101010101]
    anss = [int, float, int, bool, str, str, str, float, float ]
    timeOut = 2
    
    def __init__(self, uf):
        cases = self.cases
        anss = self.anss
        timeOut = self.timeOut
        for i in range(len(cases)):
            print('李奶奶想知道[%s]的类型，她把数据（data）传给了你' % cases[i])
            time.sleep(0.5)
            ans = tryUserFunction(uf, timeOut, cases[i])
            if isinstance(ans, Exception):
                if isinstance(ans, TimeOutError):
                    print("哪里卡住了？")
                else:
                    print("试试找到错误原因吧")
                return
            if not ans:
                print('李奶奶在等待你把数据的类型返回(retuen)给她, 但是没有等到。快问问老师return的用法吧')
                return
            print('你觉得这是一个[%s]，把[%s]返回给了李奶奶' % (ans, ans))
            time.sleep(0.5)
            print('==================================')
            time.sleep(0.5)
            if ans != anss[i]:
                  print('好像这并不是数据的类型，李奶奶不太开心，快问问老师如何用type()取得数据的类型吧')
                  return 
        print('你帮助李奶奶整理好了数据，李奶奶奖励了你一块布丁')
        time.sleep(3)


#2魔王来偷袭核桃村啦！快帮助勇者躲开魔王的攻击
#学会使用if语句, 可以在老师的引导下尝试else语句
class Demon_attack(object):
    cases = ['left' , 'right' ,'right' ,'left' ,'left' ,'up' ]
    anss = ['right' ,'left' ,'left' ,'right','right','down' ]
    timeOut = 2
    
    def __init__(self, uf):
        cases = self.cases
        anss = self.anss
        timeOut = self.timeOut
        for i in range(len(cases)):
            print('魔王发动了攻击，打向了[%s]' % cases[i])
            time.sleep(0.5)
            ans = tryUserFunction(uf, timeOut, cases[i])
            if isinstance(ans, Exception):
                if isinstance(ans, TimeOutError):
                    print("勇者没来得及做出反应，被击倒了")
                else:
                    print("试试找到错误原因吧")
                return
            if not ans:
                print('勇者没有想到魔王会从[%s] 发起攻击, 被击倒了。 勇者事后回想起来，觉得可能躲向[%s]比较好' % (cases[i], anss[i]))
                return
            print('勇者做出了回应，躲向了[%s]' % ans)
            time.sleep(0.5)
            print('==================================')
            time.sleep(0.5)
            if ans != anss[i]:
                  print('很遗憾，勇者被击倒了。勇者事后回想起来，觉得可能躲向[%s]比较好' % anss[i])
                  return 
        print('勇者躲过了所有攻击，魔王生气地逃走了')
        time.sleep(1)
        

#3小数实在是太长了！李奶奶想要把所有的小数数据转化为整数数据， 但不是小数就不要做改动哦
#理解变量的类型要素，并学会使用类型转换函数，加深对if..else的理解
class Help_grandma_Lee_2(object):
    cases = [2, 1.6666666, -1 , True ,"'apple'" ,"'left'" ,"'2.0'", 2.0, 2.010101010101]
    anss = [2, 1, -1 , True ,"'apple'" ,"'left'" ,"'2.0'", 2, 2]
    timeOut = 2
    
    def __init__(self, uf):
        cases = self.cases
        anss = self.anss
        timeOut = self.timeOut
        for i in range(len(cases)):
            print('李奶奶拿起了[%s]' % cases[i])
            time.sleep(0.5)
            ans = tryUserFunction(uf, timeOut, cases[i])
            if isinstance(ans, Exception):
                if isinstance(ans, TimeOutError):
                    print("哪里卡住了？")
                else:
                    print("试试找到错误原因吧")
                return
            if not ans:
                print('你没有想好[%s]应该转化成什么, 李奶奶不太开心。事后回想起来，觉得应该是[%s]' % (cases[i], anss[i]))
                return
            print('你把他转化成了[%s]' % ans)
            time.sleep(0.5)
            print('==================================')
            time.sleep(0.5)
            if ans != anss[i]:
                  print('很遗憾，数据转化得不对，李奶奶不太开心。事后回想起来，觉得应该是[%s]才对' % anss[i])
                  return 
        print('你帮助李奶奶转化好了数据，李奶奶奖励了你一瓶汽水')
        time.sleep(1)
