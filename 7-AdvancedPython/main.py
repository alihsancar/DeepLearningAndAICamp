print("=" * 60)
print("SECTION 1: DECORATORS")
print("=" * 60)

def my_decorator(func):
    def wrapper():
        print("İlk İşlem")
        func()
        print("İkinci İşlem")

    return wrapper

@my_decorator
def hello_world():
    print("Hello World!")

hello_world()