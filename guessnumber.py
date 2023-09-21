import random
print("Guess number")
print("Я загадал число от 1 до 10. Твоя задача угадать его")
rnd = random.randint(1, 10)
answer = int (input("Угадай число ")  )
if rnd == answer:
    print("Красава, ты угадал")
else:
    print("Ты не угадал. Ответ был ")
    print(rnd)
    