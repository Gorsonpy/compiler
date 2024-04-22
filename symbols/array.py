__package__ = "symbols"
from .type import Type
from lexer.tag import Tag

class Array(Type):
    of = None # 数组元素类型
    size = 1 # 元素个数
    def __init__(self, sz, p):
        super().__init__("[]", Tag.INDEX, sz * p.width)
        self.size = sz
        self.of = p
    def __str__(self):
        return "[" + str(self.size) + "]" + str(self.of)