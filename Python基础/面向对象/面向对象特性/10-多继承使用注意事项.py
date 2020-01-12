class A:
    def test(self):
        print("A类方法")

    def demo(self):
        print("A---demo方法")


class B:
    def test(self):
        print("B类方法")

    def demo(self):
        print("B---demo方法")


class C(B, A):
    pass


c = C()
c.test()
c.demo()

# 方法搜索顺序
print(C.__mro__)
