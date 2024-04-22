__package__ = "lexer"
from .token import Token
from .tag import Tag

# Word 用于管理保留字、标识符和像&&这样的多字符词法单元
class Word(Token):
    lexeme = ''
    def __init__(self, lexeme, tag):
        super().__init__(tag)
        self.lexeme = lexeme
    def __str__(self):
        if self.tag == Tag.ID:
            return f"<id, {self.lexeme}>"
        else:
            return f"<{self.lexeme}>"

Word.andd = Word("&&", Tag.AND)
Word.orr = Word("||", Tag.OR)
Word.eq = Word("==", Tag.EQ)
Word.ne = Word("!=", Tag.NE)
Word.le = Word("<=", Tag.LE)
Word.ge = Word(">=", Tag.GE)
Word.minus = Word("minus", Tag.MINUS)
Word.true = Word("true", Tag.TRUE)
Word.false = Word("false", Tag.FALSE)
Word.temp = Word("t", Tag.TEMP)

    