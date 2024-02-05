"""Turn a string into ASCII art using a font style."""

from random import choice

from art import ASCII_FONTS, text2art  # type: ignore

font = choice(ASCII_FONTS)
text = "Python 3"
print("Sample font:", font)
print("Sample text:", text)
result = text2art("Python 3", font=font, space=0)
print("ASCII art:")
print(result)
