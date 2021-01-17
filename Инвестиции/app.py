import sys
import time

# для ускорения вывода
print = sys.stdout.write
key = lambda x: x[2]


def is_min_less_max(x) -> bool:
    return min(x, key=key)[0] < max(x, key=key)[0]


def calculate_break_points(values: list, n_points=None) -> list:
    n = len(values)
    points = [values[i] for i in range(0, n, n // n_points - 1)]
    return [values.index(i) for i in points]


def calculate_slices(values: list, break_points: list) -> list:
    return [values[break_points[i]:break_points[i + 1]]
            for i in range(len(break_points) - 1)]


def calculate_result(values: list, budget: float, n_points: int) -> tuple:
    start = budget
    # находим точки излома
    break_points = calculate_break_points(values, n_points=n_points)
    slices = calculate_slices(values, break_points)
    # фильтруем подпоследовательности
    filtered = filter(lambda x: is_min_less_max(x), slices)
    filtered = list(filter(lambda x: budget // min(x, key=key)[2], filtered))
    for element in filtered[-k:]:
        minimum = min(element, key=key)[2]
        maximum = max(element, key=key)[2]
        n = budget // minimum
        budget -= n * minimum
        budget += n * maximum
    return budget - start, n_points, filtered


def get_info(data: list, k: int, budget: float, points=(1, 3, 25, 27, 57)):
    assert k >= 0, "Слишком малое кол-во транзакций"
    minimum = min(data, key=key)
    maximum = max(data, key=key)
    if min(data, key=key)[2] <= budget:
        # считаем стартегии при разных точках излома
        results = [calculate_result(data, budget, n_points)
                   for n_points in points]
        best_result = max(results, key=lambda x: x[0])  # берем лучшую
        # берем последние транзакции
        for element in best_result[2][-k:]:
            # вывод в консоль
            minimum = min(element, key=key)
            maximum = max(element, key=key)
            n = budget // minimum[2]
            print(f"Количество: {n}\n")
            print(f"Бюджет: {budget}\n")
            money = n * minimum[2]
            budget -= money
            print("Дата покупки: {:.0f} Время: {:.0f} Бюджет: {:^10.2f} Цена: {:^10.2f}\n" \
                  .format(minimum[0], minimum[1], budget, minimum[2]))
            element = element[element.index(minimum) + 1:element.index(maximum)]
            for i in element:
                print("Дата: {:.0f} Время: {:.0f} Изменение: {:^10.2f}\n" \
                      .format(i[0], i[1], n * i[2] - money))
            budget += n * maximum[2]
            print("Дата продажи: {:.0f} Время: {:.0f} Бюджет: {:^10.2f} Цена: {:^10.2f}\n" \
                  .format(maximum[0], maximum[1], budget, maximum[2]))
            print("\n")
        print(f"Заработали: {best_result[0]}\n")
        return best_result
    print("Недостаточно средств\n")


with open("new.csv", "r") as f:
    records = [[float(value) for value in line.split(",")[1:]]
               for line in f.readlines()[1:]]

k = int(input("Введите кол-во транзакций: "))
total_money = float(input("Введите начальную сумму: "))
t = time.time()
result = get_info(records, k, total_money, range(1, 30))
print(f"RunTime: {round(time.time() - t, 2)}")