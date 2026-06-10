import os
os.system("cls")

nome_arquivo = "dados.txt"

with open(nome_arquivo, 'a+', encoding='utf-8') as arquivo:
    
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
                arquivo.write(dados + "\n")
                arquivo.flush() 
                print("Linha gravada com sucesso!")

            case 2:
                palavras = []
                qtd_de_palavra = int(input("digite quantas palavras voce quer escrer"))
                for i in range (qtd_de_palavra):
                      frases = input("digite a palavra: ")
                      palavras.append(frases + "\n")
                arquivo.writelines(palavras)
            case 3:
                print(f"\n--- {nome_arquivo} ---")
                arquivo.seek(0)
                linhas = arquivo.readlines()
                
                if not linhas:
                    print(f"Não há nada no arquivo {nome_arquivo}")
                else:
                    for linha in linhas:
                        print(linha.strip())

            case 4:
                    arquivo.seek(0)
                    linhas = arquivo.readlines()
                    linha_desejada = int(input(f"Defina a linha que quer ver (1 a {len(linhas)}): "))
                    if 0 <= linha_desejada <= len(linhas):
                            print(f"Conteúdo: {linhas[linha_desejada - 1]}")
                    else:
                            print("Essa linha não existe no arquivo!")
            case 5:
                arquivo.seek(0)
                texto = "".join(arquivo)
                qtd_palavras = texto.split()
                print(f"Quantidade total de palavras: {len(qtd_palavras)}")

            case 6:
               
                qtd_letras = int(input("Quantidade de letras: ")) 
                count = 0
                     
                arquivo.seek(0)
                texto = "".join(arquivo)
        
                qtd_palavras = texto.split()
        
                for palavra in qtd_palavras:
                    if len(palavra) == qtd_letras:
                        count += 1
                            
                print(f"Palavras com {qtd_letras} letras: {count}")

            case 7:
                pass

            case 8:
                arquivo.seek(0)
                palavras = arquivo.read()
                palavras2 = palavras.split()
                n = int(input("digite o numero de caracteres: "))
                for palavras2 in palavras2:
                    if len(palavras) == n:
                        count = count + 1
                print(f"existem {count} palavras com {n}")
           
            while True:
                qtd_palavras = []
                a = input("Digite uma palavra ou 'sair' para terminar: ").strip().lower()
                if a == "sair":
                    break
                    
                qtd_palavras.append(a)
               
                print(f"Quantidade de palavras até agora: {len(qtd_palavras)}")
