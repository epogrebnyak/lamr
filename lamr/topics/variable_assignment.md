---
title: Variable assignment
tldr: "`a=1` is an example of variable assignment."
---

In Python operator `=` is used to assign, or 'bind', a value to a variable.

Examples of assignment:

```python
name = "Joe"
age = 28
dist = 7 * 1.5
```

## Walk through an example

What does the statement `dist = 7 * 15` mean?

Expression to the right of the `=` operator (`7 * 15`) is evaluated first
and the result of this evaluation (`105`) is attached to the variable name on the left (`dist`).

When the variable name `dist` is used again in your program, Python will know to substitute it for the value stored for that variable (`105`). Same thing happens for `name` and `age` variables.

**Example 1**. Which variables are used in code below?
What values get assigned to them?

```python
r = 2.5
area = 3.14 * r * r
print(area)
```

**Example 2**. How does the value of `multiple_greetings` variable get constructed?
What value gets printed?

```python
greeting = "Hello"
multiple_greetings = (greeting + "!" + " ") * 3
print(len(multiple_greetings))
```

## Assignment operator may update a variable itself

Assignment in Python works to update the variable itself.
This happens if you encounter the same variable name on both sides of assignment operator.
Usual rule applies:

> Take whatever there is on the right side of `=`,
> evaluate it and bind to the variable name on the left.

**Example 3.** On line 1 `n` was assigned value 1,
on line 2 there is an expression that says
'take the current value of `n` and add 3'.
The resulting value of `n` is 4.

```python
n = 1
n = n + 3
print(n)
```

**Example 3.** Changing strings:

```python
favourite_food = "My favourite food is mushroom soup."
print(favourite_food)

# Later in the same program - the variable changes.

favourite_food = "Now my favourite food is apple pie."
print(favourite_food)
```

<!--
**Excercise.** Consider `total_dist` variable that shows the distance
walked by a person in a week. Demonstrate how it can accumulate values.
-->

## Assignment operator in other programming languages

Given the `=` sign assignment may seem similar to mathematic equivalence,
while it is a different concept (`x = x + 1` not vaild in mathematics).

To highlight the difference between variable assignment and a mathematic equation,
some other programming languages use `:=` (Pascal) or `<-` (R) as an assignment operator.
This notation is not used in Python.

Pascal:

```pascal
x := 1   // assignment of value 1 to variable x in Pascal
```

R programming language:

```R
y <- 3   # assignment of value 3 to variable y in R
```

## Suggested reading

- <https://greenteapress.com/thinkpython2/html/thinkpython2003.html#sec16>
- <https://jakevdp.github.io/WhirlwindTourOfPython/03-semantics-variables.html>
