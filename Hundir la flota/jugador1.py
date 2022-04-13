import computadora
import time

def jugador1(tablerojugador, tablerocomputadora, tablerovacio1, tablerovacio2):
    while 'O' in tablerojugador and 'O' in tablerocomputadora:
        try:
            print('Tablero de la computadora\n', tablerovacio1)
            x=int(input('PLAYER 1, Introdruce la coordenada X: '))
            if x < 0 or x > 9:
                print('Coordenada recibida errónea, introduce valores entre 0 y 9')
                continue
            y=int(input('PLAYER 1, Introdruce la coordenada Y: '))
            if y < 0 or y > 9:
                print('Coordenada recibida errónea, introduce valores entre 0 y 9')
                continue

            if tablerojugador[x,y] == 'O':
                tablerojugador [x,y] = 'X'
                tablerovacio1[x,y] = 'X'
                print(f'¡TOCADO en {x},{y}!', tablerovacio1)
                continue
            elif tablerojugador[x,y] == ' ':
                tablerojugador[x,y] = '-'
                tablerovacio1[x,y] = '-'
                print(f'¡Agua en {x},{y}!', tablerovacio1)
                time.sleep(5)
                computadora.computadora(tablerojugador,tablerocomputadora,tablerovacio1,tablerovacio2)

            else:
                print('Try again player!')
                continue
        except:
            print('Error')
            continue