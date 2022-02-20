import os
from time import sleep
import mysql.connector as msqlc
banco = msqlc.connect(
    host='localhost',
    user='root',
    password='',
    database='times'
)

cursor = banco.cursor()

todostimes = []

def MostrarTimes():
    print('-=-'*20)
    print('SERIE A'.center(60))
    print('')
    comandoSQL = 'show tables'
    cursor.execute(comandoSQL)
    times = cursor.fetchall()
    for cont in range(0, len(times)):
        for time in times[cont]:
            print(time.center(60).upper().replace("_", ' '))
    print('-=-'*20)


def TimesCadastrados():
    comandoSQL = 'show tables'
    cursor.execute(comandoSQL)
    times = cursor.fetchall()
    for cont in range(0, len(times)):
        for time in times[cont]:
            if time not in todostimes:
                todostimes.append(time)
    return todostimes


def TimesComJogadores():
    timecomjogador = []
    comandoSQL = 'show tables'
    cursor.execute(comandoSQL)
    times = cursor.fetchall()
    for cont in range(0, len(times)):
        for time in times[cont]:
            if time not in todostimes:
                todostimes.append(time)
    for time in todostimes:
        comandoSQL = f'select * from {time}'
        cursor.execute(comandoSQL)
        temjogador = cursor.fetchall()
        if len(temjogador) > 0:
            timecomjogador.append(time)
    print('-=-'*20)
    print('TIMES COM JOGADORES'.center(60))
    for time in timecomjogador:
        print(time.replace('_', ' ').title().center(60))
    print('-=-'*20)


os.system('cls')

while True:
    MostrarTimes()
    print('PARA CADASTRAR NOVOS TIMES DIGITE [A], PARA VER JOGADOR DE UM TIME DIGITE [G]')
    print('ADICIONAR JOGADORES A UM TIME [J], SAIR DIGITE [L] ')
    resp1 = str(input('')).strip().lower()
    if resp1 == 'a':
        while True:
            novotime = str(input('Nome do time: ')).lower().strip()
            novotime2 = novotime.replace(' ', '_')
            lista = TimesCadastrados()
            if novotime2 not in lista:
                cursor.execute(f"CREATE TABLE {novotime2} (nome VARCHAR(255), idade INT(3), pos VARCHAR(255))")
                lista.clear()
                print(f'{(novotime).upper()} ADICIONADO COM SUCESSO!!!')
                sleep(4)
                os.system('cls')
                break
            else:
                print('ERRO! tente novamente')
    elif resp1 == 'j':
        while True:
            time = str(input('Digite o nome do time para fazer a adição: ')).strip().lower().replace(' ', '_')
            lista =TimesCadastrados()
            if time in lista:
                comandoSQL = f'INSERT INTO {time} (nome, idade, pos) VALUES (%s, %s, %s)'
                nome = str(input('Digite o nome do jogador: '))
                idade = str(input('A idade: '))
                posi = str(input('Posição: '))
                dados = (nome, idade, posi)
                cursor.execute(comandoSQL, dados)
                print(f'{(nome).upper()} ADICIONADO!!!')
                lista.clear()
                sleep(4)
                break
            else:
                print('ERRO! TIME INVÁLIDO')
    elif resp1 == 'g':
        while True:
            TimesComJogadores()
            time2 = str(input('Digite o nome do time para visualizar os jogadores cadastrados: ')).strip().lower().replace(' ', '_')
            lista = TimesCadastrados()
            if time2 in lista:
                comandoSQL = f'select * from {time2}'
                cursor.execute(comandoSQL)
                jogadores = cursor.fetchall()
                if len(jogadores) > 0:
                    for conta in range(0, len(jogadores)):
                        jogador = (jogadores[conta])
                        print(f'\nNome: {(jogador[0]).title()}; Idade: {jogador[1]}; Posição: {(jogador[2]).upper()}')
                    sleep(len(jogadores)*5)
                    os.system('cls')
                    break
                else:
                    print('SEM JOGADORES CADASTRADOS NESSE TIME!')
            else:
                print('ERRO! TIME INVALIDO')
                sleep(3)
                os.system('cls')
    elif resp1 == 'l':
        break
    else:
        os.system('cls')
        print('ERRO!')
