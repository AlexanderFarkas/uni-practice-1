def format_float(value: float) -> str:
    if value.is_integer():
        return str(int(value))
    else:
        return str(value)