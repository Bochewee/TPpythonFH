class Matrix:
    """
    Classe pour représenter une matrice.
    """

    def __init__(self, rows, cols):
        """
        Initialise une matrice de dimensions `rows x cols` remplie de zéros.

        :param rows: Nombre de lignes.
        :param cols: Nombre de colonnes.
        """
        self._rows = rows
        self._cols = cols
        self._matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    def get_value(self, row, col):
        """
        Retourne la valeur de la matrice à la position donnée.

        :param row: Index de la ligne.
        :param col: Index de la colonne.
        :return: Valeur à la position spécifiée.
        """
        if 0 <= row < self._rows and 0 <= col < self._cols:
            return self._matrix[row][col]
        else:
            raise IndexError("Index hors limites.")

    def __eq__(self, other):
        """
        Vérifie si deux matrices sont égales.

        :param other: Autre instance de Matrix.
        :return: True si les matrices sont égales, sinon False.
        """
        if not isinstance(other, Matrix):
            return False
        return self._matrix == other._matrix

# Test rapide
if __name__ == '__main__':
    m1 = Matrix(2, 3)
    m2 = Matrix(2, 3)
    m3 = Matrix(3, 2)

    # Vérification des valeurs
    print(m1.get_value(0, 0))
    # print(m1.get_value(2, 3))  # Doit lever une erreur : IndexError

    # Vérification de l'égalité
    print(m1 == m2)
    print(m1 == m3)
