import os
os.system("cls")

nome_arquivo = "dados.txt"

with open(nome_arquivo, 'a+', encoding='utf-8') as arquivo:

    while True:
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
            print("digite um número valido.")
            continue
        except:
            print("chame o programador chefe")
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
                try:
                    palavras = []

                    qtd_de_palavra = int(input("Digite quantas linhas voce quer escrever: "))

                    for i in range(qtd_de_palavra):
                        frases = input("Digite a palavra: ")
                        palavras.append(frases + "\n")

                except ValueError:
                    print("Digite apenas números!")

                except:
                    print("chame o programador chefe")


                else:
                    arquivo.writelines(palavras)
                    print("Linhas gravadas com sucesso!")
                    arquivo.flush()


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
                try:
                    arquivo.seek(0)
                    linhas = arquivo.readlines()

                    linha_desejada = int(input(f"Defina a linha que quer ver (1 a {len(linhas)}): "))

                    if 1 <= linha_desejada <= len(linhas):
                        print(
                            f"Conteúdo: {linhas[linha_desejada - 1]}")
                    else:
                        print("Essa linha não existe!")

                except ValueError:
                    print("Digite apenas números!")
                except:
                    print("chame o programador chefe")

                else:
                     print("Consulta realizada com sucesso!")

            case 5:
                arquivo.seek(0)
                texto = "".join(arquivo)
                qtd_palavras = texto.split()

                print(f"Quantidade total de palavras: {len(qtd_palavras)}")

            case 6:
                arquivo.seek(0)
                texto = arquivo.read()
                print(f"Quantidade de caracteres: {len(texto)}")

            case 7:
                try:
                    count = 0

                    arquivo.seek(0)

                    palavras = arquivo.read()
                    palavras2 = palavras.split()

                    n = int(
                        input("Digite o numero de caracteres: "))

                    for palavra in palavras2:
                        if len(palavra) == n:
                            count += 1

                except ValueError:
                    print("Digite apenas números!")

                else:
                    print(f"Existem {count} palavras com {n} caracteres")

            case 8:
                arquivo.seek(0)

                texto = arquivo.read().lower()

                palavra = input("Digite a palavra: ").lower()

                quantidade = texto.split().count(palavra)

                print(f"A palavra '{palavra}' aparece {quantidade} vezes no arquivo.")

            case _:
                print("Opção inválida!")
