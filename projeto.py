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
        catalogo[video_disponivel [0]] = video_disponivel[1:] #Sempre o elemento 0 da lista cuja é o nome do video(filme/serie) será a chave do dicionário e o restante das informações referentes ao video serão o valor
    consulta.close()
    return catalogo

#aqui estará o dicionário que fara a consulta do catalogo:(coloquei logo de inicio do codigo para ja estar pronto todo catalogo pra consulta)
dicionario = dicionario_catalogo()

#essa lista  ja estara sendo carregado sempre que o programa inicializar :
usuarios_listas_favoritos = {}# a chave será o nome do usuario e o valor sera uma lista com o nome das listas de reproduçao
dicionario_videos_lista_favoritos = {}


# estarei fazendo uma função que puxa os dados do arquivo txt e os carrega em usuarios
def leitura_lista_favoritos():
    favoritos_usuarios = open('lista_reproducao_usuarios.txt','r')
    for usuario_lista in favoritos_usuarios:
        separacao_chave_valor = usuario_lista.strip('\n').split(',')
        usuarios_listas_favoritos[separacao_chave_valor[0]] = separacao_chave_valor[1].strip("[]''").split(",")
    favoritos_usuarios.close()
    print(usuarios_listas_favoritos)

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

# usuarios_listas_favoritos = {}
def criar_lista_reproducao(usuario):
    lista_nova = input('Digite o nome da nova lista de favoritos:')
    if usuario  in (usuarios_listas_favoritos):
        usuarios_listas_favoritos[usuario].append(lista_nova)

    if usuario not in usuarios_listas_favoritos:
        usuarios_listas_favoritos[usuario] = []
        usuarios_listas_favoritos[usuario].append(lista_nova)
    persistir_criacao_lista() #sempre que uma lista nova for adicionada o arquivo será atualizado
    leitura_lista_favoritos()

    print('lista de favoritos criada com sucesso')
    menu_gerenciar_favoritos()
    

#agora essa função estará lendo o que está no dicionario e passando pro arquivo txt:
def persistir_criacao_lista():
    guardar_informacao = open('lista_reproducao_usuarios.txt','w')
    for key in usuarios_listas_favoritos:
        guardar_informacao.write(f'{key},{usuarios_listas_favoritos[key]}\n')#ficar de olho nesse \n
    guardar_informacao.close()

 
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


            
    
        
        
        
           
    

  
