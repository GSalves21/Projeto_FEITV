#funções que usarei:
def Cadastrar(Name,Senha):
    registro = open("Usuários.txt","a")
    registro.write("Usuário: %s , Senha: %s \n" % (Name,Senha))
    registro.close()


def verificar_login(Usuario,senha):
    login = open("Usuarios.txt","r")
    for  validação in login:
        if validação == ("Usuário: %s , Senha: %s \n" % (Usuario,Senha)):
            return True
        else:
            print("O usuário digitado não existe no sistema")
        return False





#menu inicial:

print("Bem vindo a FEI TV!")
print("caso você deseje fazer login,digite 0,se não possui login,digite 1 para se cadastrar: ")

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
elif acessar_menu_principal == 1:
    usuario = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")
    login = verificar_login(usuario,senha)
    if login == False:
        while True:
            usuario = input("Digite seu nome de usuário: ")
            senha = input("Digite sua senha: ")




    
    

