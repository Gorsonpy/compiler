__package__ = "lexer"
from .word import Word
from symbols.type import Type
from .tag import Tag
from .token import Token
from .num import Num
from .real import Real
import sys

class Lexer:
    line = 1
    peek = ' '
    words = {}
    def reserve(self, w):
        self.words[w.lexeme] = w
    def __init__(self):
        self.reserve(Word("if", Tag.IF))
        self.reserve(Word("read", Tag.READ))
        self.reserve(Word("write", Tag.WRITE))
        self.reserve(Word("for", Tag.FOR))
        self.reserve(Word("repeat", Tag.REPEAT))
        self.reserve(Word("until", Tag.UNTIL))
        self.reserve(Word("function", Tag.FUNCTION))
        self.reserve(Word("return", Tag.RETURN))
        self.reserve(Word("else", Tag.ELSE))
        self.reserve(Word("while", Tag.WHILE))
        self.reserve(Word("do", Tag.DO))
        self.reserve(Word("break", Tag.BREAK))

        self.reserve(Word.true)
        self.reserve(Word.false)
        self.reserve(Type.Int)
        self.reserve(Type.Char)
        self.reserve(Type.Float)
        self.reserve(Type.Bool)

    
    def readch(self, file):
        self.peek = file.read(1)
    
    def readch_check(self, c, file):
        self.readch(file)
        if self.peek != c:
            file.seek(file.tell() - 1)
            return False
        self.peek = ' '
        return True
    
    def scan(self, file):
        while(1):
            self.readch(file)
            if self.peek == '#':
                while(True):
                    self.readch(file)
                    if self.peek == '\n':
                        self.line = self.line + 1
                        break
            elif self.peek == ' ' or self.peek == '\t':
                continue
            elif self.peek == '\n':
                self.line = self.line + 1
            else:
                break
        
        
        if self.peek == '&':
            if self.readch_check('&', file):
                return Word.andd
            else:
                return Token('&')
        elif self.peek == '|':  
            if self.readch_check('|', file):
                return Word.orr
            else:
                return Token('|')
        elif self.peek == '=':
            if self.readch_check('=', file):
                return Word.eq
            else:
                return Token('=')
        elif self.peek == '!':
            if self.readch_check('=', file):
                return Word.ne
            else:
                return Token('!')
        elif self.peek == '<':
            if self.readch_check('=', file):
                return Word.le
            else:
                return Token('<')
        elif self.peek == '>':
            if self.readch_check('=', file):
                return Word.ge
            else:
                return Token('>')
        
        # 处理.5,识别为0.5
        if self.peek == '.':
            x = 0
            d = 10.0
            while True:
                self.readch(file)
                if not self.peek.isdigit():
                    file.seek(file.tell() - 1)
                    break
                x = x + int(self.peek) / d
                d = d * 10
            return Real(x)

        if self.peek.isdigit():
            v = 0
            while True:
                v = 10 * v + int(self.peek)
                self.readch(file)
                if not self.peek.isdigit():
                    break
            if self.peek != '.':
                file.seek(file.tell() - 1)
                return Num(v)
            
            x = v * 1.0
            d = 10.0
            while True:
                self.readch(file)
                if not self.peek.isdigit():
                    file.seek(file.tell() - 1)
                    break
                x = x + int(self.peek) / d
                d = d * 10

            return Real(x)
        
        if self.peek.isalpha():
            b = ''
            while True:
                b = b + self.peek
                self.readch(file)
                if not self.peek.isalpha():
                    file.seek(file.tell() - 1)
                    break
            
            # 是规定的保留词
            w = self.words.get(b)
            if w != None:
                return w
            
            w = Word(b, Tag.ID)
            self.words[b] = w
            return w
        
        tok = Token(self.peek)

        if self.peek == '':
            tok = None

        self.peek = ' '
        return tok
        