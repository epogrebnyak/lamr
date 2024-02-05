---
title: Constants and immutability
tldr: In Python variables with UPPERCASE names are assumed to remain unchanged.
---

## Constant

Python does not have constants like other languages. To indicate a constant the variable name is written with uppercase letters.

```python
LANGUAGE = "Python"
print(LANGUAGE)
LANGUAGE = "Javascript" # not nice - breaks reader expectations about LANGUAGE variable
```

However, this behavior it is not a syntax rule, but a matter of agreement, or a convention.
Python does not have a built-in mechanism for enforcing this convention at interpreter level.
This means one can reassign a new value to a variable even if the variable name is written
in uppercase letters. (This would not be considered a good code practice.)

**Question:\*** What might be a constant in your program? Explain why this value should not change.

**Example**: define `KM_PER_MILE` just once and do not change it.

```python
KM_PER_MILE = 1.6
print("One kilometer is about",  round(1/KM_PER_MILE, 2), "miles")

# ... but I want more precision!
KM_PER_MILE = 1.60934
print("One kilometer is about",  round(1/KM_PER_MILE, 2), "miles")
```

Note that some [real code to the similar purpose of calculating distances][geopy]
avoids using global constants.

[geopy]: https://github.com/geopy/geopy/blob/master/geopy/units.py

## Immutability

In some other programming languages, variables are immutable by default,
which means that once a value is assigned to a variable, it cannot be changed.
To store computation results either new variables are created or a variable has to
declared as mutable when first introduced.

Mutable variables perhaps allow to start writing quick code.
Immutable variables have their own benefits - for example,
they cannot be changed accidentally and the program behavior is more predictable.
