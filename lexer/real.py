from .token import Token
from .tag import Tag

# Real 用于处理浮点数
class Real(Token):
    def __init__(self, value):
        super().__init__(Tag.REAL)
        self.value = value
    def __str__(self):
        return "" + str(self.value)