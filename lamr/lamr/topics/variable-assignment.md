---
title: Variable assignment
tldr: `x=1` is an example of variable assignment.
---

In Python operator `=` is used to assign, or 'bind', a value to a variable.

What does the statement `h = 30 * 20 * 5` mean? Expression to the right
of the `=` operator is evaluated first and the result of this evaluation
is attached to the variable name on the left.
Wherever this name is used, Python will know to substitute it
for the value stored for that variable.

**Example 1**. Which variables are used in code below?
What values get assigned to them?

```python
r = 2.5
area = 3.1415 * r * r
print(area)
```

**Example 2**. How does the value of `multiple_greetings` variable get constructed?
What value gets printed?

```python
greeting = "Hello"
multiple_greetings = (greeting + "!" + " ") * 3
print(len(multiple_greetings))
```

## Assignment may update a variable itself

Assignment may seem similar to mathematic equivalence,
yet it should read as 'take whatever there is on the right side,
evaluate it and bind to the variable on the left.'
On the right hand side you may encounter the previous value of the variable itself.
Assignment in Python can be used repeatedly, and works to update the variable.

**Example 3.** On line 1 `n` was assigned value 1,
on line 2 there is an expression that says
'take the current value of `n` and add 3'.
The resulting value of `n` should be 4.

```python
n = 1
n = n + 3
print(n)
```

## Assignment operator in other programming languages

To highlight the difference between variable assignment and mathematic equation,
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
