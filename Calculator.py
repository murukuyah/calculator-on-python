n1 = int(input('Gib Erste Zahl: '))
n2 = int(input('Gib Zweite Zahl: '))
v = int(input('Welche Operation?\n1 Addition\n2 Subtraktion\n3 Division\n4 Multiplikation\n'))

if v == 1:
    r = n1 + n2
    o = 'Addition'
elif v == 2:
    r = n1 - n2
    o = 'Subtraktion'
elif v == 3:
    if n2 != 0:
        r = n1 / n2
        o = 'Division'
    else:
        print('Division durch 0 geht nicht!')
        exit()
elif v == 4:
    r = n1 * n2
    o = 'Multiplikation'
else:
    print('Falsche Operation!')
    exit()

print('Ergebnis', o, '=', r)
input("\nDrücke Enter, um das Programm zu beenden")
