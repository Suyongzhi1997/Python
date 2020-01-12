def demo1():
    return  int(input("请输入整数:"))


# 利用异常的传递性，在主程序中捕获异常
try:
    print(demo1())
except Exception as identifier:
    print("未知错误:%s" % identifier)