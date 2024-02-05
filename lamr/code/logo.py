"""Turn a string into ASCII art using a font style."""

from random import choice

from art import ASCII_FONTS, text2art  # type: ignore

font = choice(ASCII_FONTS)
slogan = "Python 3"
result = text2art(slogan, font=font, space=0)
print("Sample font:", font)
print("Sample text:", text)
print("ASCII art:")
print(result)
