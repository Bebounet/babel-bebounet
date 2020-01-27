# Babel-bebounet

## Changelog 

## Semaine 3: Django et Babel

### 22/01/20

###### Deploiement

- Cloud hebergement serveur 
    - heroku
    - settings.py propre a heroku
    - package gunicorn, dj-url, django-heroku
    - python manage.py collectstatic
    
###### A Developper

- Test mobile
- Page détail Publication
- Page auteur
- Formulaire d'acquisition d'une publication par l'usager

### 21/01/20

##### A faire 

- urls de la page détail
    - /catalog/"<dewey>_<aut>_<id>"/
    - /catalog/<refpub>/
- template page détails
    - publication display
    - auteur display

##### Etapes de conception web de Babel

- cahier des charges/clients/besoins/objectifs/delais/prix
- choix technologiques

###### 1
- structure des données, des tables(makemigrations et migrate)
- superadmin, compte admin
- composants/fonctions métiers
    - liste Dewey, norme de travail
    - publications
    - auteurs
###### 2
- backoffice pour l'admin en lien au données
###### 3 
- site public avec son interface
- affichage dernieres oeuvres insérées 
- fiche oeuvre
- recherche via Dewey

## Semaine 2: Django et Babel

### 10/01/20

###### Application
- Recuperer les données via la techno de scrapping html à partir d'un url
- creation d'un composant html pour afficher les données liste de scrap_url
- settings django : 
    - FILES_MEDIA: transfert des images des utilisateurs (file upload), peut être en accès privé.
    - FILES_STATIC: ressources static de l'application, accès public.(CSS, js, Front, Jpg, video)
- Integration dans des listes auteurs, publication des filtres, recherche et une autocompletion dans les formulaire de l'interface admin du backoffice de la bibliothecaire.
- elements html -> interface utilisateur 
- traduction des libelles des champs anglais -> francais
    - sur les formmulaires du backoffice
    - listes auteur, publication, dewey
- fonction couleur dans le modele dewey pour associer au code de la classification la couleur du fond de texte selon la norme dewey
- query: liste de données
- urls: aiguillage d'urls


### 09/01/20

###### Application
- ajout de fonctionnalitées : 
    - Couleurs qui s'adaptent selon le classement Dewey
    - Calcul du siècle de naissance en fonction de la date de naissance d'un auteur et integration dans l'application
- saisie formulaire
- reflexion sur les choix a prendre sur les fonctionnalitées a intégrer 
    - parfois les devs spécifiques s'evitent par une formation/accompagnement de l'utilisateur final
    - retour de l'experience métier, permet de corriger ou d'orienter le dev
    - regrouper en temps (1,2,3) les devs
- admin formulaire definition du modèle
- regrouper en sections les zones de saisie pour etre en accord avec le metier et l'objet de la table author et publication 

### 08/01/20

##### Définitions d'objectifs

#### Partie A
###### temps 0
- aide a la saisie
    - menu déroulant 
    - date

<!-- -->
###### temps 1
- bouton annuler
- rassembler les données et les ordonnés en affichage 
- tenir compte de l'objet livre, musique, video
- champs obligatoire (étoile rouge)

<!-- -->
###### temps 3
- saisie autocompletion sur auteur, publication 

<!-- -->
###### temps 2
- image file

#### Partie B
- images
- amélioration interface utilisateur et de l'experience utilisateur
    -> admin, table publication, author, dewey
    -> aide a la saisie
- dewey
    - classement niveau 2
    - fichier source
    - code couleur
- publication
    - ISBN
    - statut (emprunté, disponible) --> integration système existant

### 07/01/20

##### Documentation Django
lien vers la doc Django <https://docs.djangoproject.com/fr/3.0/>

##### Commandes serveur python
- ``C:/Users/nicos/.virtualenvs/babel-bebounet-GdwkihvD/Scripts/activate.ps1`` (se déplacer ici)
- ``python manage.py runserver`` (lancer le serveur)
- ``python manage.py makemigrations`` (creer les migrations de bdd)
- ``python manage.py migrate`` (appliquer les modifications)

##### application mediatheque
- schéma bdd 
- definition ORM
- création des classes pour créer la bdd dans ``models.py``
- Exemple d'une création de table : 

code

    class Author(models.Model):
    """Création de la table Author"""
    
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30)
    name = models.CharField(max_length=61, editable=False)
    century_birth = models.IntegerField(null=True, blank=True)
    date_birth = models.DateField(null=True, blank=True)
    place_birth = models.CharField(max_length=50, null=True, blank=True)
    date_died = models.DateField(null=True, blank=True)
    place_died = models.CharField(max_length=50, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)
    image_file = models.ImageField(null=True, blank=True)

- déclaration des modeles dans ``admin.py``, modification de l'affichage de la table Publication
- fonctions prédéfinies héritant de _models.Model_
- class ``Meta`` et utilisation de _ordering_ pour trier dans l'ordre les données de la bdd

<!-- -->

Architecture : 
    - Besoin du client
    - expression schéma utilisateur ---> 2 personnas
    - nomenclature ``code/entreprise``
    - objet : 
        - construction interface backoffice pour la gestiondu catalogue d'une médiatheque


## Semaine 1: Python et algorithmes

### 20/12/19

##### Django
- installation de django
- create superuser admin -> authentication, crud, model(bdd)
- create user
- settings.py (config django)
- page home affiche le contenu json checkurl
    - .py def home() -> url
- template home.html

### 19/12/19

##### beautifulSoup
- Package ``BeautifulSoup`` vient de PYPi.org - installé avec pip
    - outil de scraping --> recupere le contenu du web
    - format html en entrée
        - analyse le DOM ``Document Object Model``
        - organise les balise html en un arbre
    - ``soup.title``
    - ``soup.find-all <h1>``

##### Debug
- Modification du script execution sous windows
- enlever le warning W291 (mettre un \n en fin de page) chez flake8 -> lint

##### pipenv -> virtual environment 
- environement python "propre" = version downloadable de python.org
- repertoire de stockage de votre env se trouve dans /user/.virtualenv/..
- pipfile -> version humaine
- pipfile.lock -> version machine
    - connecté a pypi.org

##### divers
- consulter les sources opensource de python dont ``datetime.py`` 
- package request HTTP get url ........
    - header requete HTTP - ajout la clé user-agent valeur de votre browser
- blake -> save sans erreur de lint


### 18/12/19

- Test unitaires dont ``assertEqual``
- try, exept exception
- git github
- Fonctions avec ``datetime``
- MVC : design pattern sur traitement d'une classe et de son affichage avec un controlleur
- Syntaxe du while
- ``readme.md`` au format markdown

### 17/12/19

- Algorithme chaine de caractères qui prend une chaine " <fullname> " et la met au format " <firstname> <middle> <lastname> " 
- Dictionnaire est une liste de `` clé/valeur ``
- Import de modules `` sys, os ``
- Fonction _print()_ avec ``f" {variable} ``
- Fonction _split()_ : séparation de chaines de caractères par un sep par defaut ``" "``
- _type(a)_ permet de savoir la classe de a
- isInstance (a, classe)
- Objets de classe ``int, str, boolean, dic, list, def():``
- Opérateurs : `` =, <>, +, *, ``
- ``regex`` Expressions régulières

