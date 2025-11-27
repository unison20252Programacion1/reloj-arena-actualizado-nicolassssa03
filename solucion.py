def reloj_arena(m: int, s: str) -> str:
    if m <= 0:
        return "Error: La altura debe ser un entero positivo"

    resultado = []

    for i in range(m):
        espacios = i
        chars = 2 * (m - i) - 1
        resultado.append(" " * espacios + s * chars)

    for i in range(1, m):
        espacios = m - 1 - i
        chars = 2 * i + 1
        resultado.append(" " * espacios + s * chars)

    return "\n".join(resultado)
