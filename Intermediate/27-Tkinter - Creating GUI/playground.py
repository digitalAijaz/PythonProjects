def add(*numbers):
    # print(numbers[1])

    sum = 0
    for i in numbers:
        # sum += i
        sum += numbers[i]
    # print(sum)


add(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)


def calculate(n, **kwargs):
    # for key,value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        # self.make = kw["make"]
        # self.model = kw["model"]

        self.make = kw.get("make")
        self.model = kw.get("model")
        self.version = kw.get("version")

my_car = Car(make ="Tata", model = "Nexon")
print(my_car.make, my_car.model, my_car.version)
