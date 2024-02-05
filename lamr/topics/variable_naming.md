---
title: Variable naming
tldr: Language conventions and common sense guide variable naming.
---

Choosing a name for variable is not easy.
There are just formal limitations on variable names (PEP8 in Python),
but picking the right name should strikes a balance between brevity
and being well-understood by people who read your code.

Programmers may not agree what makes a good variable name
except for trivial cases like `x`, `y`, `z` for 3D coordinates
or `i`, `j`, `k` for matrix indices.

## Quotes

### Think about your readers

> If it's an `account_id` then don't call it `acc_id`.
> Long term think about who is going to read this content: other developers, data scientists, you
> (after you've forgotten everything). Ensure those names are consistent with other names as well!
> If you're using snake case, keep snake case everywhere. Consistency helps minimize cognitive load,
> people will learn and understand patterns from the consistent naming conventions.

Source: "Data modeling is hard" by Anton Kropp [via reddit](https://www.reddit.com/r/programming/comments/1aibp2h/data_modeling_is_hard/).

### Which of the variable naming rules are harder to follow?

Several variable naming ideas from <you.com>:

1. Choosing good variable names is an important part of writing code that is easy to read and understand.
2. The name of the variable should be descriptive and accurately describe what the variable holds or what it is used for.
3. It should be concise and include only the necessary words to clearly describe the variable.
4. Additionally, it should avoid the use of acronyms and abbreviations that may be confusing or ambiguous.
5. It is also important to avoid using generic terms like "data" or "value" as variable names.
6. Finally, it is important to be consistent with variable naming conventions across the codebase.

Which of the above is the most and least difficult to adhere to?
Do any of these contradict each other? Explain why.
