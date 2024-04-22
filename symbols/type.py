__package__ = "symbols"
from lexer.word import Word
from lexer.tag import Tag

class Type(Word):
    width = 0
    def __init__(self, s, tag, w):
        super().__init__(s, tag)
        self.width = w
    
    def numeric(self, p):
        if self == Type.Char or self == Type.Int or self == Type.Float:
            return True
        return False
    def max(self, p1, p2):
        if not self.numeric(p1) or not self.numeric(p2):
            return None
        elif p1 == Type.Float or p2 == Type.Float:
            return Type.Float
        elif p1 == Type.Int or p2 == Type.Int:
            return Type.Int
        else:
            return Type.Char
    

Type.Int = Type("integer", Tag.BASIC, 4)
Type.Float = Type("double", Tag.BASIC, 8)
Type.Char = Type("char", Tag.BASIC, 1)
Type.Bool = Type("bool", Tag.BASIC, 1)
