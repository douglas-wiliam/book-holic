from operator import mod


def func(x, y):
    if y == 0:
        return x
    else:
        return func(y, x % y)


resultado = func(9, 3)

print("O RESULTADO DE func(9,3) É ", resultado)
