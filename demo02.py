import re
import sys

err_dic = {'NameError': ['变量名错误',
                         {"name '(\w+)' is not defined": '变量名 \\1 未定义'}],
           'UnboundLocalError': ['访问未初始化局部变量错误',
                                 {"local variable '(\w+)' referenced before assignment": "变量 \\1 初始化前被引用"}],
           'ZeroDivisionError': ['除数为0错误',
                                 {"division by zero": "division by zero"}],
           'TypeError': ['类型错误',
                         {"unsupported operand type\(s\) for (.): '(\w+)' and '(\w+)'": "数学运算符\\1, 不支持类型\\2和类型\\3 相加",
                          'can only concatenate str \(not "(\w+)"\) to str': "字符串不能和\\1类型数据通过 + 连接",
                          "'NoneType' object is not callable": "空类型不可调用",
                          "^(.+\(\)) missing 1 required positional argument: '(.+)'": "调用函数 \\1 时, 没有传递位置参数 \\2"}],
           'ValueError': ['非法参数错误',
                          {"invalid literal for int\(\) with base 10: ('.+')": "int()函数不能转换字符串 \\1 为整型"}],
           'AttributeError': ['属性错误',
                              {"'(\w+)' object has no attribute '(\w+)'": "对象 \\1 没有 \\2 属性"}]
           }


def main(s):
    res = re.sub(r"invalid literal for int\(\) with base 10: ('.+')", "int()函数不能转换字符串 \\1 为整型", s)
    print(res)


def demo():
    pass

    # m

    # a = a + 1

    # 3 / 0

    # 2 + '2'

    # '2' + 2

    # s = '2.0'    # int('2.0') 等价
    # int(s)

    # func = None
    # func()

    # '字符串'.func()

    # def func(par1):
    #     pass
    # func()

    def func(par1, par2, *, par3):
        pass

    func(1, 2)


def test():
    try:
        demo()
    except:
        for i in sys.exc_info():
            print(i)


if __name__ == '__main__':
    pass
    test()

    # s = "invalid literal for int() with base 10: '3.0'"
    # main(s)
