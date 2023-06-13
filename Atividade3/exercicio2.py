# Resolva numericamente (por Euler e Runge-Kutta de alta ordem) os sistemas dinâmicos
# do exercício 1. Construir um gráfico comparando as soluções analíticas e numéricas
# em cada caso.

# %%
# Resolvendo o primeiro sistema fornecido em 1.a pelo método de Euler

import numpy as np
import matplotlib.pyplot as plt

# %%
def euler_method(f, x0, y0, t0, tmax, h):
    """
    Implementação do método de Euler para resolver um sistema dinâmico de duas equações diferenciais de primeira ordem.
    
    Args:
        f: Função que define o sistema dinâmico. Deve receber as variáveis independentes (t, x, y) e retornar
           as derivadas dx/dt e dy/dt em forma de uma tupla (dxdt, dydt).
        x0, y0: Valores iniciais para x e y.
        t0: Valor inicial para a variável independente t.
        tmax: Valor máximo para a variável independente t.
        h: Tamanho do passo.
    
    Returns:
        Um array numpy com os valores de t, x e y ao longo do intervalo [t0, tmax].
    """
    num_steps = int((tmax - t0) / h) + 1
    t = np.linspace(t0, tmax, num_steps)
    x = np.zeros(num_steps)
    y = np.zeros(num_steps)
    
    x[0] = x0
    y[0] = y0
    
    for i in range(1, num_steps):
        dxdt, dydt = f(t[i-1], x[i-1], y[i-1])
        x[i] = x[i-1] + h * dxdt
        y[i] = y[i-1] + h * dydt
    
    return np.array([t, x, y])

# %%
def system_dynamics(t, x, y):
    """
    Função que define as equações diferenciais do sistema dinâmico.
    
    Args:
        t: Variável independente (tempo).
        x, y: Variáveis dependentes.
    
    Returns:
        Uma tupla (dxdt, dydt) com as derivadas dx/dt e dy/dt.
    """
    dxdt = -3 * x + y
    dydt = x - 3 * y
    return dxdt, dydt

# %%
# Condições iniciais
x0 = 2
y0 = 3

# Intervalo de tempo
t0 = 0
tmax = 10

# Tamanho do passo
h = 0.001

# Resolvendo o sistema dinâmico usando o método de Euler
solution = euler_method(system_dynamics, x0, y0, t0, tmax, h)

# %%
# Extraindo os resultados
t_values = solution[0]
x_values = solution[1]
y_values = solution[2]

# Imprimindo os resultados
for t, x, y in zip(t_values, x_values, y_values):
    print(f"t = {t:.3f}, x = {x:.6f}, y = {y:.6f}")

# %%
# Plotando gráfico
# Plotando os resultados
plt.plot(t_values, x_values, label='Solução Numérica - x(t)')
plt.plot(t_values, y_values, label='Solução Numérica - y(t)')
plt.xlabel('Tempo')
plt.ylabel('Valor')
plt.legend()
plt.grid(True)
plt.show()



#%%
# RESOLVENDO PELO MÉTODO Runge-Kutta de alta ordem
def derivative(t, x, y):
    dxdt = -3 * x + y
    dydt = x - 3 * y
    return dxdt, dydt
#%%
def runge_kutta_method(f, x0, y0, t0, tmax, h):
    num_steps = int((tmax - t0) / h) + 1
    t = np.linspace(t0, tmax, num_steps)
    x = np.zeros(num_steps)
    y = np.zeros(num_steps)

    x[0] = x0
    y[0] = y0

    for i in range(1, num_steps):
        k1x, k1y = f(t[i-1], x[i-1], y[i-1])
        k2x, k2y = f(t[i-1] + h/2, x[i-1] + h/2 * k1x, y[i-1] + h/2 * k1y)
        k3x, k3y = f(t[i-1] + h/2, x[i-1] + h/2 * k2x, y[i-1] + h/2 * k2y)
        k4x, k4y = f(t[i-1] + h, x[i-1] + h * k3x, y[i-1] + h * k3y)

        x[i] = x[i-1] + h/6 * (k1x + 2*k2x + 2*k3x + k4x)
        y[i] = y[i-1] + h/6 * (k1y + 2*k2y + 2*k3y + k4y)

    return np.array([t, x, y])
#%%
x0 = 2
y0 = 3
t0 = 0
tmax = 10
h = 0.001

solution = runge_kutta_method(derivative, x0, y0, t0, tmax, h)

t_values = solution[0]
x_values = solution[1]
y_values = solution[2]

for t, x, y in zip(t_values, x_values, y_values):
    print(f"t = {t:.3f}, x = {x:.6f}, y = {y:.6f}")
#%%
plt.plot(t_values, x_values, label='Solução Numérica - x(t)')
plt.plot(t_values, y_values, label='Solução Numérica - y(t)')
plt.xlabel('Tempo')
plt.ylabel('Valor')
plt.legend()
plt.grid(True)
plt.show()

#%%
# CALCULANDO O ERRO ENTRE OS MÉTODOS E SOLUCAO ANALITICA
def analytical_solution(t):
    x = np.exp(-2*t) * (2*np.cos(t) + np.sin(t))
    y = -np.exp(-2*t) * (np.cos(t) + 2*np.sin(t))
    return x, y
#%%
# Calculando a solução analítica
x_analytical, y_analytical = analytical_solution(t_values)

# Calculando o erro para o método de Euler
error_euler_x = np.abs(x_values - x_analytical)
error_euler_y = np.abs(y_values - y_analytical)

# Calculando o erro para o método de Runge-Kutta
error_rk_x = np.abs(x_values - x_analytical)
error_rk_y = np.abs(y_values - y_analytical)

# Imprimindo os erros
for t, error_x, error_y in zip(t_values, error_euler_x, error_euler_y):
    print(f"t = {t:.3f}, erro_x (Euler) = {error_x:.6f}, erro_y (Euler) = {error_y:.6f}")

for t, error_x, error_y in zip(t_values, error_rk_x, error_rk_y):
    print(f"t = {t:.3f}, erro_x (Runge-Kutta) = {error_x:.6f}, erro_y (Runge-Kutta) = {error_y:.6f}")

#%% plot dos erros
plt.figure()

# Gráfico de erro para o método de Euler
plt.subplot(2, 1, 1)
plt.plot(t_values, error_euler_x, label='Erro x(t) - Euler')
plt.plot(t_values, error_euler_y, label='Erro y(t) - Euler')
plt.xlabel('Tempo')
plt.ylabel('Erro')
plt.legend()
plt.grid(True)

# Gráfico de erro para o método de Runge-Kutta
plt.subplot(2, 1, 2)
plt.plot(t_values, error_rk_x, label='Erro x(t) - Runge-Kutta')
plt.plot(t_values, error_rk_y, label='Erro y(t) - Runge-Kutta')
plt.xlabel('Tempo')
plt.ylabel('Erro')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

