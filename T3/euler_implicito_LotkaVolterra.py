# Arthur Milani Giovanini e Henrique de Andrade Assme

from math import *
import numpy as np
import matplotlib.pyplot as plt

#Parâmetros iniciais
t0 = 0.0 #t0 instante inicial
tf = 20.0 #T instante final
n_lista = [] #qntd de pontos

y1_0 = 20 
y2_0 = 20 

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
    m=6

    # "For" reponsável por cada gráfico
    for j in range(1,m+1):
        n=512*8**(j-1)
        n_lista.append(n)
        h = (tf-t0)/float(n)

        #executa o método
        y1 = np.zeros(n+1)
        y2 = np.zeros(n+1)
        t = np.zeros(n+1)

        y1[0] = y1_0
        y2[0] = y2_0
        t[0] = t0

        # "For" responsável pela obtenção de cada ponto de um determinado gráfico
        for i in range (0,n):
            t[i+1] = t[i] + h

            # Chute inicial é sempre o valor anteriormente calculado
            y1_raiz = y1[i]
            y2_raiz = y2[i]
            r = 0

            # Implementação do Euler Implícito
            while r<3:
                y1_aux = y1_raiz
                y1_raiz = y1[i] + h*f1(y1_raiz,y2_raiz, t[i+1])
                y2_raiz = y2[i] + h*f2(y1_aux,y2_raiz, t[i+1])
                r += 1
            
            # Valores finais obtidos para cada ponto
            y1[i+1] = y1_raiz
            y2[i+1] = y2_raiz

        t_lista.append(t)   # Coloca os valores de tempo numa lista
        y1_lista.append(y1) # Coloca os valores de y1 numa lista
        y2_lista.append(y2) # Coloca os valores de y2 numa lista
        h_lista.append(h)

    erro_lista.append(0)    # Primeiro erro é 0
    #Construção da tabela de convergência
    for i in range(1,m+1):
            e_1=e_2=p=r=0 # Parametros da tabela de convergência
            if i>1:
                r = h_lista[i-2]/h_lista[i-1] #razão usada para dividir o delta t (tem que ser 2 nesse caso)

                e_1 = -1*(y1_lista[i-1][-1]-y1_lista[i-2][-1])/(8**1-1) #erro global deve tender à 0

                e_2 = -1*(y2_lista[i-1][-1]-y2_lista[i-2][-1])/(8**1-1) #erro global deve tender à 0

                e_t = sqrt(e_1*e_1 + e_2*e_2)
                
                erro_lista.append(e_t)
                if i > 2:
                    q = erro_lista[i-2]/erro_lista[i-1]

                    p = log(q)/log(r)
                
            print("%5d & %9.3e & %9.3e & %9.3e \\\\" % (n_lista[i-1],h_lista[i-1], erro_lista[i-1], p))

    # Implementação gráfica
    for w in range(len(n_lista)):
        t = t_lista[w]
        y1 = y1_lista[w]
        y2 = y2_lista[w]
        if w==len(n_lista)-1:
            plt.plot(t, y1, label="n=%d"%n_lista[w]+", Presa", linestyle=":", color="black")
            plt.plot(t, y2, label="n=%d"%n_lista[w]+", Predador", linestyle="-.", color="black")

    plt.suptitle('Aproximação numérica para o problema presa-predador')
    plt.title('Gráfico de presa e predador para o último n calculado')
    plt.xlabel('tempo')
    plt.ylabel('População')
    plt.grid(True)
    plt.legend()
    plt.show()

    # Implementação gráfica
    for w in range(len(n_lista)):
        t = t_lista[w]
        y1 = y1_lista[w]
        if  w==0:
            plt.plot(t, y1, label="n=%d"%n_lista[w], linestyle=":", color="black")
        if  w==2:
            plt.plot(t, y1, label="n=%d"%n_lista[w], linestyle="--", color="black")
        if  w==5:
            plt.plot(t, y1, label="n=%d"%n_lista[w], linestyle="-.", color="black")

    plt.suptitle('Aproximação numérica para o problema presa-predador')
    plt.title('Gráfico da presa para 3 valores de n')
    plt.xlabel('tempo')
    plt.ylabel('População')
    plt.grid(True)
    plt.legend()
    plt.show()

    # Implementação gráfica
    for w in range(len(n_lista)):
        t = t_lista[w]
        y2 = y2_lista[w]
        if w==0:
            plt.plot(t, y2, label="n=%d"%n_lista[w], linestyle=":", color="black")
        if w==2:
            plt.plot(t, y2, label="n=%d"%n_lista[w], linestyle="--", color="black")
        if w==5:
            plt.plot(t, y2, label="n=%d"%n_lista[w], linestyle="-.", color="black")

    plt.suptitle('Aproximação numérica para o problema presa-predador')
    plt.title('Gráfico do predador para 3 valores de n')
    plt.xlabel('tempo')
    plt.ylabel('População')
    plt.grid(True)
    plt.legend()
    plt.show()
    
main()