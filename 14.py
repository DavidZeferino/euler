def contar_cadeia_collatz(numero):
    tamanho_da_cadeia = 1
    while numero > 1:
        tamanho_da_cadeia += 1
        if numero % 2 == 0:
            numero /= 2
        else:
            numero =  3 * numero + 1
    return tamanho_da_cadeia
 
 
possivel_resposta = {
    'numero' : 0,
    'tamanho_da_cadeia' : 0
}
 
for numero_possivel in range (1000000):
    tamanho_da_cadeia = contar_cadeia_collatz(numero_possivel)
    if tamanho_da_cadeia > possivel_resposta['tamanho_da_cadeia']:
        possivel_resposta['tamanho_da_cadeia'] = tamanho_da_cadeia
        possivel_resposta['numero'] = numero_possivel
 
print possivel_resposta['numero']