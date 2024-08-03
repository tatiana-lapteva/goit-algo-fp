"""
Завдання 7. Використання методу Монте-Карло
Створіть симуляцію, де два кубики кидаються велику кількість разів. 
Для кожного кидка визначте суму чисел, які випали на обох кубиках. 
Підрахуйте, скільки разів кожна можлива сума (від 2 до 12) з’являється у процесі симуляції. 
Використовуючи ці дані, обчисліть імовірність кожної суми.
На основі проведених імітацій створіть таблицю або графік, який відображає ймовірності 
кожної суми, виявлені за допомогою методу Монте-Карло.
"""

import random

def monte_carlo_simulation(a, b, num_experiments):

    roll_data = {}
    for i in range(2, 13):
        roll_data[i] = 0

    for i in range(num_experiments):
        dice_1 = random.randint(a, b)
        dice_2 = random.randint(a, b)
        roll_sum = dice_1 + dice_2

        roll_data[roll_sum] += 1  

    print("Результат Методу Монте Карло")
    print("Cума:\tЙмовірність")
    for key, value in roll_data.items():
        print(f"{key} \t {value/num_experiments:.2%}")


if __name__ == "__main__":

    num_experiments = 10**5
    monte_carlo_simulation(1, 6, num_experiments)