# Task 4: Closures & `nonlocal`

## Objective
Understand how inner functions capture variables from their enclosing scope, and how to mutate those variables.

## What to Learn

### Closures

When you define a function inside another function, the inner function can access the outer function's variables. That's nothing special — same as any nested scope. What *is* special: the inner function remembers those variables **even after the outer function returns**. This "remembering" is a closure.

Why would you want this? It lets you create functions that carry built-in state or configuration — without classes, without globals. You call the outer function to set things up, and it hands you back an inner function that's ready to use.

```python
def make_greeter(greeting):
    def greet(name):
        return f"{greeting}, {name}!"
    return greet

hello = make_greeter("Hello")
print(hello("Alice"))  # → Hello, Alice!
print(hello("Bob"))    # → Hello, Bob!

yo = make_greeter("Yo")
print(yo("Alice"))     # → Yo, Alice!
```

`make_greeter` returns the `greet` function. `greet` remembers the value of `greeting` from when `make_greeter` was called — that's the closure. Each call to `make_greeter` creates a *separate* closure with its own captured value.

### Mutating captured variables with `nonlocal`

You can *read* a captured variable freely. But if you try to *reassign* it (put it on the left side of `=`), Python treats it as a new local variable and throws an `UnboundLocalError`. The `nonlocal` keyword tells Python: "this name belongs to the enclosing scope — don't create a new local."

```python
def make_accumulator(start):
    total = start
    def add(n):
        nonlocal total
        total += n
        return total
    return add

acc = make_accumulator(10)
print(acc(5))   # → 15
print(acc(3))   # → 18
print(acc(100)) # → 118
```

Without `nonlocal total`, the line `total += n` would fail — Python would see `total` on the left side of `=` and treat it as an undefined local.

Rule of thumb: if your inner function only *reads* the captured variable, you don't need `nonlocal`. If it *reassigns* the variable, you do.

## Exercise

### 1. `counter()`
Write a function `counter()` that returns a function. Each call to the returned function increments and returns a count, starting from 1.

```python
c = counter()
c()  # → 1
c()  # → 2
c()  # → 3
```

### 2. `make_multiplier(factor)`
Write a function that takes a `factor` and returns a function that multiplies its argument by that factor.

```python
double = make_multiplier(2)
triple = make_multiplier(3)
double(5)   # → 10
triple(5)   # → 15
```
