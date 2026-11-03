# Exercices de Programmation Orientée Objet en Python

## Sommaire

1. [Exercice 1 — Compteur de visites de pages](#exercice-1)
2. [Exercice 2 — Gestion d'inventaire d'articles](#exercice-2)
3. [Exercice 3 — Carnet d'adresses minimal](#exercice-3)
4. [Exercice 4 — Calculatrice géométrique pour cercles](#exercice-4)
5. [Exercice 5 — Journal de tâches avec gestion de contexte](#exercice-5)
6. [Exercice 6 — Convertisseur de devises](#exercice-6)
7. [Exercice 7 — Gestion de la mémoire et du cycle de vie](#exercice-7)
8. [Exercice 8 — Opérateurs personnalisés (dunder methods)](#exercice-8)
9. [Exercice 9 — Classes de données avec `dataclasses`](#exercice-9)
10. [Exercice 10 — Validation avancée avec des décorateurs](#exercice-10)

## Structure du projet

```
exercices_poo/
├── exo01_compteur_page/
├── exo02_article/
├── exo03_carnet_adresses/
├── exo04_cercle/
├── exo05_journal_taches/
├── exo06_convertisseur/
├── exo07_ressource/
├── exo08_vecteur/
├── exo09_dataclass/
├── exo10_decorateurs/
├── run_all.py
└── README.md
```



---

<a id="exercice-1"></a>
## Exercice 1 — Compteur de visites de pages

**Objectif :** Distinguer attribut de classe et attribut d'instance

**Dossier :** `exo01_compteur_page/`  
**Fichiers :** compteur_page.py, `main.py`

**Résultat de l'exécution :**

![Résultat exercice 1](<img width="1280" height="720" alt="ex1" src="https://github.com/user-attachments/assets/811c1c37-3e65-457d-bd8b-3a066e91f517" />
)

---

<a id="exercice-2"></a>
## Exercice 2 — Gestion d'inventaire d'articles

**Objectif :** Encapsuler données métier et calculs

**Dossier :** `exo02_article/`  
**Fichiers :** article.py, `main.py`

**Résultat de l'exécution :**

![Résultat exercice 2](<img width="1280" height="720" alt="ex2" src="https://github.com/user-attachments/assets/02f9c243-1896-4a64-9958-ecaaa3999bd1" />
)

---

<a id="exercice-3"></a>
## Exercice 3 — Carnet d'adresses minimal

**Objectif :** Listes d'objets, propriétés et recherche

**Dossier :** `exo03_carnet_adresses/`  
**Fichiers :** contact.py, carnet.py, `main.py`

**Résultat de l'exécution :**

![Résultat exercice 3](<img width="1280" height="720" alt="ex3" src="https://github.com/user-attachments/assets/535732ee-9fef-44ad-ac60-f14109c101d4" />
)

---

<a id="exercice-4"></a>
## Exercice 4 — Calculatrice géométrique pour cercles

**Objectif :** Sécuriser l'accès aux attributs avec des propriétés

**Dossier :** `exo04_cercle/`  
**Fichiers :** cercle.py, `main.py`

**Résultat de l'exécution :**

![Résultat exercice 4](<img width="1280" height="720" alt="ex4" src="https://github.com/user-attachments/assets/19cf8652-4b9a-4805-b65f-7db682b228ef" />
)

---

<a id="exercice-5"></a>
## Exercice 5 — Journal de tâches avec gestion de contexte

**Objectif :** Utiliser `with` (`__enter__` / `__exit__`) pour ouvrir et fermer un fichier

**Dossier :** `exo05_journal_taches/`  
**Fichiers :** journal.py, `main.py`

**Résultat de l'exécution :**

![Résultat exercice 5](<img width="1280" height="720" alt="ex5" src="https://github.com/user-attachments/assets/0b6e0b2e-bda6-480e-9308-ed0aabc4b7ca" />
)

---

<a id="exercice-6"></a>
## Exercice 6 — Convertisseur de devises

**Objectif :** Méthodes statiques et méthodes de classe

**Dossier :** `exo06_convertisseur/`  
**Fichiers :** convertisseur.py, `main.py`

**Résultat de l'exécution :**

![Résultat exercice 6](<img width="1280" height="731" alt="ex6" src="https://github.com/user-attachments/assets/25f15426-5ece-4f6b-9ea3-0f9225550d22" />
)

---

<a id="exercice-7"></a>
## Exercice 7 — Gestion de la mémoire et du cycle de vie

**Objectif :** Comprendre `__del__` et la gestion des ressources

**Dossier :** `exo07_ressource/`  
**Fichiers :** ressource.py, `main.py`

**Résultat de l'exécution :**

![Résultat exercice 7](<img width="1280" height="720" alt="ex7" src="https://github.com/user-attachments/assets/e8d3c302-2ef5-4e7b-8ddd-11c0082f5c86" />
)

---

<a id="exercice-8"></a>
## Exercice 8 — Opérateurs personnalisés (dunder methods)

**Objectif :** Surcharger les opérateurs pour un code plus naturel

**Dossier :** `exo08_vecteur/`  
**Fichiers :** vecteur.py, `main.py`

**Résultat de l'exécution :**

![Résultat exercice 8](<img width="1280" height="720" alt="ex8" src="https://github.com/user-attachments/assets/7d436927-450e-408d-9fe0-1584ce297e34" />
)

---

<a id="exercice-9"></a>
## Exercice 9 — Classes de données avec `dataclasses`

**Objectif :** Simplifier la création de classes de données

**Dossier :** `exo09_dataclass/`  
**Fichiers :** produit.py, `main.py`

**Résultat de l'exécution :**

![Résultat exercice 9](<img width="1280" height="720" alt="ex9" src="https://github.com/user-attachments/assets/da2bc343-fa36-4073-b910-c962dfc860c0" />
)

---

<a id="exercice-10"></a>
## Exercice 10 — Validation avancée avec des décorateurs

**Objectif :** Créer des décorateurs pour valider les arguments de méthodes

**Dossier :** `exo10_decorateurs/`  
**Fichiers :** validateurs.py, rectangle.py, `main.py`

**Résultat de l'exécution :**

![Résultat exercice 10](<img width="1280" height="720" alt="ex10" src="https://github.com/user-attachments/assets/3fd63ab6-a151-487e-9a44-a31ffa8a6e5c" />
)

---
