from lib.Arquivo import *
# programa principal

# Nome do arquivo .txt
arq_real = 'listadesenhas.txt'

# Se arquivo não existe, o sistema vai criar na função (arquiche_creating(arq_real)
if not arquiche_true(arq_real):
    arquiche_creating(arq_real)

#menu para escolha
while True:
    cabecalho('Menu de opções')
    # Opções de escolha


    options = opc(['Consultar Senhas', 'Cadastrar novas senhas / redes', 'Sair do cadastro'])
    print(len_line())

    # Escolha da opção pelo usuario
    escolha = opcoes('Digite um valor: ')

    # Option 1
    if escolha == 1:
        # Mostrar as informações referente ao arquivo .txt
        leraquivo(arq_real)


    elif escolha == 2:
        # Gerador de senhas
        cabecalho('Gerador de senhas')
        # Email de registro
        email_real = str(input('Digite seu E-mail: '))
        # Sistema que vai utilizar (Ex: Facebook, Instagram, Twitter, etc...)
        rede_real = str(input('Digite a rede para cadastrar: '))
        # Senha gerada pelo sistema
        senha = input('Digite um valor para digitos da senha: ')
        if senha.isdigit():
            senha = int(senha)
        else:
            print('Erro! Digito Inválido')
        # Adicionando senha - rede - email ao arquivo .txt
        print(f'Sua senha para o {rede_real} é {adicionearq(arq = arq_real, email=email_real, rede=rede_real, senha = password_generate(senha))}')
    elif escolha == 3:
        cabecalho('FIM DO PROGRAMA. ATÉ BREVE.')
        break
    else:
        print('Escreva um valor válido.')