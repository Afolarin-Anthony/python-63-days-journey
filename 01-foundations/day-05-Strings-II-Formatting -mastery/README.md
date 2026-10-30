# PYTHON LEARNING
# DAY 5: Strings II : Formatting Mastery
### DATE: 23rd October 2026
### STATUS: Completed

## Concept: Become fluent with f‑strings and format specifiers, then shape output with textwrap for reports and CLIs.

## The module that brings the concept to life is the "textwrap" module.

## Examples
- The f strings - Python's modern way of inserting values into strings in a controlled manner. e.g. print(f"my name is {variable gets placed here}").
- (f"{variable_name:.1f}) ----> Rounds up number especially a float to 1 decimal point.
- (f"{variable_name:,}) ------> Separate large numbers with commas making them easier to read.
- (f"{variable_name:>10}) ----> Aligns the text value to the right.
- (f"{variable_name:<10}) ----> Aligns the text value to the left.
- (f"{variable_name:^20}) ----> Center aligns the text value.
- (f"{variable_name:04d}) ----> Pads the number with an amount of leading zeros.

## The textwrap module
- textwrap.wrap(text, width) — list of wrapped lines
- textwrap.fill(text, width) — wrapped lines joined with newlines
- textwrap.shorten(text, width) — truncate with a placeholder
- textwrap.dedent(block) — strip shared leading whitespace
- textwrap.indent(text, prefix) — prefix every line


## What I learnt
- We can programm output in a neatly manner and so much as drawing tables, grids.
- We can use the f strings to format numbers to round numbers up and put in commas.
  


 

## More researched
- There are older formatting methods used before f strings and they are still being used for specific jobs like templating by python programmers. E.g Percent formatting (%) and the .format() method
