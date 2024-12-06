# Fonctions d'échauffement

def several_zeros():
    # Retourne une liste de 10 zéros
    return [0] * 10

def several_zeros_custom(nb_zeros=10):
    # Retourne une liste de `nb_zeros` zéros (10 par défaut)
    return [0] * nb_zeros

def matrix(rows, cols):
    # Retourne une matrice de dimensions rows x cols remplie de zéros
    return [[0 for _ in range(cols)] for _ in range(rows)]

class Matrix:
    def __init__(self, rows, cols):
        # Initialise une matrice rows x cols remplie de zéros
        self._rows = rows
        self._cols = cols
        self._matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    def get_value(self, row, col):
        # Retourne la valeur à la position row, col
        if 0 <= row < self._rows and 0 <= col < self._cols:
            return self._matrix[row][col]
        raise IndexError("Index hors limites.")

    def __eq__(self, other):
        # Compare deux matrices
        if not isinstance(other, Matrix):
            return False
        return self._matrix == other._matrix

if __name__ == '__main__':
    # Tests rapides
    print(several_zeros())
    print(several_zeros_custom(5))
    print(matrix(2, 3))

    m1 = Matrix(2, 3)
    m2 = Matrix(2, 3)
    print(m1 == m2)
