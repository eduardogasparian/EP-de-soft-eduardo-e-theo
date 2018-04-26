# EP-de-soft-eduardo-e-theo# EP-de-soft-eduardo-e-theo
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
import json
Loja=dict()
lista_de_produtos={}
i=1
comandos=[0,1,2,3,4]
comandos2=[0,1,2,3,4,5,6]

try:
    with open('Lista de produtos.txt','r') as arquivo:
        Loja = json.loads(arquivo.read())
except: FileNotFoundError
   
while i!=0:
    lista=["comando Loja", "0 - sair", "1 - entrar na loja", "2 - adicionar loja", "3 - excluir loja","4 - imprimir lojas cadastradas"]
    for e in lista:
        print(e)
    opcao=int(input("escolha um comando:"))       
    if opcao not in comandos:
        print("Comando inválido")

    elif opcao==0:
       i=0 
       print("Obrigado por utilizar o sistem, tenha um bom dia")

    elif opcao == 1:
        nome_da_loja=input("Digite o nome da loja:")
        if nome_da_loja not in Loja:
            print("Loja não encontrada")
        while i!=0:
              print(nome_da_loja)
              lista=["Comandos Estoque", "0 - sair", "1 - adicionar item", "2 - excluir item", "3 - alterar item", "4 - imprimir estoque", "5 - produtos com quantidade negativa","6 - valor total do estoque"]
              for e in lista:
                  print(e)
              opcao=int(input("escolha um comando:"))       
              if opcao not in comandos2:
                      print("Comando inválido")
 
              elif opcao==0:
                     i=0 
                     print("Obrigado por utilizar o sistema, tenha um bom dia")  
                     
              elif opcao==1:
                   nome_do_produto=input("Nome do item:")
                   if nome_do_produto not in lista_de_produtos: 
                          lista_de_produtos[nome_do_produto] = {}
                          quantidadeinicial=int(input("Quantidade inicial:"))
                          while quantidadeinicial<0:
                              quantidadeinicial=int(input("A quantidade inicial não pode ser negativa"))
                          lista_de_produtos[nome_do_produto]['quantidade']=quantidadeinicial    
                          preco_do_item=float(input("Preço do item:"))    
                          while preco_do_item<0:
                                  preco_do_item=float(input("O preço do item não pode ser negativo"))
                          while preco_do_item==0:
                                  preco_do_item=float(input("O preço não pode ser nulo. Digite novamente:"))
                          lista_de_produtos[nome_do_produto]['preço do produto']=preco_do_item
                          Loja[nome_da_loja]['Lista de produtos']=lista_de_produtos
                          print("item cadastrado")
                   else:
                          print("item já cadastrado")
      

              elif opcao==2:
                  nome_do_produto=input("Nome do produto:")
                  if nome_do_produto in lista_de_produtos:
                      del(lista_de_produtos[nome_do_produto])
                      print("item removido")
                  else:
                      print("item não encontrado.")  
          
         
              elif opcao==3:
                  nome_do_produto=input("Nome do item:")
                  if nome_do_produto not in Loja[nome_da_loja]['Lista de produtos']:
                      print ("item não encontrado.")
                  elif nome_do_produto in Loja[nome_da_loja]['Lista de produtos']:
                          print("1 - alterar quantidade")
                          print("2 - alterar preço ")
                          print("3 - realizar os dois comandos de cima")
                          opcao=int(input("escolha umcomando:"))
                          while opcao < 1 or opcao > 3:
                              opcao=int(input("Comando inválido, digite um comando valido:"))
                          if opcao == 1:
                              print("Quantidade atual:{0}".format(Loja[nome_da_loja]['Lista de produtos'][nome_do_produto]['quantidade']))
                              nova_quantidade=int(input("quantidade nova:"))
                              Loja[nome_da_loja]['Lista de produtos'][nome_do_produto]['quantidade']+=nova_quantidade
                              print("Quantidade mudada")
                          elif opcao == 2:
                              print("Preço atual:{0}".format(Loja[nome_da_loja]['Lista de produtos'][nome_do_produto]['preço do produto']))
                              novo_preco=float(input("Novo preço:"))
                              while novo_preco + Loja[nome_da_loja]['Lista de produtos'][nome_do_produto]['preço do produto'] < 0 or novo_preco + Loja[nome_da_loja]['Lista de produtos'][nome_do_produto]['preço do produto'] == 0 :
                                  novo_preco=float(input("O preço não pode ser negativo"))    
                              Loja[nome_da_loja]['Lista de produtos'][nome_do_produto]['preço do produto']+=novo_preco
                              print("o preço mudou")
                          elif opcao == 3:
                              print(Loja[nome_da_loja]['Lista de produtos'][nome_do_produto])
                              nova_quantidade=int(input("quantidade nova do item:"))
                              Loja[nome_da_loja]['Lista de produtos'][nome_do_produto]['quantidade']+=nova_quantidade
                              novo_preco=float(input("Novo preço:"))
                              while novo_preco + Loja[nome_da_loja]['Lista de produtos'][nome_do_produto]['preço do produto'] < 0 :
                                  novo_preco=float(input("O preço não pode ser negativo!"))
                              while novo_preco + Loja[nome_da_loja]['Lista de produtos'][nome_do_produto]['preço do produto'] == 0:
                                  novo_preco=float(input("O preço não pode ser zero"))
                              Loja[nome_da_loja]['Lista de produtos'][nome_do_produto]['preço do produto']+=novo_preco
                              print("o item foi mudado") 

              elif opcao==4:
                  for k in Loja[nome_da_loja]['Lista de produtos']:
                      print("{0}:{1}".format(k, Loja[nome_da_loja]['Lista de produtos'][k]))                               

              elif opcao==5:  
                  for produto in Loja[nome_da_loja]['Lista de produtos']:
                      if Loja[nome_da_loja]['Lista de produtos'][produto]["quantidade"] < 0:
                          print("{0}:{1}".format(produto, Loja[nome_da_loja]['Lista de produtos'][produto]["quantidade"]))

              elif opcao==6:
                  valor_do_item = 0
                  for item in Loja[nome_da_loja]['Lista de produtos']:
                      valor_do_item += Loja[nome_da_loja]['Lista de produtos'][item]['quantidade'] * Loja[nome_da_loja]['Lista de produtos'][item]['preço do produto']
                  print("O valor total do mesmo item que existe no estoque é:{0}".format(valor_do_item))                          

    elif opcao==2:
                   nome_da_loja=input("Digite o nome da loja:")
                   if nome_da_loja not in Loja:
                       Loja[nome_da_loja]={}
                       Loja[nome_da_loja]['Lista de produtos']={}
                       print("Loja cadastrada")
                   else:
                       print("Loja já cadastrada")

    elif opcao == 3:
                  nome_da_loja=input("Digite o nome da loja:")
                  if nome_da_loja not in Loja:
                      print("Loja não encontrada.")
                  else:
                      del(Loja[nome_da_loja])    
                      print("Loja excluida")             
             

    elif opcao == 4:
                for e in Loja:
                    print(e)
             
                                 
atualizacao = json.dumps(Loja, sort_keys = True)
with open('Lista de produtos.txt','w') as arquivo:
    arquivo.write(atualizacao)