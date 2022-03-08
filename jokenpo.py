#Jogo Jokenpô

from random import randint
from time import sleep, time
import os


global lista
global op

op=1
lista = ['pedra','papel','tesoura']
cores = {'limpa':'\033[m',
         'amarelo':'\033[0;33m',
         'vermelho':'\033[0;31m',
         'verde':'\033[0;32m'}
global rodada
rodada = 1
global vitoria
vitoria = 0
global derrotas
derrotas = 0

    
#Como jogar
def como_jogar():
    os.system('cls')
    print ('\nO jogo Jokenpô também é conhecido como Pedra, papel e tesoura')
    
    print ('{}\n\nREGRAS{}'.format(cores['amarelo'],cores['limpa']))
    print('\nNeste jogo, existem três formas: \n- Pedra (punho fechado), \n- Papel (mão aberta) \n- Tesoura (dedo indicador e médio levantados)')
    print ('\nPedra quebra tesoura, tesoura corta papel e papel encobre a pedra. Duas faces iguais, leva ao empate.')
    print ('\nNo melhor de três são disputadas três rodas, vence quem vencer a maioria delas')
    op = int (input ('\n\n\nPressione 1 para continuar\n '))
    
#Sobre
def sobre():
    os.system('cls')
    print ('\nEste jogo foi desenvolvido por {}Yasmin Souza Camargo{}'.format(cores['amarelo'],cores['limpa']))
    op = int (input ('\n\n\nPressione 1 para continuar\n '))
    
#Jogar contra o computador
def modo_computador():
    global rodada
    global vitoria
    global derrotas
    os.system('cls')
    print ('{}\n\nRODADA {} - Melhor de 3{}'.format(cores['amarelo'],rodada,cores['limpa']))
    print ('\nMODO: Jogador vs Computador')
    sleep(2) 
    os.system('cls')
    print ('{}\n\nRODADA {} - Melhor de 3{}'.format(cores['amarelo'],rodada,cores['limpa']))
    op_computador = lista[randint(0,2)]
    
    while True:
        op_pessoa = int(input('\n\n 0 - PEDRA\n 1 - PAPEL \n 2 - TESOURA\n\n Jogador escolha uma opção: '))
        if (op_pessoa==0 or op_pessoa==1 or op_pessoa==2):
            op_pessoa = lista[op_pessoa]
            break
        else:
            print ('\n\n!!! OPÇÃO INVÁLIDA !!!')
            print ('Tente novamente')
    
    os.system('cls')
    print ('{}\n\nRODADA {} - Melhor de 3{}'.format(cores['amarelo'],rodada,cores['limpa']))

    print ('\n\nJO')
    sleep(1)
    print ('KEN')
    sleep(1)
    print ('PO!!\n\n')
    sleep(0.5)
    os.system('cls')
    print ('{}\n\nRODADA {} - Melhor de 3{}'.format(cores['amarelo'],rodada,cores['limpa']))
    
    if (op_pessoa == op_computador):
        while True:  
            os.system('cls')
            print ('{}\n\nRODADA {} - Melhor de 3{}'.format(cores['amarelo'],rodada,cores['limpa']))
            print('\n\nEmpate...')
            print ('Vamos tentar novamente')
            op_pessoa = int(input('\n\n 0 - PEDRA\n 1 - PAPEL \n 2 - TESOURA\n\n Jogador escolha uma opção: '))
            op_pessoa = lista[op_pessoa]
            op_computador = lista[randint(0,2)]
            print ('\n\nJO')
            sleep(1)
            print ('KEN')
            sleep(1)
            print ('PO!!\n\n')
            sleep(0.5)
            os.system('cls')
            print ('{}\n\nRODADA {} - Melhor de 3{}'.format(cores['amarelo'],rodada,cores['limpa']))
            if (op_computador!=op_pessoa):
                break

    if (op_computador=='pedra' and op_pessoa=='papel'):
        print('\n\n  {:=^20}\n'.format(' VOCÊ VENCEU!! '))
        vitoria+=1
    elif (op_computador=='pedra' and op_pessoa=='tesoura'):
        print('\n\n  {:=^20}\n'.format(' O COMPUTADOR VENCEU! '))
        derrotas+=1
        
    elif (op_computador=='papel' and op_pessoa=='pedra'):
        print('\n\n  {:=^20}\n'.format(' O COMPUTADOR VENCEU! '))
        derrotas+=1
    elif (op_computador=='papel' and op_pessoa=='tesoura'):
        print('\n\n  {:=^20}\n'.format(' VOCÊ VENCEU!! '))
        vitoria+=1
    
    elif (op_computador=='tesoura' and op_pessoa=='pedra'):
        print('\n\n  {:=^20}\n'.format(' VOCÊ VENCEU!! '))
        vitoria+=1
    elif (op_computador=='tesoura' and op_pessoa=='papel'):
        print('\n\n  {:=^20}\n'.format(' O COMPUTADOR VENCEU! '))
        derrotas+=1
        
    print('{}'.format('-'*46))
    print('|   Você escolheu: {:>14} {:>13}'.format(op_pessoa,'|'))
    print ('|   Computador escolheu: {:>8} {:>13}'.format(op_computador,'|'))
    print('{}'.format('-'*46))
    
    if (rodada==3):
        print('\nCalculando resultados ...')
        sleep(2)
        os.system('cls')
        print ('{}\n\nRESUMO DO JOGO\n{}'.format(cores['amarelo'],cores['limpa']))
        print ('    VITÓRIAS DO JOGADOR: {}'.format(vitoria))
        print ('    VITÓRIAS DO COMPUTADOR: {}'.format(derrotas))
        if (vitoria>derrotas):
            print ('\n{}{}\n\nVocê venceu o melhor de três :)\n\n{}{}'.format(cores['verde'],'#'*50, '#'*50,cores['limpa']))
        else:
            print ('\n{}{}\n\nNão foi dessa vez :( O computador venceu o melhor de três\n\n{}{}'.format(cores['vermelho'],'#'*10, '#'*10,cores['limpa']))
        op = int (input ('\n** Deseja jogar novamente? pressione 1\n '))
        if (op==1):
            vitoria=0
            derrotas=0
            rodada=1
            modo_computador()
        else:
            vitoria=0
            derrotas=0
            rodada=1
    else:
        rodada+=1
        op = int (input ('\nPressione 1 para continuar\n '))
        modo_computador()
  
  
##INICIO DO CÓDIGO   
while (op != 5):
    #Menu
    os.system('cls')
    print ('\n {}{} Bem Vindo ao jogo Jokenpô! {}{}'.format('-'*5, cores['amarelo'],cores['limpa'],'-'*5))
    print ('\n    {}1{} - Jogar contra o computador'.format(cores['amarelo'],cores['limpa']))
    print ('    {}2{} - Como jogar'.format(cores['amarelo'],cores['limpa']))
    print ('    {}3{} - Sobre'.format(cores['amarelo'],cores['limpa']))
    print ('    {}4{} - Sair'.format(cores['amarelo'],cores['limpa']))
    op = int (input('\n\nEscolha uma opção: '))

    if (op == 1):
        modo_computador()
    elif (op == 2):
        como_jogar()
    elif (op == 3):
        sobre()
    elif (op == 4):
        print('\n\nObridado por jogar jokenpo')
        sleep (1)
        exit()
    else: 
        print ('\n\n--- OPÇÃO INVÁLIDA ---')
    
    
    
