from random import randint, sample
def get_numbers_ticket(min, max, quantity):
    # Проверка корректности заданых значений
    if 0 < min < max <= 1000:
        if 0 < quantity <= max - min + 1:
            # Генерация уникальных случайных чисел
            lottery_numbers = set()
            while len(lottery_numbers) < quantity:
                lottery_numbers.add(randint(min, max))
            return sorted(sample(list(lottery_numbers), quantity))
    return []