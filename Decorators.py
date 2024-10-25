#Q1#
import time

def log_execution_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

# Applying the decorator to a sample function
@log_execution_time
def example_function(n):
    time.sleep(n)  # Simulating a delay


result = example_function(2)  # This will sleep for 2 seconds

#Q2
def repeat(num_times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return [func(*args, **kwargs) for _ in range(num_times)]
        return wrapper
    return decorator

# Applying the decorator to a sample function
@repeat(3)  # This will repeat the function 3 times
def greet(name):
    return f"Hello, {name}!"

# Call the decorated function
results = greet("Alice")

# Print the results
print(results)

#Q3
def log_method_calls(cls):
    class Wrapper:
        def __init__(self, *args, **kwargs):
            self._instance = cls(*args, **kwargs)

        def __getattr__(self, attr):
            orig_attr = self._instance.__getattribute__(attr)
            if callable(orig_attr):
                def new_func(*args, **kwargs):
                    print(f"Calling {attr} with {args}, {kwargs}")
                    return orig_attr(*args, **kwargs)
                return new_func
            return orig_attr
    return Wrapper

# Applying the decorator to a sample class
@log_method_calls
class Example:
    def greet(self, name):
        return f"Hello, {name}!"

    def add(self, a, b):
        return a + b

# Create an instance of the decorated class
example = Example()

# Call the methods
greeting = example.greet("Alice")
sum_result = example.add(5, 3)

# Print the results
print(greeting)
print(sum_result)

#Q4
def cache_results(func):
    cache = {}

    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrapper

# Applying the decorator to a sample function
@cache_results
def expensive_computation(x):
    print(f"Computing {x}...")
    return x * x  # Simulating a computation

# Call the decorated function
result1 = expensive_computation(4)  # First call, should compute
result2 = expensive_computation(4)  # Second call, should use cache

# Print the results
print(result1)
print(result2)

#Q5
def requires_permission(permission):
    def decorator(func):
        def wrapper(*args, **kwargs):
            user_permissions = kwargs.get('user_permissions', [])
            if permission in user_permissions:
                return func(*args, **kwargs)
            raise PermissionError(f"Permission '{permission}' denied")
        return wrapper
    return decorator

# Applying the decorator to a sample function
@requires_permission('admin')
def access_admin_panel(user_permissions):
    return "Access granted to admin panel!"

# Test with permissions
try:
    result = access_admin_panel(user_permissions=['admin'])  # Has permission
    print(result)
except PermissionError as e:
    print(e)

try:
    result = access_admin_panel(user_permissions=['user'])  # No permission
    print(result)
except PermissionError as e:
    print(e)

#Q6
import time

def log_execution_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

def repeat(num_times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return [func(*args, **kwargs) for _ in range(num_times)]
        return wrapper
    return decorator

def cache_results(func):
    cache = {}

    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrapper

@log_execution_time
@repeat(3)
@cache_results
def add(a, b):
    return a + b

# Call the decorated function
results = add(3, 4)

# Print the results
print(results)

#Q7
import time

# Decorator to time multiple functions
def time_multiple_functions(funcs):
    def wrapper(*args, **kwargs):
        results = {}
        for func in funcs:
            start = time.time()
            results[func.__name__] = func(*args, **kwargs)
            end = time.time()
            print(f"{func.__name__} took {end - start:.4f} seconds")
        return results
    return wrapper

# Example function to time
def add(a, b):
    return a + b

# Using the time_multiple_functions decorator
@time_multiple_functions([add])
def main():
    return add(1, 2)

# Call the main function to see timing output
main()




