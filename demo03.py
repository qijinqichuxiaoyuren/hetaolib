import sys
import traceback as tb
import re

err_dic = {'NameError': ['变量名错误',
                         {"name '(\w+)' is not defined": '变量名 \\1 未定义'}],
           'UnboundLocalError': ['访问未初始化局部变量错误',
                                 {"local variable '(\w+)' referenced before assignment": "变量 \\1 初始化前被引用"}],
           'ZeroDivisionError': ['除数为0错误',
                                 {"division by zero": "division by zero"}],
           'TypeError': ['类型错误',
                         {"unsupported operand type\(s\) for (.): '(\w+)' and '(\w+)'": "数学运算符\\1, 不支持类型\\2和类型\\3 相加",
                          'can only concatenate str \(not "(\w+)"\) to str': "字符串不能和\\1类型数据通过 + 连接",
                          "'(.+)' object is not callable": "\\1 类型不可调用",
                          "^(.+\(\)) missing (.+) required positional arguments?: (.+) \w{3} (.+)": "调用函数 \\1 需要\\2个位置参数 \\3 \\4",
                          "^(.+\(\)) missing (.+) required keyword-only argument: '(.+)'": "调用函数 \\1 需要传递\\2个关键字参数 \\3"}],
           'ValueError': ['非法参数错误',
                          {"invalid literal for int\(\) with base 10: ('.+')": "int()函数不能转换字符串 \\1 为整型"}],
           'AttributeError': ['属性错误',
                              {"'(\w+)' object has no attribute '(\w+)'": "对象 \\1 没有 \\2 属性"}]
           }


def demo():
    pass

    m

    # a = a + 1

    # 3 / 0

    # 2 + '2'

    # '2' + 2

    # s = '2.0'    # int('2.0') 等价
    # int(s)

    # func = None
    # func()    # 不可调用类型
    # a = []
    # a(1)    # 同上

    # '字符串'.func()

    # def func(par1):
    #     pass
    # func()    # missing 一个位置参数

    # def func(par1, par2, par3, par4, par5, par6, par7, par8, par9, par10):
    #     pass
    # func()    # missing N个位置参数

    # def func(par1, par2,  *, par3):
    #     pass
    # func(1, 2)


def translate_err(lineNo, function, text, err):
    print("*" * 40)
    print("出错了!")
    print("*" * 40)
    print("错误发生在这一句:")
    print(text)
    print("它在第 %d 行,  %s 中" % (lineNo, function))
    print("错误信息:")
    e = str(err)
    print(e)
    e_type = re.sub("<class '(\w+)'>", '\\1', str(type(err)))
    if e_type in err_dic:
        print('翻译:')
        print(err_dic[e_type][0])
        msg_dic = err_dic[e_type][1]
        for s in msg_dic:
            if re.match(s, e) is not None:
                print(re.sub(s, msg_dic[s], e))
                break
    print("*" * 40)


def main():
    sys.stdout = open('C:/Users/kc/Desktop/d12.txt', 'w+')
    # sys.stderr = open('C:/Users/kc/Desktop/d13.txt', 'w+')
    try:
        demo()
    except Exception as e:
        # info = sys.exc_info()
        # file, lineNo, function, text = tb.extract_tb(info[2])[-1]
        # translate_err(lineNo, function, text, e)

        info = sys.exc_info()
        for i, v in enumerate(info):
            print(i, v, type(v))

        stack_summary_obj = tb.extract_tb(info[-1])
        print('-' * 80)
        for i, v in enumerate(stack_summary_obj):
            print(i, v, type(v))
            print(f'\t\t{locals()}\n\t\t文件名: {v.filename}\n\t\t行号: {v.lineno}\n\t\t函数名: {v.name}\n\t\t出错行: {v.line}')

        print('-' * 80)
        for i, v in enumerate(stack_summary_obj.format()):
            print(i, v, type(v))


if __name__ == '__main__':
    main()
