#função para criar o cadastro
def cadastro():
    print("Vamos iniciar seu cadastro: ")
    cadastro_email_usuario = input("Insira seu email: ")
    cadastro_usuario_senha = input("crie uma senha: ")
    print("etapa concluida!")
    cadastro_usuario_nome = input("Digite um nome de usuário: ")
    email_usuario = cadastro_email_usuario
    senha_usuario = cadastro_usuario_senha
    nome_usuario = cadastro_usuario_senha 
    usuario = [nome_usuario,email_usuario,senha_usuario]
    
#menu inicial:

print("Bem vindo a FEI TV!")
print("caso você deseje fazer login,digite 0,se não possui login,digite 1 para se cadastrar: ")
acessar_menu_principal = int(input("Qual ação você quer realizar? ")) # lembrar de pensar em um nome melhor para essa variavél
while acessar_menu_principal != 0 and acessar_menu_principal != 1:
    print("O número digitado é invalido!")
    acessar_menu_principal = int(input("Qual ação você quer realizar? ")) # lembrar de pensar em um nome melhor para essa variavél


#se houver o login quais opções de menu será oferecida ao usuário:
if acessar_menu_principal == 0:
    print("login realizado com sucesso")#talvez posteriormente eu mova esse print para uma função de login
    print("1-Buscar,2-curtir,3-Gerenciar listas")
    opção_menu_usuário = int(input("Digite a opção que você deseja realizar: "))
    while opção_menu_usuário < 1 or opção_menu_usuário > 3:
        print("Opção inválida!")
        print("1-Buscar,2-curtir,3-Gerenciar listas")
        opção_menu_usuário = int(input("Digite a opção que você deseja realizar: "))



    

