# Search-engine-for-movies-and-series
# Partie 1 : Analyse descriptive des bases et visualisation:
Vous devrez tout d’abord effectuer une description classique des données (ex. taille des fichiers, nombre
d’observations…) puis répondre aux questions suivantes:  
* Quelle est la plateforme qui contient le plus de diversité géographique de films et séries ? Faire un
graphique  
* Quelle est l’évolution au cours du temps de l’offre (i.e. nombre) de films et séries pour chacune des
plateformes de streaming ? Faire la distinction Amazon Prime/Netflix/Disney + et également une
distinction film/série  
* Quels sont les genres de films/séries les plus représentés sur chaque plateforme de streaming ? Faire un
graphique global/films uniquement/séries uniquement  
* Quelle est la note moyenne des films par genre pour chaque plateforme ? Se concentrer uniquement sur les
5 genres les plus représentés pour créer une représentation graphique des notes moyennes par genre, par
plateforme  
# Partie 2 : Moteur de recherche
Vous devrez ensuite construire un moteur de recherche qui permettra de chercher dans les différentes bases
et retourner à un utilisateur à minima les résultats suivants (vous pouvez rajouter d’autres fonctionnalités si
vous le souhaitez) :  
* L’utilisateur saisit le titre d’un film ou d’une série : Afficher les plateformes sur lesquelles le film/la série est
disponible avec des informations comme l’année de sortie, le synopsis, les acteurs principaux, le genre. Si
c’est un film, donner sa note sur IMDb si elle existe. Prendre en compte le cas où l’utilisateur entre un film
qui n’existe dans aucun catalogue.  
* L’utilisateur entre le nom d’un acteur : Suggérer une plateforme entre les 3 en fonction du nombre de
films/séries de l’acteur disponible sur chacune des plateformes, puis afficher les films/séries de cet acteur
disponibles avec des informations dessus (type, nom, année, synopsis, classification et genres)  
* L’utilisateur saisit un type de contenu (film/série) et un genre : Afficher le nombre de résultats qui
remplissent les critères d’entrée pour chacune des plateformes puis parmi ces résultats les 3 films ou séries
les plus récent(e)s pour chaque plateforme  
* Demander à l’utilisateur des informations sur ses préférences : séries ou films, genre, rating, pays de
production et éventuellement le nom d’un ou de plusieurs acteurs et suggérer du contenu sur chaque
plateforme. Pour cette suggestion, vous pouvez par exemple donner les 5 films/séries les plus récent(e)s
pour chaque plateforme, les 5 films/séries ajoutées le plus récemment etc. Vous mentionnerez le critère
choisi.  
# Partie 3 : Interface
Vous devrez ensuite créer une interface pour l’utilisateur, afin qu’il n’ait pas à écrire de lignes de code pour
utiliser le moteur de recherche une fois le script exécuté. Vous pourrez soit demander les infos à l’utilisateur
avec des input puis afficher les résultats dans la console avec print (version simple), soit utiliser le module
Python Tkinter pour réaliser une interface graphique (version plus poussée).  
