from random import randint, sample
def get_numbers_ticket(min, max, quantity):
    ### Инструкция по обработке рандома в диапазоне заданных значений
    min<=quantity<=max
    lottery_numbers = set()

    if 0<min<max<=1000:
        while len(lottery_numbers) != quantity:
            lottery_numbers.add(randint(min, max))
            return(sorted(sample(range(min, max), quantity)))
    else: ValueError