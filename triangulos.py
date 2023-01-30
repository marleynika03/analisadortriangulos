class ANSI():
    def background(code):
        return '\33[{code}m'.format(code=code)

    def style_text(code):
        return '\33[{code}m'.format(code=code)

    def color_text(code):
        return '\33[{code}m'.format(code=code)

print('-=' *20)
print('Analisador de triângulos')
print('-=' *20)

while True:
    try:
        a = float(
            input('O valor do segmento A é: '))
        b = float(
            input('O valor do segmento B é: '))
        c = float(
            input('O valor do segmento C é: '))
        if a + b > c and a + c > b and b + c > a:
            r =  ANSI.background(
                40) + ANSI.color_text(32) + ANSI.style_text(7) + 'Estes valores podem formar um triângulo.\033[m'
            print(r)
        if a == b == c:
            print('Este é um triângulo equilátero.')
        elif a == b or a == c or b == c:
            print('Esté é um triângulo isósceles.')
        elif a != b != c:
            print('Este é um triângulo escaleno.')
        else:
            print('Estes valores não formam um triângulo.')
        break
    except ValueError:
        l = ANSI.background(
            40) + ANSI.color_text(31) + ANSI.style_text(7) + 'Por favor, digite um valor numérico.\033[m'
        print(l)
    except KeyboardInterrupt:
        break
