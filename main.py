import os
os.system("cls")
nome_arquivo = "dados.txt"
with open(nome_arquivo, 'w+', encoding='utf-8') as arquivo:
    
    while True:
        print("\n--- MENU DE OPÇÕES ---")
        print("0 - SAIR")
        print("1 - Gravar uma linha")
        print("2 - Gravar varias linhas")
        print("3 - Exibir o conteudo do arquivo")
        print("4 - Exibir uma linha dada pelo usuario")
        print("5 - Contar palavras")
        print("6 - Contar caracteres")
        print("7 - Contar palavras com N letras")
        print("8 - Contar palavras dadas pelo usuário")

        try:
            option = int(input("Selecione uma das opções: "))
        except ValueError:
            print("Por favor, digite um número válido.")
            continue

        match option:

            case 0:
                print("Saindo....")   
                break
                
              case 1:
                dados = input("Digite o texto: ")
                arquivo.write(dados)
                print("linha gravada com sucesso!")

            case 2:
               
            case 3:
                 print(f"\n--- {nome_arquivo}---")
               
                arquivo.seek(0)
                linhas = arquivo.readlines()
                
                if not linhas:
                    print(f"Não há nada no arquivo {nome_arquivo}")
                else:
                    for linha in linhas:
                        print(linha.strip())
                        
            case 4:
                
            case 5:
              
            case 6:
               
            case 7:

                
