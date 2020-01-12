class Gun:
    def __init__(self, model):

        # 1. 枪的型号
        self.model = model

        # 2. 子弹的数量
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count += count

    def shoot(self):
        # 1.判断子弹数量
        if self.bullet_count <= 0:
            print("[%s]没有子弹了..." % self.model)
            return

        # 2.发射子弹
        self.bullet_count -= 1

        # 3.提示法神信息
        print("[%s]发射突突突...[%d]" % (self.model, self.bullet_count))


class Soldier:
    def __init__(self, name):

        # 1.姓名
        self.name = name
        # 2.枪
        self.gun = None

    def fire(self):
        # 1.判断士兵是否有枪
        # if self.gun == None:
        if self.gun is None:
            print("%s 还没有枪!" % self.name)
            return

        # 2.高喊口号
        print("冲冲冲...%s" % self.name)

        # 3.装填子弹
        self.gun.add_bullet(50)

        # 4.发射子弹
        self.gun.shoot()


ak47 = Gun("ak47")

xiaobing = Soldier("小兵张嘎")
xiaobing.gun = ak47
xiaobing.fire()
print(xiaobing.gun)
