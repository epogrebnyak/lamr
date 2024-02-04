"""Turn a string into ASCII art using a font style."""

from random import choice

from art import ASCII_FONTS, text2art  # type: ignore

# Print available font style names
print("Available fonts:", ", ".join(ASCII_FONTS))

# Print sample ASCII art
font = choice(ASCII_FONTS)
text = "Python 3"
print("\nSample font:", font)
print("Sample text:", text)
result = text2art("Python 3", font=font, space=1)
print("ASCII art:")
print(result)
print("Characters printed:", len(result))
