# Variables

## What is a variable?

> A variable is a name that is bound to a value.

A variable is an identifier that is used to refer to a specific value
stored in the memory of a computer.
The variable serves as a "nickname", or an "alias", for the value.

The value can be of various types, such as a number, a string, or some other object,
and it can be passed to various parts of the program, modified or reassigned
during the execution of the program.

Concept of a variable in programming is slightly different from mathematics.
In mathematics, a variable is often used to represent an unknown value that needs to be derived by solving an equation.
In programming the variable value is known after assignment and can be used in further computations.

### Questions and excercises

1. Does the variable name always remain the same throughout the program?
1. Does the variable value always remain the same throughout the program?

## Variable assignment

> `x=1` is an example of variable assignment.

In Python operator `=` is used to assign a value to a variable.
Expression to the right of the `=` operator is evaluated first,
and the result is then assigned to the variable name on the left.

```python
r = 2.5
area = 3.1415 * r * r
print(area)
```

::: details Assignment operator in other programming languages

To highlight the difference between variable assignment and mathematic equation,
some other programming languages use `:=` (Pascal) or `<-` (R) as an assignment operator.

&nbsp;

```pascal
x := 1   // assignment of value 1 to variable x in Pascal
```

&nbsp;

```R
y <- 3   # assignment of value 3 to variable y in R
```

:::

## Changing variables

> In Python all variables are mutable.

After initially assigning a value to a variable in Python you can reassign
a new value to it.

Here is an example with strings.

```python
favourite_food = "My favourite food is mushroom soup."
print(favourite_food)

# later in the same program

favourite_food = "Now my favourite food is apple pie."
print(favourite_food)
```

Another example that uses integers:

```python
year = 1991       # assignment of value of 1991 to variable
year = year + 1   # new assignment to variable, not an equation
print(year)       # prints 1992
```

A typical situation where a variable changes is a counter,
a variable that increases by one at each step.

```python
string = ("Now my favourite food is Apple Pie, " +
          "but I liked Mushroom Soup before.")
letter = "m"
counter = 0
for s in string:
   if s == letter:
      counter = counter + 1
print("We searched for letter:", letter)
print("In the following string:", string)
print("The letter was found", counter, "times")
```

### Questions and excercises

1. In code example above screw the counter to wrong starting value.
1. Think of different and better variable names instead of `string`, `s`, `letter` and `counter` in code above.
1. Count number of spaces in `string` and print the result.
1. What other variable does seem to change other than `counter`?
1. Try removing `if` from code. How did the meaning of code change? What else needs to be changed in this code without `if`?
1. Can we adapt this code to search for any letter, regardless of lower or upper case?
1. Can we adapt this code to search for letter combinations?

## Constants and immutability

> In Python variables with UPPERCASE names are assumed to remain unchanged.

Python does not have a concept of **constants** like other languages.
To indicate a constant the variable name is written with uppercase letters.

```python
LANGUAGE = "Python"
print(LANGUAGE)
```

Question: what might be a constant in your program? Explain why this value will not change.

However, this behavior it is not a syntax rule, but a matter of agreement, or a convention.
Python does not have a built-in mechanism for enforcing this convention at interpreter level.
This means one can reassign a new value to a variable even if the variable name is written
in uppercase letters. (This would not be considered a good code practice.)

```python
KM_PER_MILE = 1.6
print("One kilometer is about",  round(1/KM_PER_MILE, 2), "miles")

# ... but I want more precision!
KM_PER_MILE = 1.60934
print("One kilometer is about",  round(1/KM_PER_MILE, 2), "miles")

# Peer advice: define KM_PER_MILE just once and do not change it.
```

Note that some [real code to the similar purpose of calculating distances][geopy]
avoids using global constants.

[geopy]: https://github.com/geopy/geopy/blob/master/geopy/units.py

::: details Immutability

In some other programming languages, variables are immutable by default,
which means that once a value is assigned to a variable, it cannot be changed.
To store computation results either new variables are created or a variable has to
declared as mutable when first introduced.

Mutable variables perhaps allow to start writing quick code.
Immutable variables have their own benefits -- for example,
they cannot be changed accidentally and the program behavior is more predictable.
:::

## Variable naming in Python

> Language conventions and common sense guide variable naming.

Variable naming is not as easy at it may first sound.
While there are just a few formal syntax limitations on variable names,
picking the right name that strikes a balance between brevity
and being well-understood by people who read your code is rather difficult.
Programmers may not agree what makes a good variable name, except for trivial
cases like `x` and `y` for coordinates on a two-dimensional plaine.

Variable naming ideas from you.com:

> 1. Choosing good variable names is an important part of writing code that is easy to read and understand.

> 2. The name of the variable should be descriptive and accurately describe what the variable holds or what it is used for.

> 3. It should be concise and include only the necessary words to clearly describe the variable.

> 4. Additionally, it should avoid the use of acronyms and abbreviations that may be confusing or ambiguous.

> 5. It is also important to avoid using generic terms like "data" or "value" as variable names.

> 6. Finally, it is important to be consistent with variable naming conventions across the codebase.

Which of the above is the most and least difficult to adhere to? Explain why.
