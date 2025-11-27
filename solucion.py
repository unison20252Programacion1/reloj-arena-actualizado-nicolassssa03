def reloj_arena(m: int, s: str) -> str:
    # Validación de altura positiva
    if m <= 0:
        return "Error: La altura debe ser un entero positivo"

    resultado = []

    # PARTE SUPERIOR (triángulo decreciente)
    # desde 0 espacios / (2*m - 1) caracteres
    # hasta (m-1) espacios / 1 carácter
    for i in range(m):
        espacios = i
        chars = 2 * (m - i) - 1
        resultado.append(" " * espacios + s * chars)

    # PARTE INFERIOR (triángulo creciente)
    # desde (m-2) espacios / 3 caracteres
    # hasta 0 espacios / (2*m - 1) caracteres
    for i in range(1, m):
        espacios = m - 1 - i
        chars = 2 * i + 1
        resultado.append(" " * espacios + s * chars)

    return "\n".join(resultado)
