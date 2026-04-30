#funções que usarei:

def Cadastrar(Name,Senha):
    registro = open("Usuarios.txt","a")
    registro.write("Usuario: %s , Senha: %s \n" % (Name,Senha))
    registro.close()

#fim da função

#essa função ira fazer uma verificação se o login é válido

def verificar_login(Usuario,senha):
    login = open("Usuarios.txt","r")
    for  validação in login:
        validação = ("Usuario: %s , Senha: %s \n" % (Usuario,senha))
        if validação == login.readlines():
            login.close()
            return True
        else:
            print("O usuário digitado não existe no sistema")
        return False
#fim da função

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
    cadastro = Cadastrar(Nome,Senha)

#fazer login

else:
    if acessar_menu_principal == 1:
        usuario = input("Digite seu nome de usuário: ")
        senha = input("Digite sua senha: ")
        login = verificar_login(usuario,senha)

#se a função retornar falso o código pedirá que o usuário insira denovo usuário e senha e depois chamará a função verificar_login novamente para fazer a verificação e caso seja um usuario válido o loop quebrará e proseguiremos
    
    if login == False:
        while True:
            usuario = input("Digite seu nome de usuário: ")
            senha = input("Digite sua senha: ")
            login = verificar_login(usuario,senha)
            if login == True:
                break
print("Bem vindo!")

#agora o usuario podera navegar pelas seções que ele escolher

seção = int(input("Qual seção você deseja acessar? (1-buscar 2-curtir 3-gerenciar lista): "))

# if seção == 1:









    
    

