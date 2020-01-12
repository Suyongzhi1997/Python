class A:
    def testA(self):
        print("A类方法")
    

class B:
    def testB(self):
        print("B类方法")


class C(A,B):
    """ 多继承可以让子类对象，同时具有多个父类的属性和方法 """
    pass


c = C()
c.testA()
c.testB()