import itertools
import random
from numpy.random import choice

MUT_PROB = 0.01

def route_length(route, matrix):
    l = 0
    for i in range(len(route) - 1):
        l += matrix[route[i]][route[i + 1]]
    l += matrix[route[-1]][route[0]]
    return l


def make_child(p1, p2, splits):
    child = [None] * splits[0] + p2[splits[0]:splits[1]] + [None] * (c - splits[1])
    i = 0
    j = splits[0] + 1
    stop = False
    while not stop:
        if child[i] is not None:
            i += 1
            if i >= c:
                stop = True
            continue
        while not stop:
            if p1[j] in child:
                j += 1
                if j >= c:
                    j = 0
                if j == splits[0] + 1:
                    stop = True
                continue
            child[i] = p1[j]
            break
    return child


def mutate_child(child, prob=MUT_PROB):
    if random.random() < prob:
        splits = list(choice(range(c), size=2, replace=False))
        child[splits[0]], child[splits[1]] = child[splits[1]], child[splits[0]]
        return True
    return False


def make_children(p1, p2):
    while True:
        splits = sorted(list(choice(range(c + 1), size=2, replace=False)))
        if 2 <= splits[1] - splits[0] < c-1:
            break
    c1 = make_child(p1, p2, splits)
    c2 = make_child(p2, p1, splits)
    par1 = ''.join(map(lambda x: str(x + 1), p1[:splits[0]])) + '|' + ''.join(
        map(lambda x: str(x + 1), p1[splits[0]:splits[1]])) + '|' + ''.join(map(lambda x: str(x + 1), p1[splits[1]:]))
    par2 = ''.join(map(lambda x: str(x + 1), p2[:splits[0]])) + '|' + ''.join(
        map(lambda x: str(x + 1), p2[splits[0]:splits[1]])) + '|' + ''.join(map(lambda x: str(x + 1), p2[splits[1]:]))
    ch1 = ''.join(map(lambda x: str(x + 1), c1[:splits[0]])) + '|' + ''.join(
        map(lambda x: str(x + 1), c1[splits[0]:splits[1]])) + '|' + ''.join(map(lambda x: str(x + 1), c1[splits[1]:]))
    ch2 = ''.join(map(lambda x: str(x + 1), c2[:splits[0]])) + '|' + ''.join(
        map(lambda x: str(x + 1), c2[splits[0]:splits[1]])) + '|' + ''.join(map(lambda x: str(x + 1), c2[splits[1]:]))

    for i in range(1, 3):
        print(f"{locals()[f'par{i}']}  | {locals()[f'ch{i}']} | {route_length(locals()[f'c{i}'], matrix)}")
    if mutate_child(c1):
        print("Потомок 1 мутировал: " + ''.join(map(lambda x: str(x + 1), c1)))
    if mutate_child(c2):
        print("Потомок 2 мутировал: " + ''.join(map(lambda x: str(x + 1), c2)))
    return c1, c2


def generation(c, matrix, p, g):
    global first_length, first_average, first_sum, final_length, final_average, final_sum
    og_cities = list(range(c))
    population = sorted([random.sample(og_cities, len(og_cities)) for _ in range(p)], key=lambda route: route_length(route, matrix))
    for i in range(g):
        print(f"Поколение {i + 1}")
        lengths = [route_length(route, matrix) for route in population]
        if (i == 0):
            first_length = lengths[0]
            first_sum = sum(lengths)
            first_average = first_sum / len(lengths)
        probabilities = [1 / length for length in lengths]
        total_probability = sum(probabilities)
        probabilities = [prob / total_probability for prob in probabilities]
        if (i != 0 and i < g - 1):
            print("Код   | Значение целевой функции | Вероятность участия в размножении")
            for i, (code, length, prob) in enumerate(zip(population, lengths, probabilities), 1):
                print(f"{''.join(map(lambda x: str(x + 1), code))} | {length}                       | {prob}")
        else:
            print("Код   | Значение целевой функции")
            for i, (code, length) in enumerate(zip(population, lengths), 1):
                print(f"{''.join(map(lambda x: str(x + 1), code))} | {length}")
        print()

        all_pairs = list(itertools.combinations(range(p), 2))
        pairs = random.sample(all_pairs, p // 2)
        pairs_str = ", ".join([f"({pair[0] + 1}, {pair[1] + 1})" for pair in pairs])
        print(f"Пусть выбраны пары: {pairs_str}")
        print("Родители | Потомки | Значение целевой функции для потомков")
        for j, pair in enumerate(pairs):
            p1 = population[pair[0]]
            p2 = population[pair[1]]
            children = make_children(p1, p2)
            unique_children = []
            for child in children:
                if child not in population:
                    unique_children.append(child)

            population += unique_children
        print()
        population.sort(key=lambda route: route_length(route, matrix))
        population = population[:p]
        print()
    print(f"Финальное поколение")
    lengths = [route_length(route, matrix) for route in population]
    final_length = lengths[0]
    final_sum = sum(lengths)
    final_average = final_sum / len(lengths)
    print("Код   | Значение целевой функции")
    for i, (code, length) in enumerate(zip(population, lengths), 1):
        print(f"{''.join(map(lambda x: str(x + 1), code))} | {length}")
    print()
    return population[0], route_length(population[0], matrix)


if __name__ == "__main__":
    c = 5
    matrix = [[0, 4, 5, 3, 8], [4, 0, 7, 6, 8], [5, 7, 0, 7, 9], [3, 6, 7, 0, 9], [8, 8, 9, 9, 0]]
    p = 4
    g = 3
    print()
    result, length = generation(c, matrix, p, g)
    print(f"Таким образом после {g} итераций значение целевой функции для лучшего решения изменилось c {first_length} на {final_length}, среднее значение изменилось с {first_average} до {final_average}, а общее качество с {first_sum} до {final_sum}.")


