a = float(input())
b = float(input())
c = float(input())
f = b ** 2 - 4 * a * c
if a == 0 and b == 0:
    print('Неверные коэффициенты')
else:
    if a != 0:
        if f > 0:
            print((-b + f ** 0.5) / 2 * a)
            print((-b - f ** 0.5) / 2 * a)
        elif f == 0:
            print(-b / 2 * a)
        else:
            print("Корней не существует")
    else:
        print(-c/b)






