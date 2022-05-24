import math
import matplotlib.pyplot as plt


def f(x):
    return x ** 3 - 3 * x ** 2 + 2 * x + 5


# dérivée de f
def f_deriv(x):
    return 3 * x ** 2 - 6 * x + 2


def balayage_pas_constant(a, b, n, f, mini):
    dx = (b - a) / n
    extremum = f(a)
    for i in range(1, n):
        x = a + i * dx
        y = f(x)
        if y < extremum and mini or y > extremum and not mini:
            extremum = y

    return extremum


def balayage_pas_constant_err(a, b, n, f, exact):
    dx = (b - a) / n
    min = f(a)
    for i in range(1, n):
        x = a + i * dx
        y = f(x)
        if y < min:
            min = y
    return abs(min - exact)


def gradient1D(f, x0, f_deriv, u, epsilon):
    xn = x0
    der = f_deriv(xn)
    end = 100000
    while not (epsilon > der > - epsilon) and end >0:
        xn = xn + u * f_deriv(xn)
        der = f_deriv(xn)
        end -= 1
    return f(xn)


def methode_pas_constant():
    n_list = [i for i in range(10, 1000)]
    err_list = []

    maxi_exact = 5 + 2 / (3 * math.sqrt(3))
    print("minimum : exact =", min_exact, " ; calc =", balayage_pas_constant(0, 3, 100, f, True))
    print("maximum : exact =", maxi_exact, " ; calc =", balayage_pas_constant(0, 1, 100, f, False))

    for n in n_list:
        err_list.append(balayage_pas_constant_err(0, 3, n, f, min_exact))

    plt.plot(n_list, err_list)
    plt.title("erreur pas constant")
    plt.xlabel("n")
    plt.ylabel("erreur")
    plt.savefig("Erreur_balayage_pas_constant.png")
    plt.clf()


if __name__ == "__main__":
    # question 1 / 2 / 3 / 4
    min_exact = 5 - 2 / (3 * math.sqrt(3))
    methode_pas_constant()

    # question 6
    print("\n------ Gradient1D ---------\n")
    mini = gradient1D(f, 1.5, f_deriv, -0.001, 0.001)
    print("minimum : exact =", min_exact, " ; calc =", mini)
    print("erreur :", abs(min_exact - mini))
