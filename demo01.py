import sys
import re


def func():
    try:
        demo()
    except UnboundLocalError:
        exc_info = get_exc_info()
        match_obj = re.search("local variable '(\w+)' referenced before assignment", f'{exc_info[1]}')
        print(f'变量 {match_obj.group(1)} 引用之前未赋值')
    except NameError:
        exc_info = get_exc_info()
        match_obj = re.search("name '(\w+)' is not defined", f'{exc_info[1]}')
        if match_obj is not None:
            print(f'变量名 {match_obj.group(1)} 没有定义')
    # 备注: 类定义滞后, 也是NameError, 且使用本正则
    except ZeroDivisionError:
        print('除数不能为0')
    except TypeError:
        exc_info = get_exc_info()
        match_obj = re.search("unsupported operand type\(s\) for (\+): '(float|int)' and '(str)'", f'{exc_info[1]}')
        if match_obj is not None:
            print(f'{match_obj.group(1)} 运算符不支持 类型 {match_obj.group(2)} 和 {match_obj.group(3)}')

        match_obj = re.search('can only concatenate (str) \(not "(int|float)"\) to str', f'{exc_info[1]}')
        if match_obj is not None:
            print(f'字符串 {match_obj.group(1)} 不能和 {match_obj.group(2)} 类型级联')
    except Exception as e:
        print(e)


def get_exc_info():
    return sys.exc_info()


def demo():
    # m
    # 3 / 0
    # a = a + 1
    # 2 + '2'
    # 2.0 + '2'
    # '2' + 2
    # '2' + 2.0
    pass


def test():
    try:
        demo()
    except:
        exc_info = sys.exc_info()
        for i, v in enumerate(exc_info):
            print(f'{i:<5}{str(v):<55}{str(type(v)):<25}')


if __name__ == '__main__':
    test()
    # func()





