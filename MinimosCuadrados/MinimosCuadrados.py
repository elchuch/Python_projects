#Programa de minimos cuadrados(Metodos Numericos
import math
#Se ingresa la cantidad de pares ordenados(x,y)
print(f"Metodo de minimos cuadrados,para aproximar una recta\nde la forma y = mx+b")
print("\n\n")
def Min(n):
    puntosX=[]
    puntosY=[]
    sx=0
    sy=0;
    sxy=0
    sxx=0
    syy=0
    r=0
    m=0
    b=0
    for i in range(n):
   
        EntradaX = float(input(f"Ingresar el valor de  x{i}: "))
  
        puntosX.append(EntradaX)
        sx+=EntradaX
        sxx+=math.pow(EntradaX,2)
        EntradaY = float(input(f"Ingresar el valor de y{i}: "))
        puntosY.append(EntradaY)
        sy+=EntradaY
        syy+=math.pow(EntradaY,2)
        sxy+=(EntradaX*EntradaY)
    r=(n*sxy-sx*sy)/((math.sqrt(n*sxx-sx*sx))*(math.sqrt(n*syy-sy*sy)))
    m=(n*sxy-sx*sy)/(n*sxx-sx*sx)
    b=(sy*sxx-sx*sxy)/(n*sxx-sx*sx)
    imprime(r,m,b,puntosX,puntosY)
    puntosX.clear()
    puntosY.clear()

def imprime(r,m,b,puntosX,puntosY):
    print("\n\n")
    print("{:<10} {:<10} {:<10}".format('r','m','b',))
    print("{:<10} {:<10} {:<10}".format(r,m,b))
    print(f"ecuacion de la recta\n")
    print(f"y={m}x+{b}")
    print("\n")
    print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format('i','X','Y','X^2','Y^2','X*Y'))
    for i in range(n):
         imprimirX=puntosX[i]
         imprimirY=puntosY[i]
         print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(i,imprimirX,imprimirY,math.pow(imprimirX,2),math.pow(imprimirY,2),imprimirY*imprimirX))



n = int(input("ingresar datos: "))
Min(n)
r=input("desea ingresar otra iteracion: ")
while r!='n' or r=='N':
    n = int(input("ingresar datos: "))
    
    Min(n)
   
    r=input("desea ingresar otra iteracion: ")







