---
title: "Introduction aux structures de données (corrigé)"
date: 2018-02-17
bitlink: goo.gl/gMU2Te
---

## Exercice de programmation ##

En R, les listes et les tableaux sont évidemment présents, et ces deux structures sont implémentées de façon différente:

```r
// La liste contenant les entiers 1, 2, et 3
liste = list(1, 2, 3)
// Le tableau (aussi appelé vecteur) contenant les entiers 1, 2 et 3
tableau = c(1, 2, 3)
```

(Re)programmez les primitives de ces deux structures de données : initialisation d'un objet sans données, suppression d'un élément à une position donnée (sans erreur, donc en particulier en vérifiant que l'objet contient effectivement au moins un élément !), ajout d'un élément à une position donnée, retour de l'indice d'un élément dans l'objet s'il y est présent, sinon d'une valeur par défaut (qui fait sens : donc pas une valeur qui peut être utilisée comme index d'un élément présent). Ne pas utiliser les fonctions déjà présentes en R... Il est vivement encouragé de voir par soi-même l'installation (si nécessaire) et la syntaxe de R sur Internet.

Il y a de multiples manières, plus ou moins optimisées, d'effectuer les actions précédemment citées. Ici, la lisibilité et la compréhension ont été privilégiées, au détriment de l'efficacité et de la concision. Le moyen de vérifier si les fonctions écrites effectuent **vraiment** le but que l'on leur a fixé est soit, si on est matheux, de prouver la **correction** de la fonction, en montrant qu'elle vérifie des propriétés qui imposent que le résultat soit celui attendu; soit de __déboguer__ à la main, en testant sur des exemples **variés** et **nombreux** que la fonction retourne le bon résultat : vérifier les cas limites en particulier, par exemple, quand la liste est vide, ou quand on cherche à atteindre le dernier élément du tableau, et surtout, vérifier que la fonction puisse donner une réponse cohérente dans toutes les situations (surtout quand vous lui demandez de faire une chose incohérente, comme supprimer un élément qui n'existe pas). Des exemples de la méthode "formelle" sont présentés ci-dessous.

Pour les listes :

```ocaml
liste_vide = [];;
// Suppression d'un élément à la position/indice n
let rec suppression_liste liste n = match liste with
| [] -> failwith "La liste fournie en argument a moins de n éléments."
| _ when n=0 -> queue liste
| _ -> (tete liste) :: suppression_liste (queue liste) (n-1);;
// Ajout d'un élément à la position/indice n
let rec ajout_liste liste element n = match liste with
| [] when n=0 -> [element]
| ls when n=0 -> element :: ls
| [] -> failwith "La liste fournie en argument a moins de n éléments."
| ls -> (tete ls) :: (ajout_liste (queue liste) element (n-1));;
// Retour de l'indice d'un élément présent dans la liste
let rec rechercher_liste liste element = match liste with
| [] -> false
| ls when (tete ls)=element -> true
| ls -> rechercher_liste (queue liste) element;;
```

Pour les tableaux :

```ocaml
tableau_vide = [||];;
// Suppression d'un élément à la position/indice n
let suppression_tableau tableau n =
	let len = longueur_tableau tableau in
	let nouveau_tableau = creer_tableau tableau.(0) (len-1) in
	if (n == 0) 
	then 
		for i = (n+1) to (len-2) do
			nouveau_tableau.(i) <- tableau.(i);
		done;
		nouveau
	for i = 0 to (n-1) do
		nouveau_tableau.(i) <- tableau.(i);
	done;
	for i = (n+1) to (len-2) do
		nouveau_tableau.(i) <- tableau.(i);
	done;
	nouveau_tableau;;
 
```

## Quand utiliser une liste ? Quand utiliser un tableau ? ##

