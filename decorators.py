from functools import wraps


def reg_decorator(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print(f"\nFunction '{func.__name__}' was executed.\n")

    return wrapper


# декоратор для проверки пред- и постусловий
def check_condition(precond=None, postcond=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if precond is not None:
                if not precondition(*args, **kwargs):
                    pass  # реализовать исключение
            original_func = func(*args, **kwargs)
            if postcond is not None:
                if not postcondition(original_func):
                    pass  # реализовать исключение
            return original_func

        return wrapper

    return decorator


# проверка предусловия
def precondition(check):
    return check_condition(precond=check)


# проверка постусловия
def postcondition(check):
    return check_condition(postcond=check)
