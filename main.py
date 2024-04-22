__package__ = "main"
from lexer.lexer import Lexer
from lexer.tag import Tag
if __name__ == "__main__":
    lexer = Lexer()
    # 使用lexer读取miniRC.in 拆分成token保存到myout.txt
    with open("miniRC.in", "r") as f:
        with open("myout.txt", "w") as out:
            while True:
                token = lexer.scan(f)
                if token is None:
                    break
                out.write(f"{token}\n")