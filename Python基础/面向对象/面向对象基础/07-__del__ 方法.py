class Cat:
    def __init__(self, new_name):
        self.name = new_name
        print("%s 它来了" % self.name)

    def __del__(self):
        print("%s 它走了" % self.name)


tom = Cat("汤姆")
print("*" * 30)