from functions import *

print("Calculadora circuitos RCL")

Voltaje = float(input("Digite o valor del Voltaje: "))
Desface = float(input("Digite o valor de desface: "))
Si_Frecuencia = input("Se tiene la frecuencia? (S/N): ")
if Si_Frecuencia == "S":
    Frecuencia = float(input("Digite el valor de la frecuencia: "))
    Frecuencia_Angular = 0
else:
    Frecuencia_Angular = float(input("Digite el valor de la frecuencia angular: "))
    Frecuencia = 0
Resistencia = float(input("Digite el valor de la resistencia: "))
Capacitancia = float(input("Digite el valor de la capacitancia: "))
Inductancia = float(input("Digite el valor de la inductancia: "))
Es_Serie = input("Es un circuito serie? (S/N): ")
Impedancia_Inductiva = Obtain_Xl(Frecuencia, Inductancia, Frecuencia_Angular, Si_Frecuencia)
print("La impedancia inductiva es: ", Impedancia_Inductiva)
Impedancia_Capacitiva = Obtain_Xc(Frecuencia, Capacitancia, Frecuencia_Angular, Si_Frecuencia)
print("La impedancia capacitiva es: ", Impedancia_Capacitiva)
Impedancia_Total = Obtain_Z(Impedancia_Inductiva, Impedancia_Capacitiva, Es_Serie, Resistencia)
print("La impedancia total es: ", Impedancia_Total)
Angulo = Obtain_Angulo(Impedancia_Inductiva, Impedancia_Capacitiva, Es_Serie, Resistencia)
print("El angulo es: ", Angulo)
Corriente_Total = Obtain_I(Voltaje, Impedancia_Total)
print("La corriente total es: ", Corriente_Total)
if Es_Serie == "N":
    Corriente_Resistencia = Ontain_Ir(Voltaje, Resistencia)
    print("La corriente en la resistencia es: ", Corriente_Resistencia)
    Corriente_Capacitiva = Obtain_Ic(Voltaje, Impedancia_Capacitiva)
    print("La corriente en el capacitor es: ", Corriente_Capacitiva)
    Corriente_Inductiva = Obtain_Il(Voltaje, Impedancia_Inductiva)
    print("La corriente en la bobina es: ", Corriente_Inductiva)
Factor_Potencia = Obtain_Factor_Potencia(Desface, Angulo)
print("El factor de potencia es: ", Factor_Potencia)
print("Programa finalizado")
print("Programa creado por Ricardo Gonzalez")
input("Presione enter para cerrar el programa")