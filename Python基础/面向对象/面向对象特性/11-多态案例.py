class Dog(object):
    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s 蹦蹦跳跳地玩耍" % self.name)


class XiaoTianQuan(Dog):
    def game(self):
        print("%s 飞到天上去玩耍" % self.name)


class Person(object):
    def __init__(self, name):
        self.name = name

    def play_with_dog(self, dog):
        print("%s 和 %s快乐的玩耍" % (self.name, dog.name))
        dog.game()


# wangcai = Dog("旺财")
wangcai = XiaoTianQuan("飞天旺财")
xiaoming = Person("小明")
xiaoming.play_with_dog(wangcai)
