maior_palindromo = 0 
for contagem_inversa_numero in range(999,0,-1):
    for contagem_polidromo in range(999,contagem_inversa_numero,-1):
        if contagem_inversa_numero * contagem_polidromo < maior_palindromo:
            break
        palidromo = '%i'%(contagem_inversa_numero * contagem_polidromo)
        if palidromo==palidromo[::-1]:
            maior_palindromo = max(maior_palindromo,contagem_inversa_numero * contagem_polidromo)
            break
print maior_palindromo
