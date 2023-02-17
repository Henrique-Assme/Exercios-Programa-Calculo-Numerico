# Arthur Milani Giovanini e Henrique de Andrade Assme

from math import *
import numpy as np
import matplotlib.pyplot as plt

#Parâmetros iniciais
t0 = 0.0 #t0 instante inicial
tf = 50.0 #T instante final
n_lista = [] #qntd de pontos

y1_0 = 20 #y1(t0) = 1
y2_0 = 20 #y2(t0) = 0

def f1(y1,y2,t): # f tq dy/dt = f(t,t)
    return 1*y1-0.02*y1*y2 # dy1/dt = y1 - y1y2

def f2(y1,y2,t):
    return -0.25*y2+0.02*y1*y2 # dy2/dt = -y2 + y1y2

# Main executa o método e faz os gráficos

def main():
    
    h_lista = []
    t_lista = []
    y1_lista = []
    y2_lista = []
    erro_lista = []
    m=3

    for j in range(1,m+1):
        n=512*2**(j-1)
        n_lista.append(n)
        h = (tf-t0)/float(n)

        #executa o método
        y1 = np.zeros(n+1)
        y2 = np.zeros(n+1)
        t = np.zeros(n+1)

        y1[0] = y1_0
        y2[0] = y2_0
        t[0] = t0

        for i in range (0,n):
            t[i+1] = t[i] + h

            y1_raiz = y1[i] #chute inicial é sempre o valor anteriormente calculado
            y2_raiz = y2[i]
            r = 0
            #print("Começo da iteração")
            #print("r y_raiz erro")
            while r<3: #faz 20 vezes o ponto fixo ou o erro fica menor que 1E-10
                y1_aux = y1_raiz
                y1_raiz = y1[i] + h*f1(y1_raiz,y2_raiz, t[i+1])
                y2_raiz = y2[i] + h*f2(y1_aux,y2_raiz, t[i+1])
                r += 1
            
            y1[i+1] = y1_raiz
            y2[i+1] = y2_raiz

        t_lista.append(t) #coloca os valores de tempo numa lista
        y1_lista.append(y1) #coloca os valores de y numa lista
        y2_lista.append(y2) #coloca os valores de y numa lista
        h_lista.append(h)

    erro_lista.append(0)
    for i in range(1,m+1):
            e_1=e_2=p=r=0 #parametros da tabela de convergência
            if i>1:
                r = h_lista[i-2]/h_lista[i-1] #razão usada para dividir o delta t (tem que ser 2 nesse caso)

                e_1 = -1*(y1_lista[i-1][-1]-y1_lista[i-2][-1])/(2**1-1) #erro global deve tender à 0

                e_2 = -1*(y2_lista[i-1][-1]-y2_lista[i-2][-1])/(2**1-1) #erro global deve tender à 0

                e_t = sqrt(e_1*e_1 + e_2*e_2)
                
                erro_lista.append(e_t)
                if i > 2:
                    q = erro_lista[i-2]/erro_lista[i-1]

                    p = log(q)/log(r)
                
            print("%5d & %9.3e & %9.3e & %9.3e \\\\" % (i-1,h_lista[i-1], erro_lista[i-1], p))

    #gráficos
    for w in range(len(n_lista)):
        t = t_lista[w]
        y1 = y1_lista[w]
        y2 = y2_lista[w]
        if w==0:
            plt.plot(t, y1, label="n=%d"%n_lista[w]+", Presa", linestyle=":", color="black")
            plt.plot(t, y2, label="n=%d"%n_lista[w]+", Predador", linestyle=":", color="black")
        if w==1:
            plt.plot(t, y1, label="n=%d"%n_lista[w]+", Presa", linestyle="--", color="black")
            plt.plot(t, y2, label="n=%d"%n_lista[w]+", Predador", linestyle="--", color="black")
        if w==2:
            plt.plot(t, y1, label="n=%d"%n_lista[w]+", Presa", linestyle="-.", color="black")
            plt.plot(t, y2, label="n=%d"%n_lista[w]+", Predador", linestyle="-.", color="black")

    plt.title('Aprox para função 1 por Euler Implícito')
    plt.xlabel('t[i]')
    plt.ylabel('y1[i]')
    plt.grid(True)
    plt.legend()
    plt.show()

    #gráficos
    for w in range(len(n_lista)):
        t = t_lista[w]
        y1 = y1_lista[w]
        y2 = y2_lista[w]
        if w==0:
            plt.plot(t, y1, label="n=%d"%n_lista[w]+", Presa", linestyle=":", color="black")
            plt.plot(t, y2, label="n=%d"%n_lista[w]+", Predador", linestyle=":", color="black")
        if w==1:
            plt.plot(t, y1, label="n=%d"%n_lista[w]+", Presa", linestyle="--", color="black")
            plt.plot(t, y2, label="n=%d"%n_lista[w]+", Predador", linestyle="--", color="black")
        if w==2:
            plt.plot(t, y1, label="n=%d"%n_lista[w]+", Presa", linestyle="-.", color="black")
            plt.plot(t, y2, label="n=%d"%n_lista[w]+", Predador", linestyle="-.", color="black")

    plt.title('Aprox para função 1 por Euler Implícito')
    plt.xlabel('t[i]')
    plt.ylabel('y1[i]')
    plt.grid(True)
    plt.legend()
    plt.show()
    
main()