def registrar(cod):
    nome = input("Nome do anime: ")
    ano = input("Ano de lançamento: ")
    genero = input("Genêro: ")
    estudio = input("Estudio: ")

    anime = nome + " | " + ano + " | " + genero + " | " + estudio + " | " + str(cod + 1) + '\n'
    with open('Animes.txt','a+', encoding = 'utf-8') as lista:
        lista.write(anime)

def listar():
    with open('Animes.txt','r',encoding='utf-8') as lista:
        print(lista.read())

def excluir(cod, final):
    verificação = False
    i = 0
    with open ('Códigos.txt','r',encoding='utf-8') as cods:
        teste = str(cod) + '\n'
        codigos = []
        for codigo in cods:
            codigos.append(codigo)
            if codigo == teste:
                verificação = True
                codigos.remove(codigo)
            elif codigo != teste and verificação != True:
                i += 1
    with open('Animes.txt','r',encoding='utf-8') as anime:
        lista = []
        for linha in anime:
            lista.append(linha)
            
    if verificação == True:
        lista.pop(i)                
        with open('Animes.txt','w',encoding='utf-8') as anime:
            anime.writelines(lista)
        with open('Códigos.txt','w',encoding='utf-8') as cods:
            cods.writelines(codigos)
    else:
        print("Código de exclusão inválido.")