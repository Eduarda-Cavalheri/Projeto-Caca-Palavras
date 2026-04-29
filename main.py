from caca_palavras import CacaPalavras

jogo = CacaPalavras(10, 10)
jogo.inserir_palavras('javascript', 0, 0, 'v')
jogo.inserir_palavras('css', 2, 3, 'h')
jogo.inserir_palavras('python', 1, 1, 'h')
jogo.inserir_palavras('programar', 1, 7, 'v')
jogo.inserir_palavras('mysql', 9, 1, 'h')
jogo.inserir_palavras('sqlserver', 1, 9, 'v')
jogo.preencher_vazios()
jogo.exibir()
