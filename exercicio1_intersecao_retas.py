# Exercício 1 #
# Considere duas retas em um plano xy. Fazer um programa para encontrar o ponto
# de interseçao Pi = (xi,yi) entre elas. Supor que as duas retas não são paralalelas.
# Reta 1: definida pelos pontos P1 = (x1,y1) e P2 = (x2,y2)
# Reta 2: definida pelis pontos P3 = (x3,y3) e P4 = (x4,y4)

# Recebe informações dos pontos da reta 1

#ponto 1 da reta 1
reta1_p1 = input('RETA 1 (1º PONTO) - Insira a coordenada P1=(x1,y1) da reta 1: ')
x1, y1 = reta1_p1.split(",")
x1 = float(x1)
y1 = float(y1)

#ponto 2 da reta 1
reta1_p2 = input('RETA 1 (2º PONTO) - Insira a coordenada P2=(x2,y2) da reta 1: ')
x2, y2 = reta1_p2.split(",")
x2 = float(x2)
y2 = float(y2)

# Recebe iformações dos pontos da reta 2

#ponto 1 da reta 2
reta2_p1 = input('RETA 2 (1º PONTO) - Insira a coordenada P3=(x3,y3) da reta 2: ')
x3, y3 = reta2_p1.split(",")
x3 = float(x3)
y3 = float(y3)

#ponto 2 da reta 2
reta2_p2 = input('RETA 2 (2º PONTO) - Insira a coordenada P4=(x4,y4) da reta 2: ')
x4, y4 = reta2_p2.split(",")
x4 = float(x4)
y4 = float(y4)

# Cálculo da inclinação das retas
m1 = (y2-y1) / (x2-x1) #reta 1
m2 = (y4-y3) / (x4-x3) #reta 2

# Verificando se as retas são paralelas
if m1 == m2:
    print('As retas são paralelas e, portanto, não possuem ponto de interseção.')
else:
    # Cálculo das constantes de inclinação
    b1 = y1 - m1*x1
    b2 = y3 - m2*x3

    # Cálculo do ponto de interseção
    xi = round((b2 - b1) / (m1 - m2),2)
    yi = round((m1*xi + b1),2)
    pi = (xi,yi)

    print(pi)

# Plotagem do gráfico #

    import matplotlib.pyplot as plt

    # Define as coordenadas das retas
    x1_vals = [x1, x2]
    y1_vals = [y1, y2]

    x2_vals = [x3, x4]
    y2_vals = [y3, y4]

    # Plota as retas
    plt.plot(x1_vals, y1_vals, label="Reta 1", color="gray")
    plt.plot(x2_vals, y2_vals, label="Reta 2", color="blue")

    # Plota o ponto de interseção
    plt.scatter(xi, yi, color="red", label="Ponto de interseção")

    # Define os rótulos dos eixos e o título do gráfico
    plt.xlabel("Eixo x")
    plt.ylabel("Eixo y")
    plt.title("Interseção de retas")

    # Adiciona a legenda
    plt.legend()

    # Exibe o gráfico
    plt.show()
