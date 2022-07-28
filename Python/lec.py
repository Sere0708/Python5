# 1. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) (доп) Подумайте как наделить бота ""интеллектом""



# вариант человек против человека:
# from random import randint

# def input_dat(name):
    # x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    # while x < 1 or x > 28:
        # x = int(input(f"{name}, введите корректное количество конфет: "))
    # return x


# def p_print(name, k, counter, value):
    # print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")

# player1 = input("Введите имя первого игрока: ")
# player2 = input("Введите имя второго игрока: ")
# value = int(input("Введите количество конфет на столе: "))
# flag = randint(0,2) # флаг очередности
# if flag:
    # print(f"Первый ходит {player1}")
# else:
    # print(f"Первый ходит {player2}")

# counter1 = 0 
# counter2 = 0

# while value > 28:
    # if flag:
        # k = input_dat(player1)
        # counter1 += k
        # value -= k
        # flag = False
        # p_print(player1, k, counter1, value)
    # else:
        # k = input_dat(player2)
        # counter2 += k
        # value -= k
        # flag = True
        # p_print(player2, k, counter2, value)

# if flag:
    # print(f"Выиграл {player1}")
# else:
    # print(f"Выиграл {player2}")






# 2. Создайте программу для игры в ""Крестики-нолики"".


# from random import randint
# BOARD_SIZE = 3
# board = [i for i in range(9)]
# is_winner = False
# current_player = randint(0, 1)
# markers = {0: 'O', 1: 'X'}
# available_turns = (x for x in range(9))
  # Отрисовка поля
  # Старт игры, запрос ввода (если валидация == False, exception)
  # Валидация ввода
  # Переопределяем значения списка по индексу
  # Проверка на победителя
  # Переключаем игрока

# def draw_board():
    # res = ""
    # for i, v in enumerate(board):
        # res += str(v) + " "
        # if (i+1) % BOARD_SIZE == 0:
            #  res += "\n"
    # print(res)

# def validate(value = " "):
    # if not value.isdigit() and int(value) not in available_turns:
        # raise ValueError ("Enter valid value and try again")
    # if board[int(value)] in ('X', 'O'):
        # raise ValueError ("This value has already played")
    # if '.' in value:
        # raise ValueError('Number must be int')

# def check_winner():
    # current_marker = markers[current_player]
    # if board[0] == current_marker and board[4] == current_marker and board[8] == current_marker or \
            # board[2] == current_marker and board[4] == current_marker and board[6] == current_marker or \
            # board[0] == current_marker and board[1] == current_marker and board[2] == current_marker or \
            # board[3] == current_marker and board[4] == current_marker and board[5] == current_marker or \
            # board[6] == current_marker and board[7] == current_marker and board[8] == current_marker or \
            # board[0] == current_marker and board[3] == current_marker and board[6] == current_marker or \
            # board[1] == current_marker and board[4] == current_marker and board[7] == current_marker or \
            # board[2] == current_marker and board[5] == current_marker and board[8] == current_marker:
        # return True
    # else:
        # return False

# for i in range(9):
    # try:
        # input_error = True
        # draw_board()
        # while input_error:
            # choice = input(f"Pllayer {markers[current_player]} enter your number Введите число:\n")
            # validate(choice)
            # input_error = False
        # board[int(choice)] = markers[current_player]
             #проверить победителя
        # is_winner = check_winner()
        # if is_winner == True:
            # print(f'Player {markers[current_player]} won the game!!')
            # break
        # current_player = 0 if current_player == 1 else 1
        # if is_winner == True:
    # except ValueError as ex:
        # print(ex)

# if is_winner == False:
    # print('Draw')



    


# 3. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.



# def coding(txt):
    # count = 1
    # res = ''
    # for i in range(len(txt)-1):
        # if txt[i] == txt[i+1]:
            # count += 1
        # else:
            # res = res + str(count) + txt[i]
            # count = 1
    # if count > 1 or (txt[len(txt)-2] != txt[-1]):
        # res = res + str(count) + txt[-1]
    # return res

# def decoding(txt):
    # number = ''
    # res = ''
    # for i in range(len(txt)):
        # if not txt[i].isalpha():
            # number += txt[i]
        # else:
            # res = res + txt[i] * int(number)
            # number = ''
    # return res


# s = input("Введите текст для кодировки: ")
# print(f"Текст после кодировки: {coding(s)}")
# print(f"Текст после дешифровки: {decoding(coding(s))}")



