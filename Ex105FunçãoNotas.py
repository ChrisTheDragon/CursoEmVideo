def notas(*infnot, sit=False):
    geral = {}
    s = 0

    geral['Total'] = len(infnot)
    geral['Maior'] = max(infnot)
    geral['Menor'] = min(infnot)
    geral['Media'] = sum(infnot)/len(infnot)

    if sit:
        if geral['Media'] <= 5:
            geral['Situação'] = 'Ruim'
        elif 5 < geral['Media'] <= 7:
            geral['Situação'] = 'Razoável'
        elif geral['Media'] > 7:
            geral['Situação'] = 'Boa'

    return geral


resp = notas(10, 5, 8.5, 6, sit=True)
print(resp)
resp = notas(4, 8.5, 5, 6, 10)
print(resp)
resp = notas(4, 6, 5, sit=True)
print(resp)