import random

def generador():
    a = random.randint(10000,999999999)
    return a

def numEnChino (a):
    resultado = ""
    if a >= 10000000:
        resultado = str(int(a/10000000)); "千" , queNumEs(int(a/10000000))
        a = a%10000000
        resultado = resultado, str(int(a/1000000)), "百" , queNumEs(int(a/1000000))
        a = a%1000000
        resultado = resultado, str(int(a/100000)), "十" , queNumEs(int(a/100000))
        a = a%100000
        resultado = resultado, str(int(a/10000)), "万" , queNumEs(int(a/10000))


    elif a > 1000000:
        resultado = resultado, str(int(a/1000000)), "百" , queNumEs(int(a/1000000))
        a = a%1000000
        resultado = resultado, str(int(a/100000)), "十" , queNumEs(int(a/100000))
        a = a%100000
        resultado = resultado, str(int(a/10000)), "万" , queNumEs(int(a/10000))
        
    elif a > 100000:
        resultado = resultado, str(int(a/100000)), "十" , queNumEs(int(a/100000))
        a = a%100000
        resultado = resultado, str(int(a/10000)), "万" , queNumEs(int(a/10000))
    else:
        resultado = resultado, str(int(a/10000)), "万" , queNumEs(int(a/10000))

    return resultado


def queNumEs (numA):
    x = 1
    contador = 0
    numerosChino = ["零","一","二","三","四","五","六","七","八","九"]
    while x != 0 or contador > 11 :
        for i in numerosChino:
            if numA == i:
                x = 0
                return numerosChino[i]
        contador += 1

print(numEnChino(generador()))