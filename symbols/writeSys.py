from lexer.tag import Tag
__package__ = "symbols"
class WriteSys:
    haveLogin = {}
    keys = []
    ids = []
    def store(self, token, file):
        # 如果是普通的token,tag是实际的字符串不是数字
        t = token.tag
        if isinstance(token.tag, int):
            if token.tag == Tag.NUM or token.tag == Tag.REAL or token.tag == Tag.GE or token.tag == Tag.LE or token.tag == Tag.EQ or token.tag == Tag.NE or token.tag == Tag.AND or token.tag == Tag.OR:
                return
            s = token.lexeme
            if self.haveLogin.get(s) == None:
                self.haveLogin[s] = True
                if token.tag == Tag.ID:
                    pre = "IDENTIFIER"
                    self.keys.append(f"{pre} {s}")
                else:
                    pre = "KEYWORD"
                    self.ids.append(f"{pre} {s}")

    def write(self, file):
        for i in range(len(self.ids)):
            file.write(f"{self.ids[i]}\n")
        for i in range(len(self.keys)):
            file.write(f"{self.keys[i]}\n")
        
