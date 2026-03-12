def validate_amount(amount):
    """
    Rules:
    - cannot be zero
    - cannot be negative
    - must be integer
    """

    if amount == 0:
        raise ValueError("Amount cannot be zero")

    if amount < 0:
        raise ValueError("Amount cannot be negative")

    if not isinstance(amount, int):
        raise ValueError("Amount must be an integer")

    return True


def validate_currency(currency):
    """
    Currency must be 3 letters
    Example: USD, UGX
    """

    if not isinstance(currency, str):
        raise ValueError("Currency must be string")

    if len(currency) != 3:
        raise ValueError("Currency must be 3 characters")

    return True