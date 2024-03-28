__all__ = ['riddle', 'storage', 'show_results']

_data = {}

def riddle(riddle_text: str, answer: list[str], count: int = 3) -> int:
    print(f'Отгадай загадку:\n{riddle_text}')
    for nn in range(1, count + 1):
        ans = input(f'Попытка №{nn}: ').lower()
        if ans in answer:
            return nn
    return 0


def save_result(puzzle: str, nn: int) -> None:
    _data[puzzle] = nn # ключ - значение словаря

def show_results():
    res = (f'Загадку "{puzzle}" разгадали с {nn}й попытки' if nn > 0
           else f'Загадку "{puzzle}" не разгадали'
           for puzzle, nn in _data.items())
    print(*res, sep='\n')


def storage():
    puzzles = {
        'Зимой и летом одним цветом': ['ёлка', 'ель', 'сосна'],
        'Сидит дед во сто шуб одет': ['лук', 'луковица'],
        'Не лает не кусает в дом не пускает': ['замок']
    }
    for puzzle, answer in puzzles.items():
        result = riddle(puzzle, answer)
        print(f'Угадал с {result}й попытки!' if result > 0 else 'Не угадал :(')
        save_result(puzzle, result)

if __name__ == '__main__':
    storage()
    show_results()