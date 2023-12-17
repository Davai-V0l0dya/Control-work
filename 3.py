def distribute_production(equally: int, production: int) -> int:
    """
    Генератор, который делит количество продукции максимально поровну на склады.

    equally: Количество складов
    production: Общее количество продукции
    yield: Количество продукции для каждого склада
    """
    base_amount = production // equally  # Базовое количество продукции для каждого склада
    remainder = production % equally  # Остаток после равномерного распределения

    for _ in range(equally):
        if remainder > 0:
            yield base_amount + 1  # Добавляем к базовому значению по одной единице, пока есть остаток
            remainder -= 1
        else:
            yield base_amount

# Пример использования
total_production = 5
number_of_warehouses = 3

for amount in distribute_production(number_of_warehouses, total_production):
    print(amount)