# Arthur Milani Giovanini e Henrique de Andrade Assme

from math import *
import numpy as np
import matplotlib.pyplot as plt

#Parâmetros iniciais
t0 = 0.0 #t0 instante inicial
tf = 3.0 #T instante final
n_lista = [] #qntd de pontos

y1_0 = 1 #y1(t0) = 1
y2_0 = 0 #y2(t0) = 0

def f1(y,t): # f tq dy/dt = f(t,t)
    return -sin(t) # dy/dt = -sin(t)

def f2(y,t):
    return cos(t) # dy/dt = cos(t)

def solucao1(t):
    return cos(t) #ye1(t) = cos(t)

def solucao2(t):
    return sin(t) #ye2(t) = sin(t)

# Main executa o método e faz os gráficos

def main():
    
    h_lista = []
    t_lista = []
    y1_lista = []
    y2_lista = []
    sol_exata1_lista = []
    sol_exata2_lista = []
    m=5

    for j in range(1,m+1):
        n=16*2**(j-1)
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
            while r<5: #faz 20 vezes o ponto fixo ou o erro fica menor que 1E-10
                y1_raiz = y1[i] + h*f1(y1_raiz, t[i+1])
                y2_raiz = y2[i] + h*f2(y2_raiz, t[i+1])
                r += 1
            
            y1[i+1] = y1_raiz
            y2[i+1] = y2_raiz

        t_lista.append(t) #coloca os valores de tempo numa lista
        y1_lista.append(y1) #coloca os valores de y numa lista
        y2_lista.append(y2) #coloca os valores de y numa lista
        h_lista.append(h)

    for k in range(len(t)):
        sol_exata1_lista.append(solucao1(t[k])) #coloca os valores da solução exata numa lista
    
    for k in range(len(t)):
        sol_exata2_lista.append(solucao2(t[k])) #coloca os valores da solução exata numa lista


    for i in range(1,m+1):
            e_1=e_2=q_1=q_2=p=r=e_t=0 #parametros da tabela de convergência
            if i>1:
                q_1 = abs((solucao1(tf)-y1_lista[i-2][-1])/(solucao1(tf)-y1_lista[i-1][-1])) #razão entre os erros globais

                q_2 = abs((solucao2(tf)-y2_lista[i-2][-1])/(solucao2(tf)-y2_lista[i-1][-1])) #razão entre os erros globais
                
                r = h_lista[i-2]/h_lista[i-1] #razão usada para dividir o delta t (tem que ser 2 nesse caso)

                e_1 = abs(solucao1(tf)-y1_lista[i-1][-1]) #erro global deve tender à 0

                e_2 = abs(solucao2(tf)-y2_lista[i-1][-1]) #erro global deve tender à 0

                e_t = sqrt(e_1*e_1 + e_2*e_2)

                if(max(e_1, e_2) == e_1):
                    p = log(q_1)/log(r)#deve tender à 1
                else:
                    p = log(q_2)/log(r)#deve tender à 1
                
            print("%5d & %9.3e & %9.3e & %9.3e \\\\" % (n_lista[i-1],h_lista[i-1],e_t,p))

    #gráficos
    for w in range(len(n_lista)):
        t = t_lista[w]
        y = y1_lista[w]

        if w==0 or w==3:
            plt.plot(t, y, label="n=%d"%n_lista[w], linestyle=":", color="black")
        if w==1 or w==4:
            plt.plot(t, y, label="n=%d"%n_lista[w], linestyle="--", color="black")
        if w==2:
            plt.plot(t, y, label="n=%d"%n_lista[w], linestyle="-.", color="black") 
        
    plt.plot(t, sol_exata1_lista, label="exata", color="black")
    plt.title('Aproximação para cos(t)')
    plt.xlabel('t',fontsize=12)
    plt.ylabel('y(t) = cos(t)',fontsize=12)
    plt.grid(True)
    plt.legend()
    plt.show()

    #gráficos
    for w in range(len(n_lista)):
        t = t_lista[w]
        y = y2_lista[w]

        if w==0 or w==3:
            plt.plot(t, y, label="n=%d"%n_lista[w], linestyle=":", color="black")
        if w==1 or w==4:
            plt.plot(t, y, label="n=%d"%n_lista[w], linestyle="--", color="black")
        if w==2:
            plt.plot(t, y, label="n=%d"%n_lista[w], linestyle="-.", color="black")
        
    plt.plot(t, sol_exata2_lista, label="exata",color="black")
    plt.title('Aproximação para a função sen(t)')
    plt.xlabel('t',fontsize=12)
    plt.ylabel('y(t) = sen(t)',fontsize=12)
    plt.grid(True)
    plt.legend()
    plt.show()


main()