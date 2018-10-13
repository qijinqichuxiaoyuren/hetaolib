import sys
import re


err_dic = {'ZeroDivisionError': '除数不能为0', 'NameError': '变量未定义'}


def func():
    try:
        pass
        # 3/0
        # <class 'ZeroDivisionError'>		<class 'type'>
        # division by zero		<class 'ZeroDivisionError'>
        # <traceback object at 0x000001BE42EACD88>		<class 'traceback'>

        # m
        # <class 'NameError'>		<class 'type'>
        # name 'm' is not defined		<class 'NameError'>
        # <traceback object at 0x00000169B693FF08>		<class 'traceback'>

        # a = a + 1
        # <class 'UnboundLocalError'>		<class 'type'>
        # local variable 'a' referenced before assignment		<class 'UnboundLocalError'>
        # <traceback object at 0x000001DD058ED088>		<class 'traceback'>

        demo()
    except:
        pass
        info = sys.exc_info()
        for i, v in enumerate(info):
            print(f'{i}\t\t{v}\t\t{type(v)}')
        #     match_obj = re.search("<class '(\w+)'>", f'{i}')
        #     if match_obj is not None:
        #         pass
        #         # print(match_obj)
        #         # print(match_obj.group(0), match_obj.group(1), sep='\t\t')
        #
        #         err = match_obj.group(1)
        #         print(err_dic[err])

        # match_obj1 = re.search("<class '(\w+)'>", f'{info[-3]}')
        # match_obj2 = re.search("name '(\w+)' is not defined", f'{info[-2]}')
        #
        # if match_obj2 is not None:
        #     print(f'变量名 {match_obj2.group(1)} 没有定义')
        # else:
        #     if match_obj1 is not None:
        #         print(err_dic[match_obj1.group(1)])
        # # print(match_obj1.group(1), match_obj2.group(1))
        # # # if match_obj is not None:
        # # #     pass
        # # #     # print(match_obj)
        # # #     # print(match_obj.group(0), match_obj.group(1), sep='\t\t')
        # # #
        # # #     err = match_obj.group(1)
        # # #     print(err_dic[err])
        print('..........')


def demo():
    m


if __name__ == '__main__':
    func()




