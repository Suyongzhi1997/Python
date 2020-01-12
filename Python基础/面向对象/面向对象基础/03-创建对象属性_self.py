class Cat:
    def eat(self):
        # 哪一个对象调用方法，self就是哪一个对象的引用
        print("%s爱吃鱼" % self.name)

    def run(self):
        print("%s爱运动" % self.name)


tom = Cat()

# 可以使用 .属性名,利用赋值语句
tom.name = "汤姆"
tom.eat()
tom.run()

lazy = Cat()
lazy.name = "大懒猫"
lazy.eat()
lazy.run()