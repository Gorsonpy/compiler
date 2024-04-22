# tag 用于区别不同的 Token，Num 继承 Token，Num 有一个 value 属性，用于存储数字的值。
class Token:
    def __init__(self, tag):
        self.tag = tag
    def __str__(self):
        return "" + str(self.tag)