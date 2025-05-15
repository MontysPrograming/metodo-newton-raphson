import sympy as sp

# funcion principal
def newton_raphson(fx_str, x0, tol=1e-6, max_iter=100):
    x = sp.symbols('x')
    fx = sp.sympify(fx_str)
    dfx = sp.diff(fx, x)

    print(f"\nMetodo de Newton-Raphson\nFuncion: f(x) = {fx}")
    print(f"Derivada: f'(x) = {dfx}\n")

    for i in range(max_iter):
        fx_val = fx.subs(x, x0).evalf()
        dfx_val = dfx.subs(x, x0).evalf()
        
        if dfx_val == 0:
            print("Error: derivada igual a cero.")
            return None
        
        x1 = x0 - fx_val / dfx_val
        error = abs(x1 - x0)

        print(f"Iteracion {i+1}: x = {x1:.6f}, f(x) = {fx_val:.6f}, Error = {error:.6e}")
        
        if error < tol:
            print(f"\nRaiz aproximada encontrada: {x1:.6f} con error menor a {tol}\n")
            return x1
        
        x0 = x1

    print("No se alcanzo la tolerancia especificada.")
    return None

# entrada desde la consola
if __name__ == "__main__":
    print("Ingrese la función f(x):")
    funcion = input("f(x) = ")
    
    x0 = float(input("Valor inicial x0: "))
    tol = float(input("Tolerancia (por defecto 1e-6): ") or 1e-6)
    max_iter = int(input("Numero maximo de iteraciones (por defecto 100): ") or 100)

    newton_raphson(funcion, x0, tol, max_iter)
