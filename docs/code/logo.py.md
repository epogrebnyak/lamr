---
title: ASCII art logo
---
Turn a string into ASCII art using a font style.

```python
from random import choice

from art import ASCII_FONTS, text2art  # type: ignore

font = choice(ASCII_FONTS)
slogan = "Python 3"
result = text2art(slogan, font=font, space=0)
print("Sample font:", font)
print("Sample text:", text)
print("ASCII art:")
print(result)
```

> Run ```lamr code logo.py --all``` to get this code with excercises.

## Review questions

1. What is ASCII? What is ASCII art? How could you use it?
2. What does `text2art()` function do? What arguments does `text2art()` accept? What is their meaning?
3. Each time you run the program the text font changes. Why?
4. What is the meaning of the word 'font' in this program?
5. Which of the fonts styles displayed you liked? Why are they appealing?
6. If you created you new font style for ASCII art what would it be?

## Excercises

1. Print a set of ASCII symbols to console.
2. Consult with https://github.com/sepandhaghighi/art/blob/master/FontList.ipynb 
Pick a font name and use it in your program.   

3. How many charaters does the logo you selected have? How many lines?
4. See what `print("Available fonts:", ", ".join(ASCII_FONTS))` does.
5. Print a text in `n` random styles. Set `n` to various numbers (for example 2, 3, or 5).
6. Think how you can implement the following user scenario in a Python program. 
    - Ask a user for input - what text to put on a logo.
    - Pick a few font styles that you think are most impressive.
    - Print a logo using these styles.
    - Ask which logo user likes, print the logo that the user selected.
    - If the user is unhappy continue with more logos.

7. Write a program for the first few or all of the steps of the above scenario.

## References

1. How do I get a list of all the ASCII characters using Python? URL: <https://stackoverflow.com/a/5891469/1758363>
2. Wiki about ASCII art. URL: <https://en.wikipedia.org/wiki/ASCII_art>
3. ASCII Generator. URL: <https://ascii-generator.site/t/>
4. Dive into `art` package code (with caution, the code is a bit old-fashioned). URL: <https://github.com/sepandhaghighi/art/blob/abfc138110e04f44ce489556e8ed5cf14dee671f/art/art.py#L480>
