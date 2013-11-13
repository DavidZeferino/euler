maior_palindromo = 0 
for contagem_inversa_numero in range(999,0,-1):
    for b in range(999,contagem_inversa_numero,-1):
        print b
        if contagem_inversa_numero * b < maior_palindromo:
            break
        palidromo = '%i'%(contagem_inversa_numero * b)
        if palidromo==palidromo[::-1]:
            maior_palindromo = max(maior_palindromo,contagem_inversa_numero * b)
            break
print maior_palindromo
