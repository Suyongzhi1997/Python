class Cat:
    def __init__(self, new_name):
        self.name = new_name
        print("%s 它来了" % self.name)

    def __del__(self):
        print("%s 它走了" % self.name)

    def __str__(self):
        return "我是小猫[%s]" % self.name # 必须返回字符串
tom = Cat("汤姆")
print(tom)