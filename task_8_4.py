# Примечание: сможете ли вы замаскировать работу декоратора?

from functools import wraps


def val_checker(is_valid):
    def wrapper(func):
        @wraps(func)
        def validation(*args):
            if is_valid(*args):
                result = func(*args)
                return result
            else:
                raise ValueError(f'{args} < 0')

        return validation

    return wrapper


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


print(calc_cube.__name__)
print(calc_cube(3))
print(calc_cube(-5))
