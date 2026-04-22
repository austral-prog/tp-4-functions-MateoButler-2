# Replace the "ANSWER HERE" for your answer

def roots(a, b, c):
    discriminante = b**2 - 4 * a * c
    if discriminante >= 0:

        r1 = (-1 * b + discriminante**0.5) / (2 * a)
        r2 = (-1 * b - discriminante**0.5) / (2 * a)

        if r1 != r2:
            return (f"({r1}, {r2})")
        else:
            return (f"({r1})")
    else:
        return ("( )")


def value_y(a, b, c, x):

    return a * x**2 + b * x + c

def to_string(a, b, c):
    # Caso result3: Si a y b son 0, solo queda el número solo
    if a == 0 and b == 0:
        return f"f(x) = {c}"

    # Caso result2: Si a es 0, empieza en el término X
    if a == 0:
        return f"f(x) = {b} * X + {c}"

    # Caso result4: Si b es 0, aquí es donde van los DOS ESPACIOS
    if b == 0:
        return f"f(x) = {a} * X^2  + {c}"

    # Caso result1: Si están todos los números, va con UN SOLO ESPACIO
    return f"f(x) = {a} * X^2 + {b} * X + {c}"

def derivation(a, b, c):
    der_a = 2 * a
    der_b = b

    # Caso: f'(x) = 0
    if der_a == 0 and der_b == 0:
        return "f'(x) = 0"
    # Caso: f'(x) = constante
    if der_a == 0:
        return f"f'(x) = {der_b}"
    # Caso: f'(x) = A * X
    if der_b == 0:
        return f"f'(x) = {der_a} * X"

    # Caso completo: f'(x) = A * X + B
    return f"f'(x) = {der_a} * X + {der_b}"