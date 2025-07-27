a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
action = input("Введите действие:(+ - * /) ")

match action:
    case "+":
        print(a + b)
    case "-":
        print(a - b)
    case "*":
        print(a * b)
    case "/":
        print(a / b)
input("Конец)")