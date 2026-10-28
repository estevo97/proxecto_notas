"""Funcións para clasificar notas.

FASE 1 · Desenvolve: USUARIO 2
"""


def aprobado(nota):
    return nota >= 5


def contar_aprobados(notas):
    return sum(1 for n in notas if n >= 5)


def cualificacion(nota):
    if nota < 5:
        return "Suspenso"
    elif nota < 7:
        return "Aprobado"
    elif nota < 9:
        return "Notable"
    else:
        return "Sobresaliente"
