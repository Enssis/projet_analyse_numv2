import math

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from vect import vector


def g(a, b, x, y):
    return x ** 2 / a + y ** 2 / b


# retourne la fonction g avec les paramètres a et b voulus
def fun_g(a, b):
    return lambda x, y: x ** 2 / a + y ** 2 / b


def h(x, y):
    return np.cos(x) * np.sin(y)


def grad_g(a, b, x, y):
    return vector(2 * x / a, 2 * y / b)


# retourne la fonction gradient g avec les paramètres a et b voulus
def fun_grad_g(a, b):
    return lambda x, y: vector(2 * x / a, 2 * y / b)


def grad_h(x, y):
    return vector(np.sin(x) * np.sin(y), np.cos(x) * np.cos(y))


# question 5
def gradpc(eps, m, u, x0, y0, grad):
    vects = [vector(x0, y0)]
    for i in range(m):
        vn = vects[i]
        v = vn + vector(u, u) * grad(vn.x, vn.y)
        vects.append(v)
        if grad(vn.x, vn.y).norm() < eps:
            break
    return vects


def grada(eps, m, u, x0, y0, f, grad, maximum):
    vects = [vector(x0, y0)]
    if maximum: u = -u
    for i in range(m):
        vn = vects[i]
        k = 200
        for j in range(1, 200):
            vf1 = vn + vector(j * u, j * u) * grad(vn.x, vn.y)
            f1 = f(vf1.x, vf1.y)
            vf2 = vn + vector((j + 1) * u, (j + 1) * u) * grad(vn.x, vn.y)
            f2 = f(vf2.x, vf2.y)
            if f2 >= f1:  # and maximum or f2 >= f1 and not maximum:
                k = j
                break

        v = vn + vector(k * u, k * u) * grad(vn.x, vn.y)
        vects.append(v)
        if grad(vn.x, vn.y).norm() < eps:
            break
    return vects


# question 8
def gradamax(eps, m, u, x0, y0, f, grad):
    return grada(eps, m, u, x0, y0, f, grad, True)


# question 9
def gradamin(eps, m, u, x0, y0, f, grad):
    return grada(eps, m, u, x0, y0, f, grad, False)


def graphe_3d(fun, name):
    list_x = np.linspace(-10, 10, 100)
    list_y = np.linspace(-10, 10, 100)
    list_x, list_y = np.meshgrid(list_x, list_y)
    list_z = fun(list_x, list_y)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(list_x, list_y, list_z)
    plt.title("{0}(x,y)".format(name))
    plt.xlabel("x")
    plt.ylabel("y")
    plt.savefig("Partie C/graph {0}.png".format(name))
    ax.clear()
    plt.clf()


def lignes_de_niveau(fun, name):
    list_x = np.linspace(-10, 10, 100)
    list_y = np.linspace(-10, 10, 100)
    list_x, list_y = np.meshgrid(list_x, list_y)
    list_z = fun(list_x, list_y)
    CS = plt.contour(list_x, list_y, list_z)
    plt.clabel(CS, inline=1, fontsize=10)
    plt.title("Lignes de niveau de {0}(x,y)".format(name))
    plt.savefig("Partie C/graph ligne de niveaux {0}.png".format(name))
    plt.clf()


def iterations(fun_grad, name, x0, y0):
    gradpc_fun = gradpc(10 ** -6, 300, -0.2, x0, y0, fun_grad)
    iterations = [i for i in range(len(gradpc_fun))]
    plt.plot(iterations, [v.x for v in gradpc_fun], label="xn de {0}".format(name))
    plt.plot(iterations, [v.y for v in gradpc_fun], label="yn de {0}".format(name))
    plt.xlabel("n")
    plt.legend()
    plt.title("itérations de gradpc pour {0}".format(name))
    plt.savefig("Partie C/itérations de gradpc pour {0}.png".format(name))
    plt.clf()


def erreur_relative():
    u = [-i / 1000 for i in range(1, 999, 10)]
    e = []
    for i in u:
        gradpc_g = gradpc(10 ** -5, 120, i, 5, 5, fun_grad_g(1, 20))
        e.append(gradpc_g[len(gradpc_g) - 1].norm())
    plt.plot([i for i in u], [j for j in e], label="erreur de g")
    plt.legend()
    plt.xlabel("u")
    plt.title("erreur relative de g1,20")
    plt.savefig("Partie C/erreur relative de g1,20.png")
    plt.clf()


def nombre_iterations():
    u = [-i / 1000 for i in range(1, 999, 10)]
    nb_pc = []
    nb_amin = []
    for i in u:
        gradpc_g = gradpc(10 ** -5, 200, i, 5, 5, fun_grad_g(1, 20))
        nb_pc.append(len(gradpc_g))
        gradamin_g = gradamin(10 ** -5, 200, i, 5, 5, fun_g(1, 20), fun_grad_g(1, 20))
        nb_amin.append(len(gradamin_g))
    plt.plot([i for i in u], [j for j in nb_pc], label="gradpc")
    plt.plot([i for i in u], [j for j in nb_amin], label="gradamin")
    plt.legend()
    plt.xlabel("u")
    plt.ylabel("iterations")
    plt.title("difference de méthode pour le min de g1,20")
    plt.savefig("Partie C/difference de méthode pour le min de g1,20.png")
    plt.clf()


if __name__ == "__main__":
    graphe_3d(fun_g(2, 2 / 7), "g2,2|7")
    graphe_3d(h, "h")
    lignes_de_niveau(fun_g(2, 2 / 7), "g2,2|7")
    lignes_de_niveau(h, "h")

    print("normes de gradient de g(2,2/7)")
    print(grad_g(2, 2 / 7, 1, 1).norm())
    print(grad_g(2, 2 / 7, 3, 7).norm())
    print(grad_g(2, 2 / 7, 5, 5).norm())

    print("\nnormes de gradient de h")
    print(grad_h(1, 1).norm())
    print(grad_h(3, 7).norm())
    print(grad_h(5, 5).norm())
    print("\n")

    iterations(fun_grad_g(2, 2 / 7), "g2,2|7", 7, 1.5)
    iterations(grad_h, "h", 0, 0)
    erreur_relative()
    lignes_de_niveau(fun_g(1, 20), "g1,20")
    print("iterations pour gradamin et gradamax :")
    print([str(v) for v in gradamin(10 ** -6, 300, -0.5, 0, 0, h, grad_h)])
    print([str(v) for v in gradamax(10 ** -6, 300, -0.5, 0, 0, h, grad_h)])
    nombre_iterations()
