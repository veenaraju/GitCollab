"""Simple Calculator - Team Collaboration Demo."""


def add(a: int, b: int) -> int:
    """Adds two numbers together."""
    return a + b


if __name__ == "__main__":
    num1 = 10
    num2 = 5
    print(f"Adding: {num1} + {num2} = {add(num1, num2)}")
