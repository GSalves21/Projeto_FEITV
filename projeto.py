#funções que usarei:

def Cadastrar(Name,Senha):
    registro = open("Usuarios.txt","a")
    registro.write("%s,%s\n" % (Name,Senha))
    registro.close()

#fim da função

#essa função ira fazer uma verificação se o login é válido

def verificar_login(Usuario,senha):
    acesso_usuario =  ("%s,%s\n" % (Usuario,senha)) # o /n faz a quebra de linha
    arquivo = open("Usuarios.txt","r")
    for  registro in arquivo:
        if registro == acesso_usuario:
            arquivo.close()
            return True
    else:
        arquivo.close()
        print("O usuário digitado não existe no sistema")
        return False
#fim da função


#Agora farei uma função pra salvar varios filmes e suas informações em um arquivo no formato txt e já criar o catalogo:
def criando_catalogo(Nome,ano_lancamento,genero,duracao,sinopse):
    catalogo = open('catalogo.txt','a')
    catalogo.write(f'{Nome};{ano_lancamento};{genero};{duracao};{sinopse}\n')
    catalogo.close()

#aqui havera uma leitura de cada linha do catalogo.txt e criará uma lista usando o metodo split
def dicionario_catalogo():
    catalogo = {}
    consulta = open('catalogo.txt','r')
    for video_disponivel in consulta:
        video_disponivel = video_disponivel.split(';')
        catalogo[video_disponivel [0]] = video_disponivel[1:5] #Sempre o elemento 0 da lista cuja é o nome do video(filme/serie) será a chave do dicionário e o restante das informações referentes ao video serão o valor
    consulta.close()
    return catalogo
    
    
        

#aqui estará o dicionário que fara a consulta do catalogo:(coloquei logo de inicio do codigo para ja estar pronto todo catalogo pra consulta)
dicionario = dicionario_catalogo

#menu inicial:
print("Bem vindo a FEI TV!")
print("caso você deseje fazer login  digite 1,se não possui login digite 0 para se cadastrar: ")

#definindo se irá pra login ou cadastro:

acessar_menu_principal = int(input("Qual ação você quer realizar? ")) # lembrar de pensar em um nome melhor para essa variavél
while acessar_menu_principal != 0 and acessar_menu_principal != 1:
    print("O número digitado é invalido!")
    acessar_menu_principal = int(input("Qual ação você quer realizar? ")) # lembrar de pensar em um nome melhor para essa variavél

#Fazer um cadastro
if acessar_menu_principal == 0:
    Nome = input("Cadastre seu nome: ")
    Senha = input("escolha uma senha:" )
    Cadastrar(Nome,Senha) #chamei a função para realizar o cadastro
    print("cadastro realizado com sucesso!")


#fazer login

else:
    if acessar_menu_principal == 1:
        usuario = input("Digite seu nome de usuário:")
        senha = input("Digite sua senha:")
        login = verificar_login(usuario,senha)

#se a função retornar falso o código pedirá que o usuário insira denovo usuário e senha e depois chamará a função verificar_login novamente para fazer a verificação e caso seja um usuario válido o loop quebrará e proseguiremos
    
    if login == False:
        while True:
            usuario = input("Digite seu nome de usuário:")
            senha = input("Digite sua senha:")
            login = verificar_login(usuario,senha)
            if login == True:
                break

print("Bem vindo!")

#agora o usuario podera navegar pelas seções que ele escolher

seção = int(input("Qual seção você deseja acessar? (1-buscar 2-curtir 3-gerenciar lista): "))

if seção == 1:
    video = input("Digite o nome do filme/série que você deseja acessar:")
    
