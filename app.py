"""Simple demo application for the Jenkins pipeline."""


def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Return the difference of two numbers."""
    return a - b


def greet(name):
    """Return a greeting for the given name."""
    if not name:
        raise ValueError("name must not be empty")
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(greet("Jenkins"))
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 2 = {subtract(5, 2)}")
