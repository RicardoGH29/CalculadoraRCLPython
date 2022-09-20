import math


# Inverso
def Obtain_Inverso(n):
    return 1 / n


# Obtencion de impedancias
def Obtain_Xl(frecuencia, inductancia, frecuencia_angular, Si_Frecuencia):
    if Si_Frecuencia == "S":
        return 2 * math.pi * frecuencia * inductancia
    else:
        return frecuencia_angular * inductancia


def Obtain_Xc(frecuencia, capacitancia, frecuencia_angular, Si_Frecuencia):
    if Si_Frecuencia == "S":
        return 1 / (2 * math.pi * frecuencia * capacitancia)
    else:
        return 1 / (frecuencia_angular * capacitancia)


# Obtencion de la impedancia total
def Obtain_Z(impedancia_inductiva, impedancia_capacitiva, es_serie, Resistencia):
    if es_serie == "S":
        return math.sqrt((impedancia_inductiva - impedancia_capacitiva) ** 2 + Resistencia ** 2)
    else:
        return Obtain_Inverso(math.sqrt((Obtain_Inverso(Resistencia) ** 2) + (
                    Obtain_Inverso(impedancia_inductiva) - Obtain_Inverso(impedancia_capacitiva)) ** 2))


def Obtain_Angulo(impedancia_inductiva, impedancia_capacitiva, es_serie, Resistencia):
    if es_serie == "S":
        return (math.atan((impedancia_inductiva - impedancia_capacitiva) / Resistencia)) * 180 / math.pi
    else:
        return (math.atan(
            (Obtain_Inverso(impedancia_inductiva) - Obtain_Inverso(impedancia_capacitiva)) / Obtain_Inverso(
                Resistencia))) * 180 / math.pi



# Obtencion de corrientes
def Obtain_I(Voltaje, impedancia_total):
    return Voltaje / impedancia_total


def Ontain_Ir(Voltaje, Resistencia):
    return Voltaje / Resistencia


def Obtain_Ic(Voltaje, impedancia_capacitiva):
    return Voltaje / impedancia_capacitiva


def Obtain_Il(Voltaje, impedancia_inductiva):
    return Voltaje / impedancia_inductiva


# Obtencion factor de potencia
def Obtain_Factor_Potencia(desface, angulo):
    return desface-angulo


