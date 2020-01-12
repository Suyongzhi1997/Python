class Animal:
    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

    def run(self):
        print("跑")

    def sleep(self):
        print("睡")


class Dog(Animal):
    # def eat(self):
    #     print("吃")

    # def drink(self):
    #     print("喝")

    # def run(self):
    #     print("跑")

    # def sleep(self):
    #     print("睡")

    def bark(self):
        print("汪汪汪叫~~~")



dog = Dog()
dog.eat()
dog.drink()
dog.run()
dog.sleep()
dog.bark()