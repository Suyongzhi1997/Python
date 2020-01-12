class A:
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200

    def __test(self):
        print("私有方法 %d %d" % (self.num1, self.__num2))

    def test(self):
        print("父类公有方法 %d" % self.__num2)
        self.__test()


class B(A):
    def demo(self):
        # 1.访问父类的私有属性,不能访问！
        # print("访问父类的私有属性 %d" % self.__num2)
        # 2.调用父类的私有方法，不能调用!
        # self.__test()
        # 3.访问父类的公有属性
        print("访问父类中的公有属性")
        # 4.调用父类的公有方法
        self.test()


# b = B()
# b.demo()
# print(b.num1)
# b.test()

a = A()
a.test()
