s1 = float(input('\033[30;42mPrimiro seguimento: \033[m'))
s2 = float(input('\033[30;41mSegundo seguimento: \033[m'))
s3 = float(input('\033[30;44mTerceiro seguimento: \033[m'))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    if s1 == s2 == s3:
        t = 'equilátero'
    elif s1 == s2 or s2 == s3 or s3 == s1:
        t = 'isósceles'
    elif s1 != s2 and s2 != s3 and s3 != s1:
        t = 'Escaleno'
    print(f'\033[97mOs seguimentos podem formar um triangulo {t}\033[m')
else:
    print('\033[97mOs seguimentos não podem formar um triangulo\033[m')


