def main(x,y):
    """
    Given two integers x, y return the "(x+y)*2={answer}" string.
    Args:
        x: int
        y: int
    Returns:
        str: return answer.
    """
    d = x+y
    return f"({x+y})*2={d*2}"
print(main(4,6))