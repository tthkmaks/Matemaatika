from random import *

print("Welcome to quiz!")
print("Сейчас будем тестировать ваш мозг!))")
level = int(input("Уровень сложности (Tase 1, Tase 2, Tase 3): "))
primer = int(input("Введите количество примеров: "))
vopros = 0
while primer > 0:
    num1 = randint(1, 10**level)
    num2 = randint(1, 10**level)
    operator = choice(['+', '-', '*', '/'])
    q = f"{num1} {operator} {num2} = "
    user_vopros = float(input(q))
    if operator == '+':
        correct_answer = num1 + num2
    elif operator == '-':
        correct_answer = num1 - num2
    elif operator == '*':
        correct_answer = num1 * num2
    elif operator == '/':
        correct_answer = num1 / num2
    
    if user_vopros == correct_answer:
        print("Правильно!")
        vopros += 1
    else:
        print("Неправильно!")
        primer -= 1  
ocenka = (vopros / (primer + vopros)) * 100
print("Оценка:")
if ocenka < 60:
    print("Hinne 2")
elif 60 <= ocenka < 75:
    print("Hinne 3")
elif 75 <= ocenka < 90:
    print("Hinne 4")
else:
    print("Hinne 5")



