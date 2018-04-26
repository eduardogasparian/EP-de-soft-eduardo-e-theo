# EP-de-soft-eduardo-e-theo

Lista_de_produtos = {}

Escolha = int(input('''0 - Sair
             1 - Adicionar item
             2 - Remover item
             3 - Alterar item
             4 - Imprimir estoque
             Faça sua escolha:'''))



while Escolha != 0:
    
    if Escolha == 1:
        Produto = input('Nome do produto:')
        Quantidade = int(input('Quantidade:'))
        Lista_de_produtos[Produto] = {}
        Lista_de_produtos[Produto]['Quantidade'] = Quantidade
        if Produto in Lista_de_produtos:
            print('Produto já cadastrado')
    
        print('{0}: Quantidade: {1}'.format(Produto, Quantidade))
    

    elif Escolha == 2:
        Produto = input('Nome do produto:')
        Quantidade = int(input('Quantidade:'))
        del Lista_de_produtos[Produto]
        print('Produto não encontrado')
        
    elif Escolha == 3:
        if Produto == input('Nome do produto:'):
            Quantidade_2 = int(input('Quantidade:'))
            Quantidade_2 += Quantidade
            print(Quantidade_2)

    elif Escolha == 4:
        print(Lista_de_produtos)
        
    Escolha = int(input('''0 - Sair
             1 - Adicionar item
             2 - Remover item
             3 - Alterar item
             4 - Imprimir estoque
             Faça sua escolha:'''))


if Escolha == 0:
    print('Até mais!')
    