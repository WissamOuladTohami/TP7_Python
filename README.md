# Exercice 1 : Utilisation des Mixins

### Description
Ce projet illustre l’utilisation des **classes Mixins** pour enrichir des classes principales avec des comportements réutilisables, sans recourir à l’héritage hiérarchique traditionnel.  
L’objectif est de modéliser des entités métiers pouvant bénéficier de fonctionnalités transversales comme l’horodatage ou la validation automatique, tout en gardant une organisation claire et modulaire.

---

### Features
- **Horodatage automatique** : chaque action sur l’objet peut être loguée avec la date et l’heure via `Horodatable`.
- **Validation automatique** : les attributs essentiels comme le titre sont vérifiés via `Validable`.
- **Composition flexible** : la classe principale `Document` combine les mixins à la demande.
- **Méthode de sauvegarde** : `sauvegarder()` applique horodatage et validation avant de confirmer l’enregistrement.

---

### Résultat attendu

<img width="1410" height="188" alt="TP71" src="https://github.com/user-attachments/assets/a88d61bf-95e0-4afa-bdb6-dae607456d4e" />

---

# Exercice 2 : Gestion de Contrats avec Mixins

### Description
Ce projet illustre l’usage avancé des **mixins en Python** pour structurer des comportements transversaux tels que la **journalisation**, l’**historique des modifications** et la **sérialisation JSON**.  
L’objectif pédagogique est de favoriser la réutilisabilité, la séparation des responsabilités et la composition dynamique des capacités métiers.

---

### Features
- **Sérialisation JSON** : la classe `Serializable` permet de convertir un objet en JSON et de le recréer depuis un JSON.
- **Historique des états** : `Historisable` enregistre les versions précédentes d’un objet avec timestamp.
- **Journalisation** : `Journalisable` affiche dans la console toutes les actions effectuées sur l’objet.
- **Composition flexible** : la classe `Contrat` combine les trois mixins pour offrir toutes les fonctionnalités sans héritage hiérarchique complexe.
- **Modification sécurisée** : la méthode `modifier()` conserve l’historique et journalise chaque mise à jour.

---

### Résultat attendu

<img width="1407" height="197" alt="TP72" src="https://github.com/user-attachments/assets/5eee28cb-880c-4c46-8fff-364304d45c58" />

---

# Exercice 3 : Gestion de Tâches Professionnelles avec Mixins

### Description
Ce projet modélise un système de gestion de tâches professionnelles en Python.  
Chaque tâche possède un titre obligatoire, une description et une date de création.  
L’objectif pédagogique est de démontrer l’intérêt de la **composition de comportements via mixins**, tout en séparant les responsabilités et en favorisant la réutilisation et la modularité du code.  
Le système gère également la traçabilité des modifications et la validation métier.

### Features
- **Validation du titre** : `ValidationMixin` vérifie que le titre est toujours renseigné et non vide.  
- **Historique des modifications** : `HistoriqueMixin` enregistre chaque version antérieure de la description.  
- **Journalisation des actions** : `JournalisationMixin` affiche un journal de chaque action (création, mise à jour).  
- **Mise à jour sécurisée** : la méthode `mettre_a_jour()` conserve l’historique et journalise chaque modification.  
- **Consultation de l’historique** : la méthode `afficher_historique()` permet de visualiser les anciennes descriptions.

### Résultat attendu 

<img width="1407" height="308" alt="TP73" src="https://github.com/user-attachments/assets/9a934d26-32f1-4ec1-835e-1318f1f029a3" />




