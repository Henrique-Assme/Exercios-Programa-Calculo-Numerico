# Arthur Milani Giovanini e Henrique de Andrade Assme

from math import *
import numpy as np
import matplotlib.pyplot as plt

#Parâmetros iniciais
t0 = 0.0 #t0 instante inicial
tf = 2.0 #T instante final
n_lista = [100, 140, 200] #qntd de pontos

y0 = 1.0 #y(t0) = 1

def f(t,y): # f tq dy/dt = f(t,t)
    return 2*t*y

def solucao(t):
    return exp(t**2)

# Main executa o método e faz os gráficos

def main():
    
    t_lista = []
    y_lista = []
    erro_global_lista = []
    sol_exata_lista = []

    for n in n_lista:
        h = (tf-t0)/float(n)

        #executa o método

        y = np.zeros(n+1)
        t = np.zeros(n+1)

        y[0] = y0
        t[0] = t0

        for i in range (0,n):
            t[i+1] = t[i] + h

            y_raiz = y[i] #chute inicial é sempre o valor anterior calculado
            erro = 1
            r = 0
            #print("Começo da iteração")
            #print("r y_raiz erro")
            while r<20 and erro > 0.0000000001:
                y_aux = y_raiz
                y_raiz = y[i] + h*f(y_raiz, t[i+1])
                erro = np.absolute(y_raiz - y_aux)
                r += 1
                #print (r, y_raiz, erro)
            
            y[i+1] = y_raiz

        t_lista.append(t)
        y_lista.append(y)
        erro_global_lista.append( np.absolute(y[n] - solucao(tf)))
    for k in range(len(t)):
        sol_exata_lista.append(solucao(t[k]))

    #gráficos
    for w in range(len(n_lista)):
        t = t_lista[w]
        y = y_lista[w]

        plt.plot(t, y, label="n=%d"%n_lista[w])
        
    plt.plot(t, sol_exata_lista, label="exata")
    plt.title('Aprox para função por Euler Implícito')
    plt.xlabel('t[i]')
    plt.ylabel('y[i]')
    plt.grid(True)
    plt.legend()
    plt.show()

main()