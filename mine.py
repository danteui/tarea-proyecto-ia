import scipy.integrate as integrate
import scipy.special as special

# Realizamos la integración de la función de Bessel de primera especie de orden 2.5
# desde 0 hasta 4.5
result, error = integrate.quad(lambda x: special.jv(2.5, x), 0, 4.5)

print(f"Resultado de la integral: {result}")
print(f"Error estimado: {error}")
#eso de ahi muestra cómo integrar numéricamente una función especdcial
#matemática que no tiene una forma cerrada sencilla — algo que sería muy
#difícil de hacer a mano, pero scipy lo resuelve en una línea.cd
