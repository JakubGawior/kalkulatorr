x = input('Podaj x: ')
znak = input('Podaj znak(+,-,*,/,**,//,%): ')
y = input('Podaj y: ')


if znak == '+':
    wynik = int(x) + int(y)

if znak == '-':
    wynik = int(x) - int(y)

if znak == '*':
    wynik = int(x) * int(y)

if znak == '**':
    wynik = int(x) ** int(y)

if znak == '/':
    wynik = int(x) / int(y)

if znak == '//':
    wynik = int(x) // int(y)

if znak == '%':
    wynik = int(x) % int(y)

print(x, znak, y, '=', wynik)
