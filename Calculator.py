def calculator():
    print("Калькулятор")
    print("Доступные операции: +, -, *, /")

    try:
        num1 = float(input("Введите первое число: "))
        operator = input("Введите оператор (+, -, *, /): ")
        num2 = float(input("Введите второе число: "))

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                print("Деление на ноль")
                return
            result = num1 / num2
        else:
            print("Неверный оператор!")
            return

        print(f"Результат: {num1} {operator} {num2} = {result}")

    except ValueError:
        print("Ошибка ввода!")


calculator()
