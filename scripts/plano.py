def calcular_ecuacion_plano(N):
    # Vector normal
    A = 11
    B = -1
    C = -8

    # Punto A
    x0 = 7 * N
    y0 = 5 * N
    z0 = 8 * N

    # Constante D calculada usando el punto A
    D = -(A * x0 + B * y0 + C * z0)

    # Ecuación del plano
    print(f"La ecuación del plano es: {A}x + {B}y + {C}z + {D} = 0")

# Solicitar el valor de N
N = float(input("Introduce el valor de N: "))
calcular_ecuacion_plano(N)
