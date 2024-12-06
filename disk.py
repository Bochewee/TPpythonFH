# Classe Disk pour la supervision

class Disk:
    def __init__(self, total, used):
        # Initialise un disque avec total et used
        if used > total:
            raise ValueError("Used > Total")
        self.total = total
        self.used = used

    @property
    def free(self):
        # Retourne l'espace libre
        return self.total - self.used

    def __str__(self):
        # Retourne une chaîne décrivant le disque
        return f"Disk[total: {self.total} Gb, used: {self.used} Gb]"

    def __lt__(self, other):
        # Compare deux disques par pourcentage utilisé
        return (self.used / self.total) < (other.used / other.total)

if __name__ == '__main__':
    # Tests rapides
    disk1 = Disk(total=10, used=2)
    disk2 = Disk(total=20, used=5)
    print(disk1)
    print(disk2)
    print(disk1.free)
    print(disk2.free)
    disks = [disk2, disk1]
    disks_sorted = sorted(disks)
    for disk in disks_sorted:
        print(disk)
