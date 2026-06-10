import os
os.system("cls")
nome_arquivo = "dados.txt"
with open(nome_arquivo, 'w+', encoding='utf-8') as arquivo:
    
    while True:
        print("\n--- MENU DE OPÇÕES ---")
        print("0 - SAIR")
        print("1 - Gravar uma linha")
        print("2 - Gravar varias linhas")

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
