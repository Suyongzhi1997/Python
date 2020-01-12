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

ak47 = Gun("ak47")
ak47.add_bullet(60)
ak47.shoot()

xiaobing = Soldier("小兵张嘎")
xiaobing.gun = ak47
print(xiaobing.gun)