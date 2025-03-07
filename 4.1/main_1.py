
def take_params():
    print("Введите коэффициенты a, b и c для уравнения ax^2 + bx + c = 0:")

    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))

    return [a, b, c]



def counting_values(function):
    massive = function

    a = int(massive[0])
    b = int(massive[1])
    c = int(massive[2])

    discriminant = b * b - 4 * a * c

    if discriminant > 0:
        root1 = (-b + discriminant**2) / (2 * a)
        root2 = (-b - discriminant**2) / (2 * a)
        print('Корни уравнения: ', root1, ' и ', root2)

    elif discriminant == 0:
            root = -b / (2 * a)
            print('Единственный корень уравнения: ', root)

    else:
        print("У уравнения нет действительных корней")