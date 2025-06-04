grade_pontuações = {
    'f':    [32, 28, 25, 18, 15, 11, 7, 5],
    'm':    [50, 47, 44, 41, 38, 35],
    'd':  [55, 60, 65, 70]
}


def calculo_por_turno(grau_dificuldade,tentativa):
    resultado_por_turno = grade_pontuações.get(grau_dificuldade)
    return resultado_por_turno[tentativa-1]

resultado_por_turno=(calculo_por_turno('f',3))
print(resultado_por_turno)
    