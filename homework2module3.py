from random import randint, sample
def get_numbers_ticket(min, max, quantity):
    ### Инструкция по обработке рандома в диапазоне заданных значений
    
    lottery_numbers = set()

    if 0<min<max<=1000:
        if min>max:
            return lottery_numbers==""
        if quantity > max - min + 1:
            return lottery_numbers==""
        while len(lottery_numbers) != quantity:
            lottery_numbers.add(randint(min, max))
            return(sorted(sample(range(min, max), quantity)))
    else: ValueError