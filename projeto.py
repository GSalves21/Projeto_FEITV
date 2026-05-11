#funções que usarei:

def Cadastrar(Name,Senha):
    registro = open("Usuarios.txt","a")
    registro.write("%s,%s\n" % (Name,Senha))
    registro.close()

#fim da função

#essa função é o menu de cadastro
def menu_cadastro():
        Nome = input("Cadastre seu nome: ")
        Senha = input("escolha uma senha:" )
        Cadastrar(Nome,Senha) #chamei a função para realizar o cadastro
        print("cadastro realizado com sucesso!")
        
        


#essa função ira fazer uma verificação se o login é válido

def verificar_login(Usuario,senha):
    acesso_usuario =  ("%s,%s\n" % (Usuario,senha)) # o /n faz a quebra de linha
    arquivo = open("Usuarios.txt","r")
    for  registro in arquivo:
        if registro == acesso_usuario:
            arquivo.close()
            return Usuario #será usado na função curtir
    else:
        arquivo.close()
        print("O usuário digitado não existe no sistema")
        return False
#fim da função

#Aqui está a função do menu de login:
def menu_login(usuario,senha):
    login = verificar_login(usuario,senha)
    if login == False: #se a função retornar falso o código pedirá que o usuário insira denovo usuário e senha e depois chamará a função verificar_login novamente para fazer a verificação e caso seja um usuario válido o loop quebrará e proseguiremos
        return False
    else:
        return True
        

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
        video_disponivel = video_disponivel.strip().split(';')
        catalogo[video_disponivel [0]] = video_disponivel[1:5] #Sempre o elemento 0 da lista cuja é o nome do video(filme/serie) será a chave do dicionário e o restante das informações referentes ao video serão o valor
    consulta.close()
    return catalogo

#aqui estará o dicionário que fara a consulta do catalogo:(coloquei logo de inicio do codigo para ja estar pronto todo catalogo pra consulta)
dicionario = dicionario_catalogo()

#essa lista  ja estara sendo carregado sempre que o programa inicializar :
usuarios_listas_favoritos = []
dicionario_videos_lista_favoritos = {}


#estará criando o dicionario que terá a informação de todas as listas de reprodução de cada usuário
def leitura_lista_favoritos():
    favoritos_usuarios = open('listas_reproducao_usuarios.txt','r')
    for lista in favoritos_usuarios:
        lista = lista.split(':')
        usuarios_listas_favoritos.append =  lista[0] + lista[1:]
    favoritos_usuarios.close()


def atualizar_lista_favoritos(usuario_atual,video_adicionado,remover = False): #essa lista adicionará ou apagará um filme da lista de favoritos
    if remover == False:
        usuarios_listas_favoritos.clear()
        adicionar_video = open('listas_reproducao_usuarios.txt','a')
        adicionar_video.write(f'{usuario_atual}:{video_adicionado}')
        adicionar_video.close()
        leitura_lista_favoritos()
    else:
        if remover == True:
            remover_video = open('listas_reproducao_usuarios.txt','w')
            for 

    
leitura_lista_favoritos()




#aqui havera a busca no dicionario para ver se o video que o usuario quer está no catalogo
def busca(video):
    for conteudo in dicionario:
        if video.strip().upper() == conteudo.upper().strip() :
            Titulo = f'titulo:{conteudo} \n'
            lancamento = f'Lançamento: {dicionario[conteudo][0]} \n'
            genero = f'Genêro: {dicionario[conteudo][1]} \n'
            duracao = f'duração: {dicionario[conteudo][2]} \n'
            sinopse = f'Sinopse: {dicionario[conteudo][3]} \n'
            return f'{Titulo}.{lancamento}.{genero}.{duracao}.{sinopse}'


#essa função permitirá o usuário curtir videos
def curtida(usuario,video):
    Curtidas = open('curtidas.txt','a')
    for obras in dicionario:
        if video.strip().upper() == obras.upper().strip() :
            curtir_titulo = obras
            curtida_existe = verificar_curtida_existente(usuario,curtir_titulo)
            if curtida_existe == True:
                Curtidas.write(f'{usuario}:{curtir_titulo}\n')
            else:
                print('você já curtiu esse video!')
    Curtidas.close()

#essa função não permitirá que o usuario curta um video que ele ja curtiu
def verificar_curtida_existente(usuario,obras):
    verificar_existencia = open('curtidas.txt','r')
    for curtida in verificar_existencia:
        if curtida.strip('\n') == f'{usuario}:{obras}':
            return False
    return True

 


#aqui está a navegação do programa depois do login
def navegar_seção():
    seção = int(input("Qual seção você deseja acessar? (1-buscar 2-gerenciar lista): "))
    if seção == 1:
        menu_busca()
    if seção == 2:
        menu_gerenciar_favoritos()

#aqui sera um submenu que aparecerá se o usuario escolher a opcao 2:
def menu_gerenciar_favoritos():
    print('o que você deseja fazer com  lista de reproduções de videos favoritos?')
    opcoes = int(input('1-criar,2-editar,3-excluir'))
    if opcoes == 1:
        criar_lista_reproducao(usuario)

    # if opcoes == 2:

    # if opcoes == 3:

#para evitar problemas posteriormente na edição de listas essa função não permitirá que um usuário crie uma nova lista com o mesmo nome de alguma que ele já criou
def verificar_listas(usuario,lista):
    listas_usuarios = open('listas_reproducao_usuarios.txt','r')
    lista_a_verificar = f'{usuario}:{lista}\n'
    for verificacao in listas_usuarios:
        if verificacao.strip().strip('\n') == lista_a_verificar.strip().strip('\n'):
            return False
    return True


 
#essa função permitirá que o usuario crie uma nova lista de reprodução
def criar_lista_reproducao(usuario):
    lista_reproducao = open('listas_reproducao_usuarios.txt','a')
    nome_lista = input('Nome da nova lista:')
    criar_nova_lista = verificar_listas(usuario,nome_lista)
    if criar_nova_lista == True:
        lista_reproducao.write(f'{usuario}:{nome_lista}\n')
        lista_reproducao.close()
        print('lista criada com sucesso!')
    if criar_nova_lista == False:
        print('essa lista já existe')
    menu_gerenciar_favoritos()





def menu_busca():
    while True:            
        video = input("Digite o nome do filme/série que você deseja acessar:")
        resultado = busca(video)
        
        if resultado == None:
            print("Video não encontrado!")
        else:
            print(resultado)
            acao = input('O que você deseja fazer agora?(L-curtir o video,A-adicionar na lista de reprodução,S-sair para o menu anterior)')
            if acao.upper() == 'L': 
                curtida(usuario,video)
            if acao.upper == 'A':
                lista_a_receber_video = input('insira em qual lista você deseja adicionar o video:')
                verificar_listas(usuario,lista_a_receber_video)
                if verificar_listas == False: #nessa função o false significa que a lista já existe

            if acao.upper() == 'S':
                break
    navegar_seção()

                
        
                


    
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
    menu_cadastro()

#fazer login
if acessar_menu_principal == 1:
    while True:
            usuario = input("Digite seu nome de usuário:")
            senha = input("Digite sua senha:")
            login_sucesso = menu_login(usuario,senha)
            if login_sucesso == True:
                break
            

#agora o usuario podera navegar pelas seções que ele escolher

navegar_seção()


            
    
        
        
        
           
    

  
