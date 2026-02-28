#Aluno: Luiz Felipe Barbosa da Silva
#Código de um catalogo de animes com campos nome, data de lançamento, gênero, estudio e codigo.

import Menu
import Funções

while True:
    Menu.escrever()

    resposta = int(input("Escolha uma opção: "))
    print()

    if resposta == 1:
        with open('Código.txt','r') as cod:
            i = cod.read()
            if i == "":
                i = 0
            else:
                i = int(i)
        Funções.registrar(i)
        with open('Código.txt','w') as cod:
            cod.write(str(i + 1))
        with open('Códigos.txt','a+',encoding='utf-8') as codigos:
            codigos.write(str(i+1)+'\n')

    elif resposta == 2:
        Funções.listar()

    elif resposta == 3:
        with open('Código.txt','r') as cod:
            i = cod.read()
            if i == '0' or i == "":
                 print("Lista vazia, não é possível excluir.\n")
            else:
                x = int(input("Digite o código do anime para exclusão: "))
                print()
                Funções.excluir(x, int(i))

    elif resposta == 4:
        break