
import random

class JeuDeCartes:
    def __init__(self):
        self.cartes = [(v, c) for v in range(2, 15) for c in range(4)]

    def nom_carte(self, carte):
        valeurs = {11: 'Valet', 12: 'Dame', 13: 'Roi', 14: 'As'}
        couleurs = {0: 'Coeur', 1: 'Carreau', 2: 'Trèfle', 3: 'Pique'}
        valeur_carte = carte[0]
        couleur_carte = carte[1]
        nom_valeur = valeurs.get(valeur_carte, str(valeur_carte))
        nom_couleur = couleurs.get(couleur_carte)
        return f"{nom_valeur} de {nom_couleur}"

    def battre(self):
        random.shuffle(self.cartes)

    def tirer(self):
        if self.cartes:
            return self.cartes.pop(0)
        else:
            return None
    def tirer_carte_milieu(self):
        if self.cartes:
            milieu = len(self.cartes) // 2  # Position de la carte du milieu
            carte_milieu = self.cartes.pop(milieu)
            return carte_milieu
        else:
            print("Le jeu de cartes est vide.")
            return None  
    def tirer_carte_milieu_aleatoirement(self):
        random.shuffle(self.cartes)
        return self.tirer_carte_milieu()      
      # Dans la classe JeuDeCartes
    def carte_milieu_est_speciale(self):
    # Vérifie si la carte du milieu est spéciale (as, 7, valet)
      if self.cartes:
        valeur, _ = self.cartes[len(self.cartes) // 2]
        return valeur in [7, 11, 14]  # As, 7, Valet

    def echanger_carte_milieu_si_speciale(self):
    # Échange la carte du milieu si elle est spéciale (as, 7, valet)
        if self.carte_milieu_est_speciale():
            nouvelle_carte_milieu = self.tirer()
        if nouvelle_carte_milieu:
            self.cartes.insert(len(self.cartes) // 2, nouvelle_carte_milieu)
    # Dans la classe JeuDeCartes
    def remplacer_carte_milieu(self, carte):
    # Remplace la carte du milieu par la carte spécifiée
        self.cartes[len(self.cartes) // 2] = carte
        

# Utilisation de la classe JeuDeCartes
jeu = JeuDeCartes()
jeu.battre()
class Personne:
    def __init__(self, numero):
        self.numero = numero
        self.cartes_en_main = []
        

    def recevoir_cartes(self, jeu, nombre_de_cartes):
        for _ in range(nombre_de_cartes):
            carte = jeu.tirer()
            if carte:
                self.cartes_en_main.append(carte)
            else:
                print("Le jeu de cartes est vide.")

    def afficher_cartes_en_main(self):
        print(f"Le joueur numéro {self.numero} a :")
        for carte in self.cartes_en_main:
            print(jeu.nom_carte(carte))

    def sauvegarder_cartes(self, nom_fichier):
        with open(nom_fichier, "a") as file:
            file.write(f"Cartes du joueur {self.numero} :\n")
            for carte in self.cartes_en_main:
                file.write(jeu.nom_carte(carte) + "\n")
            file.write("\n")
    def afficher_carte_milieu(self, jeu):
        carte_milieu = jeu.tirer_carte_milieu_aleatoirement()
        if carte_milieu:
            valeur, couleur = carte_milieu
            valeurs = {11: 'Valet', 12: 'Dame', 13: 'Roi', 14: 'As'}
            if valeur == 14 or valeur == 7:
                print("La carte du milieu est un As ou un 7. Aucune carte n'est tirée.")
            elif valeur == 11:
                print("La carte du milieu est un Valet. Vous pouvez choisir n'importe quelle carte.")
            else:
                print(f"La carte du milieu est : {jeu.nom_carte(carte_milieu)}")
            return carte_milieu
        else:
            print("Aucune carte au milieu.")
            return None


    def sauvegarder_carte_milieu(self, jeu, nom_fichier):
        with open(nom_fichier, "a") as file:
            carte_milieu = jeu.tirer_carte_milieu_aleatoirement()
            if carte_milieu:
                valeur, couleur = carte_milieu
                valeurs = {11: 'Valet', 12: 'Dame', 13: 'Roi', 14: 'As'}
                if valeur == 14 or valeur == 7:
                    file.write("La carte du milieu est un As ou un 7. Aucune carte n'est tirée.\n")
                elif valeur == 11:
                    file.write("La carte du milieu est un Valet. Vous pouvez choisir n'importe quelle carte.\n")
                else:
                    file.write(f"La carte du milieu est : {jeu.nom_carte(carte_milieu)}\n")
            else:
                
                file.write("Aucune carte au milieu.\n")
    def somme_numeros_cartes(self):
        return sum([v for v, _ in self.cartes_en_main])

    def jouer_carte(self, index_carte):
        if index_carte < len(self.cartes_en_main):
            carte_jouee = self.cartes_en_main.pop(index_carte)
            print(f"Le joueur {self.numero} joue la carte : {jeu.nom_carte(carte_jouee)}")
            return carte_jouee
        else:
            print(f"Le joueur {self.numero} ne peut pas jouer cette carte.")
    # Dans la classe Personne
    def peut_repondre_avec_sept(self):
    # Vérifie si le joueur peut répondre avec un sept
        return any(carte[0] == 7 for carte in self.cartes_en_main)

    def jouer_carte_reponse(self):
    # Le joueur joue sa carte de réponse si possible
        for carte in self.cartes_en_main:
         if carte[0] == 7:
            self.cartes_en_main.remove(carte)
            return

    def piocher_deux_cartes_de_la_banque(self):
    # Le joueur pioche deux cartes de la banque
     self.recevoir_cartes(jeu, 2)
    # Dans la classe Personne
    def jouer_carte_speciale(self):
    # Si le joueur joue un valet, cela devient automatiquement la nouvelle carte du milieu
     for carte in self.cartes_en_main:
        if carte[0] == 11:  # Valet
            self.cartes_en_main.remove(carte)
            jeu.remplacer_carte_milieu(carte)
            return    
    # Dans la classe Personne
def aucune_carte_restante(self):
    # Vérifie si le joueur n'a plus de cartes à jouer
    return not self.cartes_en_main

def piocher_carte_de_la_banque(self):
    # Le joueur pioche une carte de la banque
    nouvelle_carte = jeu.tirer()
    if nouvelle_carte:
        self.cartes_en_main.append(nouvelle_carte)
    

# Utilisation des classes
jeu = JeuDeCartes()
joueur1 = Personne(1)
joueur1.sauvegarder_carte_milieu(jeu, "carte_milieu.txt")  # Sauvegarde de la carte du milieu dans un fichier texte

# Utilisation de la classe Personne

joueur1.recevoir_cartes(jeu, 4)

# Affichage des cartes en main et de la carte tirée du milieu

carte_du_milieu = joueur1.sauvegarder_carte_milieu(jeu,"carte_milieu.txt")


if carte_du_milieu:
    joueur1.cartes_en_main.append(carte_du_milieu)
  

# Utilisation de la classe Personne
joueur1 = Personne(1)
joueur2 = Personne(2)

joueur1.recevoir_cartes(jeu, 4)
joueur2.recevoir_cartes(jeu, 4)

# Affichage des cartes en main
joueur1.afficher_cartes_en_main()

joueur2.afficher_cartes_en_main()
carte_du_milieu = joueur1.afficher_carte_milieu(jeu)

# Sauvegarde des cartes dans un fichier
joueur1.sauvegarder_cartes("cartes_joueur.txt")
joueur2.sauvegarder_cartes("cartes_joueur.txt")

# Affichage du reste de cartes
print("Reste de cartes dans le jeu :")
reste_cartes = []
while True:
    carte_tiree = jeu.tirer()
    if carte_tiree:
        reste_cartes.append(jeu.nom_carte(carte_tiree))
    else:
        print("Le jeu de cartes est vide.")
        break

# Sauvegarde du reste de cartes dans un fichier
with open("cartes_restantes.txt", "w") as file:
    for carte in reste_cartes:
        file.write(carte + "\n")
        

# Détermination du joueur avec le plus petit poids
if joueur1.somme_numeros_cartes() < joueur2.somme_numeros_cartes():
    premier_joueur = joueur1
    autre_joueur = joueur2
else:
    premier_joueur = joueur2
    autre_joueur = joueur1

# Premier joueur joue la première carte
premier_joueur.jouer_carte(0)

# Autre joueur joue la première carte
autre_joueur.jouer_carte(0)

# Après le joueur a joué une carte
if jeu.carte_milieu_est_speciale():
    jeu.echanger_carte_milieu_si_speciale()
    # Effectuer d'autres actions en conséquence


