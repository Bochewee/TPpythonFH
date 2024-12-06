import tkinter as tk
from tkinter import messagebox

class DiskUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculateur d'utilisation de disque")

        # Champs d'entrée
        tk.Label(root, text="Espace total (Gb):").grid(row=0, column=0, padx=10, pady=5)
        self.total_entry = tk.Entry(root)
        self.total_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Espace utilisé (Gb):").grid(row=1, column=0, padx=10, pady=5)
        self.used_entry = tk.Entry(root)
        self.used_entry.grid(row=1, column=1, padx=10, pady=5)

        # Bouton pour calculer le pourcentage
        tk.Button(root, text="Calculer", command=self.calculate).grid(row=2, column=0, columnspan=2, pady=10)

        # Zone pour afficher le résultat
        self.result_label = tk.Label(root, text="", fg="blue")
        self.result_label.grid(row=3, column=0, columnspan=2, pady=10)

    def calculate(self):
        try:
            total = float(self.total_entry.get())
            used = float(self.used_entry.get())

            if used > total:
                raise ValueError("L'espace utilisé ne peut pas dépasser l'espace total.")

            # Calcul du pourcentage d'utilisation
            usage_percentage = (used / total) * 100
            self.result_label.config(text=f"Utilisation : {usage_percentage:.2f}%")
        except ValueError as e:
            messagebox.showerror("Erreur", str(e))

# Exécution de l'interface
if __name__ == '__main__':
    root = tk.Tk()
    app = DiskUI(root)
    root.mainloop()
