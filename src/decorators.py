from datetime import datetime
from functools import wraps


def log(filename=None):
    def logging(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                start = datetime.now()
                result = func(*args, **kwargs)
                stop = datetime.now()
                if filename:
                    path = r'C:\Users\artem_zhitkov\PycharmProjects\homework\logs\.' + filename + '.txt'
                    with open(path, 'a', encoding='utf-8') as file:
                        file.write(f'{func.__name__} start - {start}\n{func.__name__} - ok\n'
                                   f'{func.__name__} stop - {stop}.\n')
                else:
                    print(f'{func.__name__} start - {start} \n{func.__name__} - ok \n{func.__name__} stop - {stop}')
            except Exception as error:
                if filename:
                    path = r'C:\Users\artem_zhitkov\PycharmProjects\homework\logs\.' + filename + '.txt'
                    with open(path, 'a', encoding='utf-8') as file:
                        file.write(f'{func.__name__} error: {error} with args: {args} and kwargs: {kwargs}.\n')
                else:
                    print(f'{func.__name__} error: {error} with args: {args} and kwargs: {kwargs}')
                raise

            return result
        return wrapper
    return logging
