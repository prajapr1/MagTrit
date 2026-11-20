"""Balanced ternary (-1, 0, +1) logic gate primitives and single-trit full adder."""

VALID_TRITS = (-1, 0, 1)


def validate_trit(t: int) -> int:
    if t not in VALID_TRITS:
        raise ValueError(f"Invalid trit {t!r}; expected one of {-1, 0, 1}")
    return t


def sti(a: int) -> int:
    """Standard Ternary Inverter: negates sign while keeping 0."""
    validate_trit(a)
    return -a


def pti(a: int) -> int:
    """Positive Ternary Inverter."""
    validate_trit(a)
    return -1 if a == 1 else 1


def nti(a: int) -> int:
    """Negative Ternary Inverter."""
    validate_trit(a)
    return 1 if a == -1 else -1


def t_min(a: int, b: int) -> int:
    """Ternary MIN gate."""
    validate_trit(a)
    validate_trit(b)
    return min(a, b)


def t_max(a: int, b: int) -> int:
    """Ternary MAX gate."""
    validate_trit(a)
    validate_trit(b)
    return max(a, b)


def full_adder_trit(a: int, b: int, carry_in: int = 0) -> tuple[int, int]:
    """Add two trits plus incoming carry (-1..+1). Returns (sum_trit, carry_out)."""
    validate_trit(a)
    validate_trit(b)
    validate_trit(carry_in)
    total = a + b + carry_in
    if total > 1:
        return total - 3, 1
    if total < -1:
        return total + 3, -1
    return total, 0
