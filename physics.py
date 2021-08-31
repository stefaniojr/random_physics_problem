
import numpy as physics_problem # importando a lib numpy

#
#
#
# Declaração de variáveis
a = float(-9.81) # assumindo condições de arremesso vertical na terra
v = float(0) # velocidade em hmax
#Um lançador arremessa uma bola de beisebol para cima, ao longo do eixo y vertical, com uma velocidade inicial de 12 m/s.
#a) Quanto tempo a bola leva para atingir a altura máxima?
print("Questão extra:")
print("Um lançador arremessa uma bola de beisebol para cima, ao longo do eixo y vertical, com uma velocidade inicial de 12 m/s")
def linha():
   print(" ___________________________________________________________________________________________________________ ")
linha()
#agora vamos à letra A
print("a) Quanto tempo a bola leva para atingir a altura máxima?")

while True:
  vo=float(input('Insira o valor da velocidade inicial vo: '))

  if vo <= 0:
    print('A velocidade precisa ser maior que 0')
    continue
  else:
    break

tempo=(v-vo)/a
tempo = round(tempo, 3) # aproxima para 3 casas decimais
print('O tempo que a bola leva para atingir a altura máxima é de', tempo,'segundos')

#agora vamos pro proximo tópico pedido: altura maxima, que ja com os dados armazenados pode ser encontrada.
linha()
print("b) Qual é a altura máxima (y) alcançada pela bola em relação ao ponto de lançamento?")

y=((v ** 2)-(vo ** 2))/(2*a)
y=round(y, 3)
print('A altura máxima y que a bola atinge é de', y,'metros')
#por fim encontraremos os valores de tempo na altura 5m
linha()
print("c) Quanto tempo a bola leva para atingir um ponto deltaY (m) acima do ponto inicial?")
deltaY=float(input('Insira o valor de deltaY: '))
#responderemos a questão através da formula y=vo*t-1/2*gt^2

#-(a/2)*t^2 - vo*t + deltaY = 0

t = [(-a/2), -vo, deltaY] # coeficientes do polinômio quadrático (ax^2 + bx + c = 0) --> ((-a/2)t^2 - vo*t + deltaY = 0)
t = physics_problem.roots(t) # extrai raizes do polinômio com os coeficientes indicados em t
t = physics_problem.round(t, 3) # aproxima pra 3 casas decimais
print(t) # imprime na tela o vetor t, cujo valores são os pontos de interseção com o eixo t