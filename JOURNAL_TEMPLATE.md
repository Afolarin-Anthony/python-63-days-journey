# Day 1

**Date:** 2026-10-10  
**Phase:** Foundations
**Status:** In Progress

## Learning Objectives

By the end of this phase, I want to:

- Understand python modules and how to use them.
- Build discipline in reading, writing code
- Understand programming generally

## Module of the Day

**Module:** `sys`

**Purpose:**
Talking to the interpreter and the Operating system

## Concepts Learned

- A form of error handling
- OS enumeration


## Practice Completed

### Exercise 1: [exercise_1.py]

**Problem:**

Print out certain information about the platform and python version.

**Approach:**

I used the print function on sys.version and sys.platform
**Result:**

Successfully printed it out.

### Exercise 2: [exercise_2.py]

**Problem:**

Writing a python script that counts the number of arguments it receives

**Approach:**

Used the len() counting function

**Result:**

Returned the number of arguments in numeric form.

## Code Example

import sys
print("Number of arguments:", len(sys.argv))
sys.exit(0) # 0 means success

Learnt about enumerate(), stderr.
