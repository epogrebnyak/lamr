# Turing Machine

[![Reddit][reddit-icon]][source]

[reddit-icon]: https://img.shields.io/badge/Reddit-%23FF4500.svg?style=flat&logo=Reddit&logoColor=white
[source]: https://www.reddit.com/r/learnprogramming/comments/1ar1pbc/comment/kqlzlbf/

A Turing machine is a hypothetical machine with an infinite memory tape that can only:

- read the value on the tape,
- write a new value to the tape,
- move the tape left or right to a new position,
- maintain and change between a finite set of states,
- conditionally do the above based on the result of a tape read.

It is proven that mathematically, any machine that can do the above can compute anything that is mathematically computable. 

That is, the set of all problems that a Turing machine be can solve is equal to the set of all problems solvable by lambda calculus (the mathematical formalism of computation, see [Church-Turing thesis][ct]).

[ct]: https://en.m.wikipedia.org/wiki/Church%E2%80%93Turing_thesis

In real life, no Turing machines can exist due to the requirement for an infinite memory. But ignoring that, we call a language Turing complete if it can perform the operations of a Turing machine.

<!--
So all a language needs to be Turing complete is the ability to:

-  read memory
-  write memory (by at least being able to add or subtract 1 from any value)
-  change the spot in memory read and written to.
-  store variables
-  conditionally execute instructions based on its stored variables.

Storing variables/state can be as simple as jumping to a new part of the code for the language. It doesn't require actual permanent data. So function calls or go-to/jump statements satisfy this.
-->

## How about being Turing-incomplete?

Turing completeness is one of those things where it can lead to people using a language for more than is needed from it. [Dhall](https://dhall-lang.org/) is meant as a slightly more powerful way of configuring stuff (like JSON or TOML) but without the full power and complexity of a programming language. HTML by itself is also not Turing complete, as it's only purpose is to create document layouts.

On the other hand, HTML+CSS and Microsoft PowerPoint are Turing complete if you allow for a user to click elements. Microsoft Excel is also Turing complete using just cell formulas. You can find YouTube videos of people who made low-powered CPU emulators in PowerPoint and Excel.

In fact, if you define your language well enough, [a single instruction][si] is all that is needed for a Turing complete language (although very impractical). 

[si]: https://en.m.wikipedia.org/wiki/One-instruction_set_computer

