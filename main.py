from random import randint


def print_current_attempt(current_attempt: dict) -> None:
    print(f'Текущая попытка. Осталось попыток {6 - attempts_counter}')
    for letter in range(5):
        print(current_attempt.get(letter)[1], end='')
    print()
    for letter in range(5):
        print(current_attempt.get(letter)[0], end='')
    print()


with open('russian.txt', encoding='cp1251') as file:
    words_list = list(filter(lambda x: len(x) == 5, file.read().lower().split()))

guessed = False
attempts_counter = 0
right_word = words_list[randint(0, len(words_list) - 1)]
current_attempt = {}

print('Ваша задача - за 6 попыток отгадать слово из 5 букв, удачи!')
while attempts_counter != 6:
    user_word = input("Введите слово: ").lower()
    if not(user_word.isalpha()):
        print('Я сказал - слово!')
    else:
        if len(user_word) != 5:
            print('Длина слова должна быть 5 букв!')
            continue
        elif user_word not in words_list:
            print('Такого слова нет в списке!')
            continue
        else:
            attempts_counter += 1
            if user_word == right_word:
                guessed = True
                break
            for i in range(len(user_word)):
                if user_word[i] in right_word:
                    if user_word[i] == right_word[i]:
                        current_attempt[i] = (user_word[i], 'R')
                    else:
                        current_attempt[i] = (user_word[i], 'Y')
                else:
                    current_attempt[i] = (user_word[i], 'B')
            print_current_attempt(current_attempt)
            current_attempt.clear()
if guessed:
    print(f'Вы угадали, ушло попыток - {attempts_counter}')
else:
    print(f'К сожалению у вас не получилось. Загаданное слово - {right_word}')
