from enum import Enum


class Emoji(str, Enum):
    CHECK = "✅"
    ERROR = "❌"
    INFO = "ℹ️"


class Color(int, Enum):
    ERROR = 0xFF0000
    SUCCESS = 0x00FF00
    INFO = 0x0000FF