#!/usr/bin/env python3
# In lib/functions.py
def greet(name):
    print(f"Hello, {name}!")
    
def greet_programmer():
    print("Hello, programmer!")

def greet_programmer():
    greeting = "programmer"
    print(f"Hello, {greeting}!")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

def add(num1: int | float, num2: int | float) -> int | float:
    """Add two numbers together and return the result."""
    return num1 + num2

def halve(number: int | float) -> float | None:
    """Halves the input number if it's numeric, otherwise returns None."""
    if not isinstance(number, (int, float)):
        return None
    return number / 2