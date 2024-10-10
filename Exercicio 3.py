'''

int INDICE = 12, SOMA = 0, K = 1;
enquanto K < INDICE
faça { K = K + 1; SOMA = SOMA + K; }
imprimir(SOMA);
'''

INDICE = int(12)
soma = 0
k = 1
while k < INDICE:
    k = k + 1
    soma = soma + k
print('O Resultado final de "soma" sera {}'.format(soma))