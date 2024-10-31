import math  # підключення бібліотеки math

def task_integer9():
    try:
        number = int(input("Введіть тризначне число: "))
        if 100 <= number <= 999:
            result = number // 100  # ділення націло для отримання першої цифри
            print(result)
        else:
            print("Число має бути тризначним (100-999)!")
    except ValueError:
        print("Введене значення має бути ЦІЛИМ числом!")
        input("Натисніть Enter для продовження...")


def task2_37():
    try:
        x = float(input("Введіть x = "))
        y = float(input("Введіть y = "))
    except ValueError:
        print("x та y мають бути ЧИСЛАМИ!")
        input("Натисніть Enter для продовження...")
    else:
        try:
            # обчислення чисельника
            numerator = math.log(abs(math.cos(x) - math.cos(y)), math.e)
            # обчислення знаменника
            denominator = 2 * math.log(2, math.e)
            # обчислення результату
            result = numerator / denominator
            print(f"Результат = {result}")
        except (ValueError, ZeroDivisionError):
            print("Помилка обчислення!")
            input("Натисніть Enter для продовження...")


def task_boolean16():
    try:
        number = int(input("Введіть позитивне ціле число: "))
        if number <= 0:
            print("Число має бути позитивним!")
            return
        # перевірка чи є число двозначним (10-99) та парним
        result = (10 <= number <= 99) and (number % 2 == 0)
        print(f"Число є парним двозначним: {result}")
    except ValueError:
        print("Введене значення має бути ЦІЛИМ числом!")
        input("Натисніть Enter для продовження...")


def main():
    while True:
        print("\nОберіть завдання:")
        print("1 - Integer9")
        print("2 - Math37")
        print("3 - Boolean16")
        print("0 - Вихід")

        try:
            task_num = int(input("\nВведіть номер завдання: "))

            if task_num == 0:
                break
            elif task_num == 1:
                task_integer9()
            elif task_num == 2:
                task2_37()
            elif task_num == 3:
                task_boolean16()
            else:
                print("Неправильний номер завдання! Спробуйте ще раз.")

            input("\nНатисніть Enter для продовження...")
        except ValueError:
            print("Помилка! Номер завдання має бути ЦІЛИМ числом!")
            input("\nНатисніть Enter для продовження...")


if __name__ == "__main__":
    main()
