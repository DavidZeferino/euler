def listar_dicionarios(numeros):

    dic_numeros = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen'
    }

    dic_dezenas = {
        2: 'twenty',
        3: 'thirty',
        4: 'forty',
        5: 'fifty',
        6: 'sixty',
        7: 'seventy',
        8: 'eighty',
        9: 'ninety'
    }

    # garante que estamos trabalhando com um valor positivo
    numeros = abs(numeros)

    saida = ''

    if numeros == 0:
        saida = 'zero'
    else:

        if numeros >= 1000:
            saida += dic_numeros[numeros / 1000]
            saida += 'thousand'
            if numeros % 1000 > 0:
                saida += ' '
            numeros %= 1000

        if numeros >= 100:
            saida += dic_numeros[numeros / 100]
            saida += 'hundred'
            if numeros % 100 > 0:
                saida += ' and '
            numeros %= 100

        if numeros >= 20:
            saida += dic_dezenas[numeros / 10]
            numeros %= 10
            if numeros % 10 in dic_numeros:
                saida += ' '

        if numeros in dic_numeros:
            saida += dic_numeros[numeros]

    return saida

def limpar_str(string):
    string = string.replace(' ','')
    #string = string.replace('-','')
    return string

#for i in range(0,1001):
    #print listar_dicionarios(i)

print sum(len(limpar_str(listar_dicionarios(numeros_em_extenso))) for numeros_em_extenso in range(1,1001))