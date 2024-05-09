import turtle as tur


class Forme:
    def __init__(self, couleur):
        self.couleur = couleur

    def draw(self):
        pass


class Cercle(Forme):

    def __init__(self, rayon, couleur):
        super().__init__(couleur)
        self.rayon = rayon

    def draw(self):
        tur.color(self.couleur)
        tur.begin_fill()
        tur.circle(self.rayon)
        tur.end_fill()


class Carre(Forme):

    def __init__(self, cote, couleur):
        super().__init__(couleur)
        self.cote = cote

    def draw(self):
        tur.color(self.couleur)
        tur.begin_fill()
        for _ in range(4):
            tur.forward(self.cote)
            tur.right(90)
        tur.end_fill()


def main():
    while True:
        try:
            type_forme = input(
                "Saisissez le type de forme (cercle/carre): ").lower()
            if type_forme not in ("cercle", "carre"):
                raise ValueError("Type de forme non valide.")
                main()

            couleur = input("Saisissez la couleur de la forme en anglais: ")
            if type_forme == "cercle":
                rayon = float(input("Veuillez saisir le rayon du cercle : "))
                cercle = Cercle(rayon, couleur)
                cercle.draw()

            elif type_forme == "carré" or type_forme == "carre":
                cote = float(
                    input("Veuillez saisir la taille du côté du carré : "))
                carre = Carre(cote, couleur)
                carre.draw()
            tur.hideturtle()
            tur.done()

        except ValueError as e:
            print(f"Erreur: {e}")


if __name__ == "__main__":
    main()
