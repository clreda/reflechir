---
title: "Introduction aux graphes (corrigé)"
date: 2017-12-16
bitlink: http://bit.ly/2AMYmZC
--- 

**Note :** C'est la correction des exercices de l'article "Introduction aux graphes".

## Exercices de compréhension ##

**Exercice 1 :** Dites combien vaut K(G) quand G a trois sommets 0, 1 et 2, et trois arêtes, une reliant 0 à 1, une reliant 1 à 2, et l'autre reliant 2 à 0.

Attention : on parle ici d'arêtes, donc le graphe est non orienté. On rappelle que K(G) est le nombre minimal de couleurs nécessaire pour qu'il existe une coloration c telle que (P) : si les sommets i et les sommets j sont reliés par une arête, alors ils ont des couleurs distinctes par la coloration c : c(i) différent de c(j) (en reprenant les notations de l'article précédent). On va évidemment utiliser au moins une couleur, donc K(G) est au moins supérieur ou égal à 1. D'autre part, le nombre minimal de couleurs est tout d'abord forcément plus petit ou égal au nombre de noeuds du graphe, ici 3, puisque qu'une coloration donne une couleur à chaque noeud. Donc, de manière générale, pour n'importe quel graphe à n sommets, 1 $\leq$ K(G) $\leq$ n.

Voici ci-dessous le graphe G de l'exercice :

<img src="/images/2017-12-16-image1.png" style="float: center"/> 

Voici un exemple de l'inégalité prouvée précédemment sur G :

<img src="/images/2017-12-16-image2.png" style="float: center"/> 

Pour démontrer que K(G) = 3, il suffit de montrer que K(G) $\geq$ 3, et utiliser les inégalités trouvées précédemment. Pour cela, on peut tester les cas K(G) = 1 et K(G) = 2, et montrer que de telles colorations ne respectent pas la propriété requise (P). 

Plus astucieusement, on peut raisonner par l'absurde. En supposant que K(G) est strictement inférieur à 3, il existe alors deux noeuds dans G qui ont la même couleur (puisqu'il y a moins de 3 couleurs pour 3 noeuds : on appelle aussi ce raisonnement **le principe des tiroirs**). Or toute paire de sommets dans G est reliée par une arête (voir le schéma précédent), ce qui contredit (P). Donc K(G) est supérieur ou égal à 3, donc K(G) = 3.

**Exercice 2 :** Un graphe complet à i sommets (noté $K_i$) est un graphe tel qu'il existe une arête entre chaque couple de sommets distincts du graphe (par exemple, le graphe de l'exercice précédent s'appelle $K_3$). Montrez que $K(K_i)$ est supérieur ou égal à i. (Indice : démonstration par l'absurde, en supposant que $K(K_i)$ est strictement inférieur à i)

Suivons l'indice donné, et faisons une démonstration par l'absurde, en supposant $K(K_i)$ strictement inférieur à i. Alors le graphe $K_i$ est colorié avec strictement moins de i couleurs, donc il existe au moins deux noeuds distincts ayant la même couleur (voir le raisonnement effectué à l'exercice 1). Or il existe une arête entre chaque couple de sommets distincts, donc la coloration ne respecte pas (P). Donc $K(K_i)$ est supérieur ou égal à i.

En utilisant le raisonnement décrit à l'exercice précédent, on montre que $K(K_i)$ est inférieur ou égal à i, donc $K(K_i)$ = i.

**Exercice 3 :** Un cycle à i sommets $C_i$ est un graphe tel que, si les sommets sont numérotés 0, 1, 2, 3, ..., i-1, ses arcs sont (0, 1), (1, 2), (2, 3), ..., (i-2, i-1), (i-1, 0). Montrez que si i est supérieur ou égal à 2, alors soit $K(C_i)$ = 2 si i est pair, soit $K(C_i)$ = 3 si i est impair. (Indice : raisonnement par récurrence sur i puis, à l'intérieur de la récurrence, un raisonnement par disjonction de cas, dans les deux cas où i est pair/impair)

Faisons un raisonnement par récurrence sur i supérieur ou égal à 2. On démontre "si i est supérieur ou égal à 2, alors soit $K(C_i)$ = 2 si i est pair, soit $K(C_i)$ = 3 si i est impair".

Si i = 2, alors la seule paire de sommets distincts dans le graphe est reliée par une arête, donc $K(C_2)$ est supérieur ou égal à 2. De plus, on peut montrer par un dessin que l'on peut colorier ce graphe avec deux couleurs en respectant (P) :

<img src="/images/2017-12-16-image3.png" style="float: center"/> 

Donc $K(C_2) \leq$ 2, d'où $K(C_2)$ = 2.

Si i = 3, c'est le graphe de l'exercice 1.

Prenons i > 3. Raisonnons par disjonction de cas.

**Si i est impair**, on sait par récurrence que $K(C_{i-1})$ = 2, car i-1 est pair et strictement inférieur à i. L'intuition est que l'on obtient $C_{i}$ à partir de $C_{i-1}$ en ajoutant le noeud i-1, et en retirant l'arête reliant i-2 à 0, et en ajoutant une arête reliant i-1 à 0. On va alors construire une coloration du graphe $C_i$ avec un nombre de couleurs minimal à partir de la coloration avec un nombre de couleurs minimal de $C_{i-1}$.

Soit c une coloration à deux couleurs, jaune et bleu par exemple, de $C_{i-1}$ (d'après l'hypothèse de récurrence). Quitte à échanger les deux couleurs, supposons que le noeud 0 est colorié en jaune. Alors, nécessairement, le noeud i-2 est colorié en bleu, car sinon cela contredirait le fait que $K(C_{i-1}) = 2$. Effectuons l'opération précédente pour obtenir le graphe $C_i$. Les deux voisins du noeud i-1 sont coloriés en bleu et en jaune, donc nécessairement le noeud i-1 doit être colorié dans une autre couleur. En effet, si on ne veut colorier le graphe qu'avec deux couleurs et qu'on colore le noeud i-1 en bleu, alors le noeud i-2 doit être colorié en jaune. Par récurrence sur le nombre de noeuds du graphe (c'est-à-dire en itérant ce raisonnement sur un graphe de plus en plus petit), cela signifierait que $K(C_{i-1})=1$ (imaginer le cas i=3), ce qui est absurde. Donc $K(C_{i}) \geq 3$. Et vu que la coloration c construite précédemment (nombres pairs coloriés en jaune, nombres impairs coloriés en bleu, i-1 colorié en rouge) est une coloration qui respecte la propriété (P), alors $K(C_i) \leq 3$, d'où $K(C_i) = 3$.

**Si i est pair**, le plus simple est de se passer de l'hypothèse de récurrence. On peut numéroter les noeuds du graphe de 0 à i-1, et colorier les noeuds de numéro pair en rouge, et les noeuds de numéro impair en bleu. Les noeuds de numéro pair (respectivement impair) n'étant reliés qu'à des noeuds de numéro impair (respectivement pair), ce coloriage respecte la propriété (P), d'où $K(C_i) \leq 2$. Si on n'utilise qu'une seule couleur, toutes les paires de sommets reliés par une arête sont de la même couleur, ce qui contredit (P). D'où $K(C_i) \geq 2$, d'où finalement $K(C_i) = 2$.

Cela achève la démonstration.

## Exercices avancés ##

**Exercice de programmation :** Ecrire (dans le langage de votre choix) l'algorithme réalisé précédemment, pour le problème des emplois du temps. Vérifiez qu'il renvoie bien m=2 pour l'instance présentée précédemment.

La correction est donnée dans le langage Python, choisi pour sa lisibilité. On rappelle brièvement la méthode suivie dans l'article précédent (qui, au passage, est loin d'être la plus efficace en temps...) : étant donné un graphe G=(S, A) (représentés respectivement en Python par une liste d'entiers, et par une liste de couples d'entiers), on énumère les possibles nombres chromatiques en partant de 0, jusqu'à trouver une coloration qui respecte la propriété (P) sur l'ensemble du graphe. L'algorithme retourne le nombre chromatique m correspondant. Le plus dur est d'implémenter la procédure de coloration du graphe. En pratique, au lieu de fixer d'abord m et d'essayer de colorier le graphe, on va plutôt partir d'un noeud que l'on va colorier par exemple en bleu (couleur 1); on coloriera ses voisins en jaune (couleur 2). On va alors répéter ce processus, quitte à utiliser d'autres couleurs lorsque au moins l'un des voisins du noeud que l'on considère est colorié en bleu, jaune, ou toute autre couleur déjà utilisée. La coloration sera résumée dans un tableau de longueur égale au nombre de noeuds dans le graphe, et où sera écrit dans chaque case associée à un noeud le numéro correspondant à la couleur de ce noeud. On garde en mémoire le nombre de couleurs utilisé m. 

```python
def trouver_coloration(S,A):
	if (len(S)==0):
		return(0)
	col=[None]*len(S)
	m = 1
	if (len(A)==0):
		return(m)
	i = 0
	while (any([v==None for v in col]) and i <= len(S)-1):
		voisins = [S.index(x[1]) for x in filter(lambda x : x[0]==S[i], A)]
		voisins += [S.index(x[0]) for x in filter(lambda x : x[1]==S[i], A)]
		M = 1
		while (any([col[v]==M for v in voisins])):
			M += 1
		if (M == m+1):
			m += 1
		col[i] = M
		i += 1
	return(m)
```

Pour tester l'instance du problème de l'article précédent :

```python
S=["Mathématiques", "Français", "Histoire", "SVT", "Physique"]
A=[["Mathématiques", "Français"], ["Histoire", "SVT"], ["SVT", "Physique"]]
print(trouver_coloration(S, A))
```

L'algorithme retourne bien m=2 sur cette instance.

**Une famille de graphes particulière : les graphes planaires** Un graphe planaire G est tel qu'il existe une façon de le dessiner sans que les arêtes ne s'intersectent. Un __graphe planaire plongé__ est un graphe qui est dessiné sans que les arêtes ne s'intersectent. Autrement dit, un graphe planaire peut être dessiné sous forme d'un graphe planaire plongé. Ici, lorsqu'on évoquera un graphe planaire, on pensera à sa version plongée.

Le graphe $K_4$ est-il planaire ? $K_5$ est-il planaire ? (Indice : il y a un oui et un non. Pour prouver le oui, dessinez une version planaire du graphe. La justification du non nécessite le théorème de Kuratowski-Wagner, qui sera présenté plus tard)

$K_4$ est planaire, voir le dessin ci-dessous :

<img src="/images/2017-12-16-image6.png" style="float: center"/> 

**Une autre famille de graphes particulière : les graphes connexes** Un graphe connexe est un graphe tel que, pour tous sommets i et j distincts, il existe un chemin, c'est-à-dire une suite d'arêtes/arcs, dans le graphe de i vers j (et de j vers i, si le graphe est non orienté). Par exemple, $K_3$ est connexe. Donnez un exemple de graphe non connexe, et justifiez sa non-connexité (On exhibera donc un couple de sommets qui ne respecte pas la condition ci-dessus).

<img src="/images/2017-12-16-image7.png" style="float: center"/> 

0 et 1 ne respectent pas la condition de connexité, puisque ce graphe ne possède pas d'arête.

**Une autre famille de graphes particulière : les graphes bipartis** Le graphe $G_{i,j}$ est le graphe constitué de deux ensembles de sommets distincts $G_i$ (contenant i sommets) et $G_j$ (contenant j sommets), tels que toute arête/arc soit une interaction de la forme (a, b) où soit a appartient à $G_i$ et b appartient à $G_j$, soit a appartient à $G_j$ et b appartient à $G_i$. Vérifiez que le graphe présentant l'instance du problème de l'article est un graphe biparti, et exhibez les parties de l'ensemble de sommets correspondantes. Il existe un théorème qui montre qu'un graphe a un nombre chromatique inférieur ou égal à 2 si et seulement s'il est biparti. Prouvez ce théorème.

Le graphe est bien biparti : on colore les noeuds du premier ensemble de sommets en rouge, ceux du deuxième ensemble en vert.

<img src="/images/2017-12-15-image3.png" style="float: center"/> 

L'énoncé du théorème utilise un "si et seulement si" : il s'agit alors de prouver les deux sens de l'équivalence.

Supposons que le graphe est biparti. Alors colorions en rouge les noeuds issus du premier ensemble de sommets, et en vert les noeuds appartenant au deuxième ensemble (comme dans la figure ci-dessus). Alors la coloration obtenue respecte bien la propriété (P) de l'article d'introduction aux graphes (car les deux ensembles de sommets sont __distincts__ et que les arêtes/arcs ne sont partagés que par des noeuds appartenant à des ensembles de sommets différents, par définition).

Supposons que le graphe a un nombre chromatique inférieur ou égal à 2, donc égal à 1 ou à 2 si le graphe possède au moins un sommet. S'il est égal à 1, alors cela signifie que les noeuds du graphe ne sont pas reliés entre eux, car s'il existait une arête/arc, alors la propriété (P) ne serait pas maintenue pour le couple de noeuds reliés par cette arête/arc. On peut alors choisir arbitrairement deux ensembles de sommets distincts (avec éventuellement l'un des deux vide) dont l'union est égale à l'ensemble total de sommets, donc le graphe est biparti. Si le nombre chromatique est égal à 2, alors il existe une coloration à deux couleurs du graphe qui respecte la propriété (P). Les deux ensembles de noeuds distincts sont alors les deux ensembles de noeuds de couleur différente. Par définition de la coloration, les arêtes/arcs ne relient que des noeuds de couleur différente, donc appartenant à des ensembles différents. Donc le graphe est biparti. 

**Bonus :** Pour dessiner les graphes, on peut utiliser __GraphViz__ (ce qui a été utilisé pour cet article). Voir cette [référence](https://fr.wikipedia.org/wiki/DOT_(langage)) pour une première approche.

