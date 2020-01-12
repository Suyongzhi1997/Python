class Cat:
    def __init__(self):
        print("这是一个初始化方法!!")

        # self.属性名 = 属性的初始值
        self.name = "汤姆"

    def eat(self):
        print("%s爱吃鱼" % self.name)

# 使用类名加括号时会自动调用初始化方法 __init__ 这个方法
tom = Cat()
print(tom.name)
tom.eat()
