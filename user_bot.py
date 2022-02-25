def script(check, x, y):
    if check("gold", x, y) > 0:
        return "take"
    return "pass"
