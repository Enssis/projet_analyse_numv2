class matrice:

    ## n est le nombre de lignes
    ## m est le nombre de colonnes

    def __init__(self, n, m, value=0.0):
        self.n = n
        self.m = m
        self.values = [[value for j in range(m)] for i in range(n)]

    def __str__(self):
        result = ""
        for i in range(self.n):
            for j in range(self.m):
                result += str(self.values[i][j]) + " "
            result += "\n"
        return result

    def __add__(self, other):
        if self.n == other.n and self.m == other.m:
            result = matrice(self.n, self.m)
            for i in range(self.n):
                for j in range(self.m):
                    result.values[i][j] = self.values[i][j] + other.values[i][j]
            return result
        else:
            print("Les matrices n'ont pas la même taille")
            return None

    def __sub__(self, other):
        if self.n == other.n and self.m == other.m:
            result = matrice(self.n, self.m)
            for i in range(self.n):
                for j in range(self.m):
                    result.values[i][j] = self.values[i][j] - other.values[i][j]
            return result
        else:
            print("Les matrices n'ont pas la même taille")
            return None

    def __mul__(self, other):
        if self.m == other.n:
            result = matrice(self.n, other.m)
            for i in range(self.n):
                for j in range(other.m):
                    for k in range(self.m):
                        result.values[i][j] += self.values[i][k] * other.values[k][j]
            return result
        else:
            print("Les matrices n'ont pas la même taille")
            return None

    def __eq__(self, other):
        if self.n == other.n and self.m == other.m:
            for i in range(self.n):
                for j in range(self.m):
                    if self.values[i][j] != other.values[i][j]:
                        return False
            return True
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __getitem__(self, i, j):
        return self.values[i][j]

    def __setitem__(self, i, j, value):
        self.values[i][j] = value

    def __delitem__(self, i, j):
        del self.values[i][j]

    def set_diag(self, value):
        for i in range(self.n):
            self.values[i][i] = value

    def mult(self, value):
        for i in range(self.n):
            for j in range(self.m):
                self.values[i][j] *= value
        return self

    def transpose(self):
        result = matrice(self.m, self.n)
        for i in range(self.n):
            for j in range(self.m):
                result.values[j][i] = self.values[i][j]
        return result

    def norme(self):
        result = 0
        for i in range(self.n):
            for j in range(self.m):
                result += self.values[i][j] ** 2
        return result ** 0.5

    def numb(self):
        if self.n == 1 and self.m == 1:
            return self.values[0][0]

    def equal(self, other):
        for i in range(self.n):
            for j in range(self.m):
                if self.values[i][j] != other:
                    return False
        return True

    # rempli la diagonale décalée de `diag` par rapport à la diagonale centrale
    # (diag > 0 pour les diagonales en dessous)
    def set_sous_diag(self, diag, value):
        if abs(diag) > self.n:
            print("erreur sur la valeur de diag")
            return
        for i in range(self.n - abs(diag)):
            if diag > 0:
                self.values[i][i + diag] = value
            if diag < 0:
                self.values[i - diag][i] = value
        