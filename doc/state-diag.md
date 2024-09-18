```mermaid
stateDiagram
    login : Se connecter
    menu_joueur : Menu Joueur
    logon : Créer un compte      
    [*] --> Accueil      
    Accueil --> login
    login --> menu_joueur      
    Accueil --> logon      
    Accueil --> quitter
    quitter --> [*]
```