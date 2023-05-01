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