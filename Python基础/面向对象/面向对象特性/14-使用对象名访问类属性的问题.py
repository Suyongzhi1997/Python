class Tool(object):
    # 使用赋值语句定义类属性，记录所有工具对象的数量
    count = 0

    def __init__(self, name):
        self.name = name
        Tool.count += 1


# 创建工具对象
tool1 = Tool("斧头")
tool2 = Tool("锤子")
tool3 = Tool("榔头")


tool3.count = 99 # 使用对象.属性 = 值 赋值语句，只会给对象增加一个属性，而不会影响类属性的值
print("工具使用总数: %d" % tool3.count) 
print("===> %d" % Tool.count)