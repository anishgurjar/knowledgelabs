from enum import Enum

class Model(Enum):
    INCH_14 = "14-inch"
    INCH_16 = "16-inch"

class Chip(Enum):
    M3 = "M3"
    M3_PRO = "M3 Pro"
    M3_MAX = "M3_Max"

class Color(Enum):
    SILVER = "Silver"
    SPACE_GRAY = "Space Gray"

class RAM(Enum):
    GB4 = 4
    GB8 = 8
    GB16 = 16
    GB32 = 32    

class Storage(Enum):
    GB256 = 256    
    GB512 = 512
    GB1024 = 1024
    GB2048 = 2048
    GB3096 = 3096