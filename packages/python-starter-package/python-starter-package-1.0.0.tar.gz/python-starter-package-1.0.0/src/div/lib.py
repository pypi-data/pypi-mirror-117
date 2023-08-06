class InvalidDivideError(RuntimeError):
    """Error generated if denominator is zero."""


def divide(a: float, b: float) -> float:
    """Divides first input with the second input.

    Args:
        a: Numerator
        b: Denominator

    Raises:
        InvalidDivideError: If denominator is 0

    Returns:
        Computed division.
    """
    if b == 0:
        raise InvalidDivideError("Divide by zero error")

    return a / b
