from random import randint

print('Игра "Угадай число"')

upper_bound = 100
comp_num = randint(1, upper_bound)
counter = 0

print(f"Угадайте число от 1 до {upper_bound}: ")

while True:
    try:
        user_num = int(input("Введите Ваш вариант: "))    
        counter += 1
        if user_num == comp_num:
            print(f"Поздравляю, Вы угадали число!\nКоличество попыток: {counter}")
            break
        elif user_num > comp_num:
            print("Ваше число больше загаданного...")
        elif user_num < comp_num:
            print("Ваше число меньше загаданного...")
    except ValueError:
        print("Надо ввести число!")