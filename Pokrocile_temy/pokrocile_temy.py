# Pokročilé témy
# Generátory
def simple_generator():
    yield 1
    yield 2
    yield 3

for value in simple_generator():
    print(value)

# Dekorátory
def my_decorator(func):
    def wrapper():
        print("Nastala dekorovaná funkcia.")
        func()
        print("Dekorovaná funkcia skončila.")
    return wrapper

@my_decorator
def pozdrav():
    print("Ahoj!")

pozdrav()

