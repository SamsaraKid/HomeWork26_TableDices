# Верхняя строка
print(u'\u2554', end='')

for i in range(207):
    print(u'\u2550', end='')

print(u'\u2557')

# Строка с множителями
print(u'\u2551', '\t', sep='', end='\t')

for i in range(1, 11):
    print(u'\u2502', f'\t\t{i}\t\t', sep='', end='\t')

print(u'\u2551')

# Строка-разделитель
def divider():
    print(u'\u255F', u'\u2500', u'\u2500', u'\u2500', u'\u2500', u'\u2500', u'\u2500', u'\u2500', sep='', end='')
    for i in range(10):
        print(u'\u253C', sep='', end='')
        for k in range(19):
            print(u'\u2500', sep='', end='')
    print(u'\u2562')

# Основная таблица
for i in range(1, 11):
    if i == 10:
        space = ''
    else:
        space = ' '
    divider()
    print(u'\u2551', f'\t{i}\t', sep='', end='')
    for k in range(1, 11):
        print(u'\u2502', '\t %s%d * %d = %d ' % (space, i, k, i*k), sep='', end='\t')
    print(u'\u2551')


# Нижняя строка
print(u'\u255A', end='')

for i in range(207):
    print(u'\u2550', end='')

print(u'\u255D')


# Игра в кубики
from random import randint

dices = ('╭─────────╮\n│         │\n│    ●    │\n│         │\n╰─────────╯',
         '╭─────────╮\n│       ● │\n│         │\n│ ●       │\n╰─────────╯',
         '╭─────────╮\n│       ● │\n│    ●    │\n│ ●       │\n╰─────────╯',
         '╭─────────╮\n│ ●     ● │\n│         │\n│ ●     ● │\n╰─────────╯',
         '╭─────────╮\n│ ●     ● │\n│    ●    │\n│ ●     ● │\n╰─────────╯',
         '╭─────────╮\n│ ●     ● │\n│ ●     ● │\n│ ●     ● │\n╰─────────╯')

print('Игра в кубики. Первый игрок бросает два кубика пока не выпадут одинаковые числа. Потом второй игрок делает то же самое. Выигрывает тот у кого числа на кубиках больше')

def dice():
    i = randint(0, 5)
    j = randint(0, 5)
    print(dices[i])
    print(dices[j])
    return i, j

first = 0
second = 0
exit = False
while True:
    while True:
        ans = input('Ход первого игрока. Бросить кубики? (Чтобы бросить нажмите Enter. Для завершения игры введите любой символ):\n')
        if ans == '':
            i, j = dice()
            if i == j:
                first = i
                break
        else:
            exit = True
            break
    if exit:
        break
    while True:
        ans = input(f'У первого игрока выпало {first + 1}. Ход второго игрока. Бросить кубики? (Чтобы бросить нажмите Enter. Для завершения игры введите любой символ):\n')
        if ans == '':
            i, j = dice()
            if i == j:
                second = i
                break
        else:
            exit = True
            break
    if exit:
        break
    if first > second:
        print(f'Победил первый игрок ({first + 1} > {second + 1}).', end=' ')
    elif first < second:
        print(f'Победил второй игрок ({first + 1} < {second + 1}).', end=' ')
    else:
        print('Ничья.', end=' ')
    ans = input('Играть заново? (Чтобы играть заново нажмите Enter. Для завершения игры введите любой символ):\n')
    if ans == '':
        i = 0
        j = 0
    else:
        break

