def main() -> None:
    while True:
        try:
            input_list = [int(i) for i in
                          input('Введите целые числа, разделяя их знаком "пробел": ').split()
                          if (i.isdigit())]
            print(f'Список первоначальных чисел: {input_list}')
        except ValueError:
            pass
        else:
            break
    task_list = input_list.copy()
    for value in input_list:
        if value == 20:
            input_list[(input_list.index(20))] = 200
            break
    print(f"Решение 'Задачи 1' - замена первого вхождения числа 20 на 200: {input_list}")
    print(f"Решение 'Задачи 2' - возведение списка в квадрат: {list(map(lambda x: x ** 2, task_list))}")
    print(f"Решение 'Задачи 2' - выведение списока без чисел '20': {list(filter(lambda x: x != 20, task_list))}")


if __name__ == '__main__':
    main()
