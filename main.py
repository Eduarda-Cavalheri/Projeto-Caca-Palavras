import random
import string


class CacaPalavras:
    def __init__(self, linhas, colunas):
        self.linhas = linhas
        self.colunas = colunas
        self.matriz = [['.' for _ in range(colunas)] for _ in range(linhas)]

    def inserir_palavras(self, palavra, linha_inicial, coluna_inicial, direcao):
        palavra = palavra.upper()
        if direcao == 'H':
            #Verifica se a palavra cabe na linha
            if coluna_inicial + len(palavra) > self.colunas:
                print(f'ERRO: A palavra {palavra} não cabe horizontalmente nesta posição.')
                return

            #Substitui os pontos pelas letras da palavra na mesma linhas, avançando as colunas.
            for i in range (len(palavra)):
                self.matriz[linha_inicial][coluna_inicial + i] = palavra[i]



#Usando a biblioteca 'string' para pegar as letras maiusculas do alfabeto.
alfabeto = string.ascii_uppercase