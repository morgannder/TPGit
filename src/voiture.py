class Voiture:
    """Classe représentant une voiture.

    Attributes
    ----------
    nom : str
        le nom de la voiture.
    couleur : str
        la couleur de la voiture.
    vitesse : int
        la vitesse de la voiture (initalisée à 0).
    """

    def __init__(self, nom, couleur):
        """Constructeur"""
        self.nom = nom
        self.couleur = couleur
        self.vitesse = 0

    def __str__(self):
      return f"La voiture {self.nom} de couleur {self.couleur} roule à {self.vitesse} km/h."

    def accelere(self, increment) -> None:
        """Augmente la vitesse de la voiture.

        L'incrément maximal est de 10 km/h.
        La Vitesse maximale est de 130 km/h.

        Parameters
        ----------
        increment : int
            la valeur de l'accélération demandée (limité à 10)
        """
        if increment > 10:
            increment = 10
        self.vitesse = min(130, self.vitesse + increment)