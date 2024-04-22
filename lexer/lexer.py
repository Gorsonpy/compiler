from .word import Word
from .tag import Tag
import sys

class Lexer:
    line = 1
    peek = ' '
    words = {}
    def reverse(self, w):
        self.words[w.lexeme] = w
    def __init__(self):
        self.reserve(Word("if", Tag.IF))
        self.reserve(Word("else", Tag.ELSE))
        self.reserve(Word("while", Tag.WHILE))
        self.reserve(Word("do", Tag.DO))
        self.reserve(Word("break", Tag.BREAK))
        self.reserve(Word.true)
        self.reserve(Word.false)
        self.reserve(Word.temp)
    
    def readch(self):
        self.peek = sys.stdin.read(1)
    
    def readch_check(self, c):
        self.readch(self)
        if self.peek != c:
            return False
        self.peek = ' '
        return True
    