# Implementarea unui joc de X și 0 (Tic Tac Toe) în linie de comandă.
# Acesta trebuie să permită jocul în 2 jucători. La pornirea jocului,
# acesta va cere numele celor acestora și îi va folosi ulterior pe
# parcursul jocului.
#
# Jocul de X si O va fi alcătuit din 3 componente principale:
# 1. Realizarea și desenarea planșei de joc
# 2. Verificarea unui câștigător
# 3. Prelucarea planșei de joc în funcție de inputul de la fiecare dintre
#    cei doi jucători
#
# Mai jos se află un exemplu de planșă. Dacă ai altă idee go for it :D
#   --- --- ---
#
#  | X |   |   |
#
#   --- --- ---
#
#  |   | X |   |
#
#   --- --- ---
#
#  |   |   | O |
#
#   --- --- ---


def display(table):
    print('--- --- ---')
    for i in range(3):
        line = ''
        for j in range(3):
            line += '|'
            line += table[i][j]
            line += '| '
        print(line)
        print('--- --- ---')


def check_win(table):
    if table[0][0] == table[1][1] and table[1][1] == table[2][2]:
        if table[0][0] != ' ':
            return True
    for i in range(3):
        if table[i][0] == table[i][1] and table[i][1] == table[i][2]:
            if table[i][0] != ' ':
                return True
        if table[0][i] == table[1][i] and table[1][i] == table[2][i]:
            if table[0][i] != ' ':
                return True
    return False


def play(table, player, symbol):
    print(player + "'s turn!")
    ok = False
    while not ok:
        input1 = input()
        pos = input1.split()
        if not pos[0].isdigit() or not pos[1].isdigit():
            print('Invalid input! Try again, ' + player + '!')
            continue
        x = int(pos[0])
        y = int(pos[1])
        if x < 0 or x > 2 or y < 0 or y > 2:
            print('Invalid position! Try again, ' + player + '!')
            continue
        if table[x][y] == 'X' or table[x][y] == '0':
            print('Position taken! Try again, ' + player + '!')
            continue
        table[x][y] = symbol[player]
        ok = True

    display(table)
    if check_win(table):
        print(player + ' wins!')
        return True
    return False


def main():
    print('============== Welcome to TIC-TAC-TOE! ================')
    print('Player1 (X), choose a nickname: ')
    player1 = input()
    print('Player2 (0), choose a nickname: ')
    player2 = input()
    symbol = {player1: 'X', player2: '0'}
    table = [[' ' for _j in range(3)] for _i in range(3)]
    finished = False
    while not finished:
        for i in range(2):
            if i == 0:
                finished = play(table, player1, symbol)
            else:
                finished = play(table, player2, symbol)
            if finished:
                break


if __name__ == "__main__":
    main()
