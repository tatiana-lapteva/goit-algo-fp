"""
Завдання 6. Жадібні алгоритми та динамічне програмування

Необхідно написати програму на Python, яка використовує два підходи — 
жадібний алгоритм та алгоритм динамічного програмування для розв’язання 
задачі вибору їжі з найбільшою сумарною калорійністю в межах обмеженого бюджету.
"""



def greedy_algorithm(items: dict, budget: int) -> int|dict:
    """ Жадібний алгоритм, який вибирає страви, максимізуючи співвідношення 
    калорій до вартості, не перевищуючи заданий бюджет
    """
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    selected_items = {}
    total_calories = 0
    total_cost = 0
    for item in sorted_items:
        if budget >= item[1]['cost']:
            budget -= item[1]['cost']
            total_calories += item[1]['calories']
            total_cost += item[1]['cost']
            selected_items[item[0]] = item[1]
    return total_cost, total_calories, selected_items


def dynamic_programming(items: dict, budget: int) -> int|dict:
    """ Алгоритм динамічного програмування, який обчислює оптимальний набір 
    страв для максимізації калорійності при заданому бюджеті
    """
    selected_items = {}
    total_calories = 0
    total_cost = 0

    cost = [item['cost'] for item in items.values()]
    calories = [item['calories'] for item in items.values()]
    n = len(items)
    memo = [[0 for w in range(budget + 1)] for i in range(n + 1)]
    for i in range(n + 1):
        for w in range(budget + 1):
            if i == 0 or w == 0:
                memo[i][w] = 0
            elif cost[i - 1] <= w:
                memo[i][w] = max(calories[i - 1] + memo[i - 1][w - cost[i - 1]], memo[i - 1][w])
            else:
                memo[i][w] = memo[i - 1][w]

    res = memo[n][budget]
    
    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res == memo[i - 1][budget]:
            continue
        else:
            item_name = list(items.keys())[i - 1]
            selected_items[item_name] = items[item_name]
            total_calories += items[item_name]['calories']
            total_cost += items[item_name]['cost']

            res = res - calories[i - 1]
            budget -= cost[i - 1]

    return total_cost, total_calories, selected_items


if __name__ == "__main__":

    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }

    budget = 90

    greedy_total_cost, greedy_total_calories, greedy_selected_items = greedy_algorithm(items, budget)

    print("Результати жадібного алгоритма:")
    print(f"Витративши {greedy_total_cost} од. бюджету (решта - {budget - greedy_total_cost}), можливо придбати їжу, загальною калорійністю - {greedy_total_calories}, а саме: ")
    print(greedy_selected_items)


    dynamic_total_cost, dynamic_total_calories, dynamic_selected_items = dynamic_programming(items, budget)
    print("Результати алгоритма динамічного програмування:")
    print(f"Витративши {dynamic_total_cost} од. бюджету (решта - {budget - dynamic_total_cost}), можливо придбати їжу, загальною калорійністю - {dynamic_total_calories}, а саме: ")
    print(dynamic_selected_items)
