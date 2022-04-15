import random
from traceback import format_exception

def numEnChino (a):
    numerosChino = ('零','一','二','三','四','五','六','七','八','九','九')
    resultado = ""
    if a >= 10000000:
        resultado = str(numerosChino[int(a/10000000)]) + '千'
        a = a%10000000
        resultado = resultado + str(numerosChino[int(a/1000000)]) + '百'
        a = a%1000000
        resultado = resultado + str(numerosChino[int(a/100000)]) + '十' 
        a = a%100000
        resultado = resultado + str(numerosChino[int(a/10000)]) + '万'
        a = a%10000
        resultado = resultado + str(numerosChino[int(a/1000)]) + '千'
        a = a%1000
        resultado = resultado + str(numerosChino[int(a/100)]) + '百'
        a = a%100
        resultado = resultado + str(numerosChino[int(a/10)]) + '十'
        a = a%10
        resultado = resultado + str(numerosChino[int(a/1)]) + '个'
    elif a >= 1000000:
        resultado = resultado + str(numerosChino[int(a/1000000)]) + '百'
        a = a%1000000
        resultado = resultado + str(numerosChino[int(a/100000)]) + '十' 
        a = a%100000
        resultado = resultado + str(numerosChino[int(a/10000)]) + '万'
        a = a%10000
        resultado = resultado + str(numerosChino[int(a/1000)]) + '千'
        a = a%1000
        resultado = resultado + str(numerosChino[int(a/100)]) + '百'
        a = a%100
        resultado = resultado + str(numerosChino[int(a/10)]) + '十'
        a = a%10
        resultado = resultado + str(numerosChino[int(a/1)]) + '个'
        
    elif a >= 100000:
        resultado = resultado + str(numerosChino[int(a/100000)]) + '十' 
        a = a%100000
        resultado = resultado + str(numerosChino[int(a/10000)]) + '万'
        a = a%10000
        resultado = resultado + str(numerosChino[int(a/1000)]) + '千'
        a = a%1000
        resultado = resultado + str(numerosChino[int(a/100)]) + '百'
        a = a%100
        resultado = resultado + str(numerosChino[int(a/10)]) + '十'
        a = a%10
        resultado = resultado + str(numerosChino[int(a/1)]) + '个'
    elif a >= 10000:
        resultado = resultado + str(numerosChino[int(a/10000)]) + '万'
        a = a%10000
        resultado = resultado + str(numerosChino[int(a/1000)]) + '千'
        a = a%1000
        resultado = resultado + str(numerosChino[int(a/100)]) + '百'
        a = a%100
        resultado = resultado + str(numerosChino[int(a/10)]) + '十'
        a = a%10
        resultado = resultado + str(numerosChino[int(a/1)]) + '个'
    elif a >= 1000:
        resultado = resultado + str(numerosChino[int(a/1000)]) + '千'
        a = a%1000
        resultado = resultado + str(numerosChino[int(a/100)]) + '百'
        a = a%100
        resultado = resultado + str(numerosChino[int(a/10)]) + '十'
        a = a%10
        resultado = resultado + str(numerosChino[int(a/1)]) + '个'
    elif a >= 100:
        resultado = resultado + str(numerosChino[int(a/100)]) + '百'
        a = a%100
        resultado = resultado + str(numerosChino[int(a/10)]) + '十'
        a = a%10
        resultado = resultado + str(numerosChino[int(a/1)]) + '个'
    elif a >= 10:
        resultado = resultado + str(numerosChino[int(a/10)]) + '十'
        a = a%10
        resultado = resultado + str(numerosChino[int(a/1)]) + '个'    
    else:
        resultado = resultado + str(numerosChino[int(a/1)]) + '个'


    return resultado

print("Escriba un número mayor o igual que 0 y menor que 100000000")
x = 1
while(x!=0):
    try:
        a = int(input("Ingrese el valor\n"))
        if a >= 0 and a < 100000000:
            x = 0
        else:
            raise format_exception
    except:
        print("Escirba un número válido pendejooooo")
print(numEnChino(a))