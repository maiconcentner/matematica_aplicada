# %%
# Determine as solução analítica dos sistemas dinâmicos abaixo
# Ver capítulo 6 - Pulino, pg. 459
# a) x'(t) = -3x(t) + y(t)
#    y'(t) = x(t) - 3y(t)
# com x(0) = 2 e y(0) = 3

import numpy as np
import matplotlib.pyplot as plt

# A solução geral é dada por:
def solucao_analitica(t, c1, c2):
    x = c1 * np.exp(-2 * t) * np.cos(t) + c2 * np.exp(-2 * t) * np.sin(t)
    y = -c1 * np.exp(-2 * t) * np.sin(t) + c2 * np.exp(-2 * t) * np.cos(t)
    return x, y

# %%
# Condições iniciais
c1 = 2
c2 = 3

# Intervalo de tempo
t = np.linspace(0, 10, 100)

# Calculando as soluções analíticas
x, y = solucao_analitica(t, c1, c2)

# Imprimindo as soluções analíticas
for i in range(len(t)):
    print(f"No tempo t = {t[i]:.2f}, x = {x[i]:.4f} e y = {y[i]:.4f}")

# %%
# Plotando os resultados
plt.plot(t, x, label='x(t)')
plt.plot(t, y, label='y(t)')
plt.xlabel('Tempo')
plt.ylabel('Valor')
plt.legend()
plt.grid(True)
plt.show()

# %%
# x'(t) = -5x(t)
# y'(t) = -4y(t) + 3z(t)
# z'(t) = 3y(t) - 4z(t)
# coom x(0) = 4, y(0) = 5 e z(0) = 6

def solucao_analitica2(t, c1, c2, c3):
    x = c1 * np.exp(-5 * t)
    y = c2 * np.exp(-4 * t) + c3 * np.exp(3 * t)
    z = c2 * np.exp(-4 * t) - c3 * np.exp(3 * t)
    return x, y, z

# %%
# Condições iniciais
c1 = 4
c2 = 5
c3 = 6

# Intervalo de tempo
t = np.linspace(0, 10, 100)

# Calculando as soluções analíticas
x, y, z = solucao_analitica2(t, c1, c2, c3)

# %%
# Plotando os resultados
plt.plot(t, x, label='x(t)')
plt.plot(t, y, label='y(t)')
plt.plot(t, z, label='z(t)')
plt.xlabel('Tempo')
plt.ylabel('Valor')
plt.legend()
plt.grid(True)
plt.show()