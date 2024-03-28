# __all__ = ['guess']

from random import randint

def guess(lower: int = 0, upper: int = 100, count: int = 10) -> bool:
    number = randint(lower, upper)
    for nn in range(1, count + 1):
        answer = int(input(f'Попытка №{nn}, введите число между {lower} и {upper}: '))
        if answer > number:
            print(f'число {answer} больше загаданного')
        elif answer < number:
            print(f'число {answer} меньше загаданного')
        else:
            return True
            # print("OK")
    return False

if __name__ == '__main__':
    print(guess())