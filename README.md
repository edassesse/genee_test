# Développement d'une application web avec gestion de formulaires dynamiques et une base de données spécifique

## Technologies requises:
- Backend: Python Flask SQLAlchemy (la connaissance de Marshmallow est un grand plus mais pas obligatoire)
- Frontend: À votre discrétion
- Base de données: À votre discrétion
- Environnement de développement: Libre

## Objectif du test:

Votre mission consiste à créer une page web contenant un formulaire. Ce formulaire est lié à une base de données qui comprend obligatoirement un modèle "Affaire". Toutes les autres données sont liées à une affaire.

Le formulaire doit contenir les éléments suivants:
1. Un champ pour le nom de l'affaire.
2. Un champ de sélection (type select) pour les lieux. Ce champ est composé des éléments suivants:
   - Un département
   - Une commune
   - Un champ texte libre intitulé "Préciser".

La base de données doit avoir une relation entre le département et la commune. Cependant, vous n'avez pas besoin de représenter toutes les communes et tous les départements de France. La création de 3 départements et 10 communes pour ce test est suffisante.

Les champs département et commune sont liés de manière à ce que, lorsqu'un département est sélectionné, seules les communes correspondantes soient disponibles pour la sélection. De plus, si une commune est sélectionnée, son département associé est automatiquement sélectionné.

Le champ de sélection du lieu doit offrir un choix unique ou multiple:
- En mode de choix unique: l'utilisateur peut insérer un seul lieu.
- En mode de choix multiple: un deuxième champ de lieu vide est automatiquement ajouté. L'utilisateur doit pouvoir supprimer des lieux s'il y en a plus de deux et il doit y avoir un bouton "+" pour ajouter de nouveaux lieux. Si l'utilisateur passe du mode de choix multiple au mode de choix unique, tous les lieux supplémentaires sont supprimés, ne laissant que le premier.

Enfin, le formulaire doit comporter un bouton "Valider" pour enregistrer les modifications. Lorsqu'un utilisateur recharge la page après avoir sauvegardé, tous les champs précédemment enregistrés dans la base de données doivent être préremplis.

Nous attendons avec impatience de voir comment vous allez résoudre ce défi!
