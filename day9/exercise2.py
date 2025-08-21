def call_counter(func):
    def wrapper(args, **kwargs):
        wrapper.calls += 1
        print(f"Function '{func.name}' has been called {wrapper.calls} times")
        return func(args, **kwargs)
    wrapper.calls = 0  
    return wrapper


@call_counter
def greet(name):
    return f"Hizzz, {name}!"



print(greet("layan"))
print(greet("noor"))
print(greet("oday"))

print("Total calls:", greet.calls)