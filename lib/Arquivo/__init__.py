import random
import string
def arquiche_true(valor):
    """

    :param valor: Informações do documento que sera a minha lista de .txt
    :return: Verificação de existe essa lista, ou não.
    """
    try:
        a = open(valor, 'rt')
        a.close()
    except:
        return False
    else:
        return True

def arquiche_creating(valor):
    """

    :param valor: criação do meu arquivo .txt de forma automatica, caso ele não exista
    :return: O arquivo criado com sua sentença.txt
    """
    try:
        a = open(valor, 'wt+')
        a.close()
    except:
        print('Erro ao criar arquivo.')
    else:
        print(f'Arquivo {valor} criado com sucesso.')

def len_line(len=45):
    """

    :param len: linhas para melhorar a vida do usuario
    :return: linha no tamanho tam
    """
    return '-' * len

def cabecalho(msg):
    """

    :param msg: Mensagem do cabeçalho do programa.
    :return: Cabeçalho do programa
    """
    print(len_line())
    print(msg.center(45))
    print(len_line())

def opc(lista):
    """

    :param lista: Lista do menu de opções dada pelo usuario.
    :return: Opções com a lista disponiveis.
    """
    cont = 1
    for c in lista:
        print(f'{cont} - {c}')
        cont += 1

def opcoes(result):
    """

    :param result: Valor input de opções, para se digitados .alphanumeric ao inves de um
    .isdigit
    :return: valor inteiro, caso não retirna um erro.
    """
    while True:
        try:
            escolha = int(input(result))
        except:
            print('Escreva um valor válido.')
            continue
        else:
            return escolha


def password_generate(len_paa=8):
    """

    :param len_paa: Tamanho de digitos da senha que será gerada.
    :return: senha dada pelas variaveis letras, numeros, caracteres e option dentro do laço
    de repetição FOR.
    """
    letras = string.ascii_letters
    numeros = string.digits
    caracteres = string.punctuation
    option = letras + numeros + caracteres
    password_v = ''
    for c in range(0, len_paa):
        password = random.choice(option)
        password_v = password_v + password
    return password_v

def adicionearq(arq, email='nãoexiste@gmail.com', rede='não existe', senha = ''):
    """

    :param arq: Nome do arquivo .txt
    :param email: Email que o usuario vai utilizar
    :param rede: Sistema que o usuario vai utilizar para entrar com a senha
    :param senha: Senha gerada de forma automatica
    :param info+: É importante ressaltar que a separação do email, senha e rede tem que ser pelo ';'
    :return: Criação do arquivo dentro do banco .txt
    """
    try:
        a = open(arq, 'at')
    except:
        print('Problemas ao adicionar valores.')

    else:
        try:
            a.write(f'{email};{rede};{senha}\n')
        except:
            print('Erro ao adicionar cadastro.')
        else:
            print(f'Cadastro da senha para o email {email} feito com sucesso.')
            return senha
def leraquivo(nome):
    """

    :param nome: nome do arquivo .txt que o usuario quer ler.
    :return: a lista de emails, redes e senhas.
    """
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao abrir o arquivo.')
    else:
        cabecalho('Sistema de senhas')
        cont = 1
        for linha in a:
            nome = linha.split(';')
            nome[2] = nome[2].replace('\n', '')
            print(f'{cont}) Email: {nome[0]:>30}\n   Rede: {nome[1]:>30}\n   Senha: {nome[2]:>30}\n')
            cont += 1
