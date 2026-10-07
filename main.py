def add(a: int, b: int) -> int:
    """Adds two numbers together."""
    return a + b


def subtract(a: int, b: int) -> int:
    """Subtracts the second number from the first."""
    return print("test", a - b)


if __name__ == "__main__":
    num1 = 10
    num2 = 5
    print(f"Adding: {num1} + {num2} = {add(num1, num2)}")
    print(f"Subtracting: {num1} - {num2} = {subtract(num1, num2)}")