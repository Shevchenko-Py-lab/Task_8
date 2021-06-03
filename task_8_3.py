# Сможете ли вы замаскировать работу декоратора? Сможете ли вывести имя функции, например, в виде:
# >>> a = calc_cube(5)
# calc_cube(5: <class 'int'>)

import sys
from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(arg_1, arg_2):
        log = f'{calc_cube.__name__}({func(arg_1, arg_2)}, {dict([(arg_1, type(arg_1)), (arg_2, type(arg_2))])})'
        return log

    # честно списал уже после того как сделал своё решение, чтобы посмотреть как правильно.
    # def wrapper(*args):
    #     for arg in args:
    #         log = dict([(arg, type(arg))])
    #         print(log)
    #     result = func(*args)
    #     return result

    return wrapper


@type_logger
def calc_cube(x, y):
    return x ** y


print(calc_cube(3, 2))

if __name__ == '__main__':
    _script_name, number_1, number_2 = sys.argv
    print(calc_cube(int(number_1), int(number_2)))

