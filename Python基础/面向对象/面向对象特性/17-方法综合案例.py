class Game(object):
    # 历史最高分
    top_score = 0

    def __init__(self, player_name):
        self.playre_name = player_name

    @staticmethod
    def show_help(): # 静态方法--方法内部，不需要访问实例属性和类属性
        print("帮助信息:让僵尸进入大门")
    
    @classmethod
    def show_top_score(cls): # 类方法--方法内部，只需要访问类属性
        print("历史记录: %d" % cls.top_score)
    
    def start_game(self): # 实例方法--方法内部需要访问实例属性
        print("%s 开始游戏啦..." % self.playre_name)


# 1.查看游戏帮助信息
Game.show_help()
# 2.查看历史最高分
Game.show_top_score()
# 3.创建游戏对象
game = Game("小明")
game.start_game()