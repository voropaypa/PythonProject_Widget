from functools import wraps
from time import time


def log(filename=None):
    """Декоратор, который будет автоматически логировать начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки.
    Декоратор должен принимать необязательный аргумент filename, который определяет,
    куда будут записываться логи (в файл или в консоль)"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time()
            name_error = None
            result = None

            try:
                result = func(*args, **kwargs)
            except Exception as e:
                name_error = type(e).__name__

            end_time = time()
            execution_time = f"The function was running for {end_time - start_time}.\n"

            if name_error is not None:
                log_info = f"Function {func.__name__} called with args: {args} and kwargs: {kwargs}. Resulted with an Error: {name_error}.\n"
            else:
                log_info = f"Function {func.__name__} called with args: {args} and kwargs: {kwargs}. Result: {result}.\n"

            if filename is None:
                print(log_info)
                print(execution_time)
            else:
                with open(filename, 'a', encoding='utf-8') as file:
                    file.write(log_info)
                    file.write(execution_time)
            return result
        return wrapper
    return decorator
