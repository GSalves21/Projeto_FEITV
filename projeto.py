#menu inicial:

print("Bem vindo a FEI TV!")
print("caso você deseje fazer login,digite 0,se não possui login,digite 1 para se cadastrar: ")
acessar_menu_principal = int(input("Qual ação você quer realizar? ")) # lembrar de pensar em um nome melhor para essa variavél
while acessar_menu_principal != 0 and acessar_menu_principal != 1:
    print("O número digitado é invalido!")
    acessar_menu_principal = int(input("Qual ação você quer realizar? ")) # lembrar de pensar em um nome melhor para essa variavél

#definindo se irá pra login ou cadastro:
if acessar_menu_principal == 0:
    

