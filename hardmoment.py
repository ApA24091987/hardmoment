def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for num in numbers:
        try:
            result += num
        except TypeError:
            print(f'Некорректный тип данных для подсчета суммы - {num}')
            incorrect_data += 1
    return result, incorrect_data


def calculate_average(numbers):
    try:
        if not isinstance(numbers, (list, tuple, set)):
            print('В numbers записан некорректный тип данных')
            return None
        if len(numbers) == 0:
            return  0
        total, incorrect_data = personal_sum(numbers)
        if total == 0 and incorrect_data == len(numbers):
            return  0
        return total /  len([num for num in numbers if isinstance(num, (int, float))])
    except ZeroDivisionError:
        return 0


print(f'Результат 1: {calculate_average('1, 2,3')}' )
print(f'Результат 2: {calculate_average([1,'Строкаю', 3, 'Еще Строка'])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 12])}')




