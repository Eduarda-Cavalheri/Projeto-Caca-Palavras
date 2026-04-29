import random
import string


class CacaPalavras:
    def __init__(self, linhas, colunas):
        self.linhas = linhas
        self.colunas = colunas
        self.matriz = [['.' for _ in range(colunas)] for _ in range(linhas)]

    def inserir_palavras(self, palavra, linha_inicial, coluna_inicial, direcao):
        palavra = palavra.upper()
        direcao = direcao.upper()

        if direcao == 'H':
            #Verifica se a palavra cabe na linha
            if coluna_inicial + len(palavra) > self.colunas:
                print(f'ERRO: A palavra {palavra} não cabe nesta posição.')
                return
        elif direcao == 'V':
            if linha_inicial + len(palavra) > self.linhas:
                print(f'ERRO: A palavra {palavra} não cabe nesta posição.')
                return

            for i in range(len(palavra)):
                if direcao == 'h':
                    self.matriz[linha_inicial][coluna_inicial + i] = palavra[i]
                else:
                    self.matriz[linha_inicial + i][coluna_inicial] = palavra[i]

    def preencher_vazios(self):
        # Usando a biblioteca 'string' para pegar as letras maiusculas do alfabeto.
        alfabeto = string.ascii_uppercase
        for l in range(self.linhas):
            for c in range(self.colunas):
                if self.matriz[l][c] == '.':
                    self.matriz[l][c] = random.choice(alfabeto)

    def exibir(self):
        for linha in self.matriz:
            linha_formatada = ' '.join(linha)
            print(linha_formatada)



