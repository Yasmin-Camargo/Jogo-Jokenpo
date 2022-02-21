#Jogo Jokenpô

from random import randint
from time import sleep

print ('\n {} Bem Vindo ao jogo Jokenpô! {}'.format('-'*5, '-'*5))
op_pessoa = int(input('\n\nEscolha uma opção:\n 0 - PEDRA\n 1 - PAPEL \n 2 - TESOURA\n'))

if (op_pessoa!=0 and op_pessoa!=1 and op_pessoa!=2):
    print ('\n\n!! OPÇÃO INÁLIDA !!\nTente novamente!')
    exit()

lista = ['pedra', 'papel', 'tesoura']
op_computador = randint(0,2)

print ('\n\nJO')
sleep(1)
print ('KEN')
sleep(1)
print ('PO!!\n\n')

print('{}'.format('-'*46))
print('|   Você escolheu: {:>14} {:>13}'.format(lista[op_pessoa],'|'))
print ('|   Computador escolheu: {:>8} {:>13}'.format(lista[op_computador],'|'))
print('{}'.format('-'*46))

if (op_computador==0 and op_pessoa==0):
    print('\n\n  {:=^20}\n\n'.format(' EMPATE! '))
elif (op_computador==0 and op_pessoa==1):
    print('\n\n  {:=^20}\n\n'.format(' VOCÊ VENCEU!! '))
elif (op_computador==0 and op_pessoa==2):
    print('\n\n  {:=^20}\n\n'.format(' O COMPUTADOR VENCEU! '))
    
elif (op_computador==1 and op_pessoa==0):
    print('\n\n  {:=^20}\n\n'.format(' O COMPUTADOR VENCEU! '))
elif (op_computador==1 and op_pessoa==1):
    print('\n\n  {:=^20}\n\n'.format(' EMPATE! '))
elif (op_computador==1 and op_pessoa==2):
    print('\n\n  {:=^20}\n\n'.format(' VOCÊ VENCEU!! '))
   
elif (op_computador==2 and op_pessoa==0):
    print('\n\n  {:=^20}\n\n'.format(' VOCÊ VENCEU!! '))
elif (op_computador==2 and op_pessoa==1):
    print('\n\n  {:=^20}\n\n'.format(' O COMPUTADOR VENCEU! '))
elif (op_computador==2 and op_pessoa==2):
    print('\n\n  {:=^20}\n\n'.format(' EMPATE! '))
    
else:
    print ('\n\nJogada Inválida!!!')

