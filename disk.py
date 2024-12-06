class Disk:
    """
    Classe pour représenter un disque de stockage.
    """

    def __init__(self, total, used):
        """
        Initialise un disque avec un espace total et utilisé.

        :param total: Espace total (en Go).
        :param used: Espace utilisé (en Go).
        """
        if used > total:
            raise ValueError("L'espace utilisé ne peut pas dépasser l'espace total.")
        self.total = total
        self.used = used

    @property
    def free(self):
        """
        Retourne l'espace libre sur le disque.

        :return: Espace libre (en Go).
        """
        return self.total - self.used

    def __str__(self):
        """
        Retourne une représentation textuelle du disque.

        :return: Chaîne formatée.
        """
        return f"Disk[total: {self.total} Gb, used: {self.used} Gb]"

    def __lt__(self, other):
        """
        Compare deux disques par le pourcentage d'espace utilisé.

        :param other: Un autre objet Disk.
        :return: True si le ratio de `self` est inférieur à celui de `other`.
        """
        return (self.used / self.total) < (other.used / other.total)

# Test rapide
if __name__ == '__main__':
    disk1 = Disk(total=10, used=2)
    disk2 = Disk(total=20, used=5)

    # Affichage des disques
    print(disk1)  # Doit afficher : Disk[total: 10 Gb, used: 2 Gb]
    print(disk2)  # Doit afficher : Disk[total: 20 Gb, used: 5 Gb]

    # Espace libre
    print(disk1.free)  # Doit afficher : 8
    print(disk2.free)  # Doit afficher : 15

    # Tri des disques
    disks = [disk2, disk1]
    disks_sorted = sorted(disks)
    for disk in disks_sorted:
        print(disk)  # Doit afficher les disques triés par pourcentage d'espace utilisé
