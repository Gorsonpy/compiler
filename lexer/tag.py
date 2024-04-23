# 定义了一些常量来表征这是什么类型的token
# 例如Tag.NUM表示这是一个数字类型的token
__package__ = "lexer"
class Tag:
    ERR = -1
    AND = 256
    BASIC = 257
    BREAK = 258
    DO = 259
    ELSE = 260
    EQ = 261
    FALSE = 262
    GE = 263
    ID = 264
    IF = 265
    INDEX = 266
    LE = 267
    MINUS = 268
    NE = 269
    NUM = 270
    OR = 271
    REAL = 272
    TEMP = 273
    TRUE = 274
    WHILE = 275
    FUNCTION = 276
    RETURN = 277
    READ = 278
    WRITE = 279
    FOR = 280
    REPEAT = 281
    UNTIL = 282