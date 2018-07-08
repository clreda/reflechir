---
title: "5 bis. Arithmétique : corrigés"
date: 2018-07-08
bitlink: https://tinyurl.com/ycrjzzz3
---

Le premier exercice de l'article d'Arithmétique est de montrer que cette définition est correcte :  

__Déf__ : Soit $n \in \mathbb{N} \setminus {0,1}$. Soient $a_1,\dots,a_n \in \mathbb{N}$. Le plus grand commun diviseur de $a_1,\dots,a_n$, noté pgcd$(a_1,\dots,a_n)$, est l'entier $d \in \mathbb{N}$ qui vérifie $d$ divise $a_1, \dots, d$ divise $a_n$ et si $c$ divise $a_1, \dots, c$ divise $a_n$ alors $c$ divise $d$.  

Commençons par l'unicité :  
Si $d_1$ et $d_2$ vérifient les propriétés de pgcd de $a_1,\dots,a_n$ alors, comme $d_1$ divise $a_1, \dots, d_1$ divise $a_n$ on a $d_1$ divise $d_2$ et comme $d_2$ divise $a_1, \dots, d_2$ divise $a_n$ on a $d_2$ divise $d_1$.  
Si $d_1 = 0$ alors comme $d_1$ divise $d_2$ on a $d_2 = 0$. De même, si $d_2 = 0$ alors $d_1 = 0$.  
Si $d_1 \neq 0$ et $d_2 \neq 0$ alors on a $d_1 \leq d_2$ et $d_1 \geq d_2$ (car $d_1$ divise $d_2$ et $d_2$ divise $d_1$) donc on a $d_1 = d_2$.  
On a prouvé l'unicité du pgcd par disjonction de cas.  

On va prouver l'existence du pgcd par récurrence sur $n$.  
On a déjà prouvé l'existence pour $n = 2$.  
Supposons que le pgcd de $n-1$ nombres existe.  
On va vérifier que pgcd(pgcd$(a_1,\dots,a_{n-1}),a_n$) vérifie les conditions de la définition de pgcd$(a_1,\dots,a_n)$.  
On remarque tout d'abord que c'est bien un entier naturel. pgcd(pgcd$(a_1,\dots,a_{n-1}),a_n$) divise $a_n$ (cf. définition du pgcd). Soit $i \in {1,\dots,n-1}$. pgcd$(a_1,\dots,a_{n-1})$ divise $a_i$ et pgcd(pgcd$(a_1,\dots,a_{n-1}),a_n$) divise pgcd$(a_1,\dots,a_{n-1})$ donc pgcd(pgcd$(a_1,\dots,a_{n-1}),a_n$) divise $a_i$ (si vous avez le moindre doute, explicitez ce que je viens d'écrire avec la définition de \textquotedblleft diviser\textquotedblright). Soit $c \in \mathbb{N}$ tel que $c$ divise $a_1, \dots, c$ divise $a_n$. $c$ divise $a_1, \dots, c$ divise $a_{n-1}$ donc $c$ divise pgcd$(a_1,\dots,a_{n-1})$ (cf. la définition du pgcd). De plus, $c$ divise $a_n$, donc $c$ divise pgcd(pgcd$(a_1,\dots,a_{n-1}),a_n$) (cf. la définition du pgcd).  

Le deuxième exercice de l'article d'Arithmétique est de montrer que cette définition est correcte :  

__Déf__ : Soit $n \in \mathbb{N} \setminus {0,1}$. Soient $a_1,\dots,a_n \in \mathbb{N}$. Le plus petit commun multiple de $a_1,\dots,a_n$, noté ppcm$(a_1,\dots,a_n)$, est l'entier $m \in \mathbb{N}$ qui vérifie $a_1$ divise $m, \dots, a_n$ divise $m$ et si $a_1$ divise $c, \dots, a_n$ divise $c$ alors $m$ divise $c$.  

Commençons par l'unicité :  
Si $m_1$ et $m_2$ vérifient les propriétés de ppcm de $a_1,\dots,a_n$ alors, comme $a_1$ divise $m_1,\dots, a_n$ divise $m_1$ on a $m_2$ divise $m_1$ et comme $a_1$ divise $m_2,\dots, a_n$ divise $m_2$ on a $m_1$ divise $m_2$.  
Si $m_1 = 0$ alors comme $m_1$ divise $m_2$ on a $m_2 = 0$. De même, si $m_2 = 0$ alors $m_1 = 0$.  
Si $m_1 \neq 0$ et $m_2 \neq 0$ alors on a $m_1 \leq m_2$ et $m_1 \geq m_2$ (car $m_1$ divise $m_2$ et $m_2$ divise $m_1$) donc on a $m_1 = m_2$.  
On a prouvé l'unicité du ppcm par disjonction de cas.  

On va prouver l'existence du ppcm par récurrence sur $n$.  
On a déjà prouvé l'existence pour $n = 2$.  
Supposons que le ppcm de $n-1$ nombres existe.  
On va vérifier que ppcm(ppcm$(a_1,\dots,a_{n-1}),a_n$) vérifie les conditions de la définition de ppcm$(a_1,\dots,a_n)$.  
On remarque tout d'abord que c'est bien un entier naturel. $a_n$ divise ppcm(ppcm$(a_1,\dots,a_{n-1}),a_n$) (cf. définition du ppcm). Soit $i \in {1,\dots,n-1}$. $a_i$ divise ppcm$(a_1,\dots,a_{n-1})$ et ppcm$(a_1,\dots,a_{n-1})$ divise ppcm(ppcm$(a_1,\dots,a_{n-1}),a_n$) donc $a_i$ divise ppcm(ppcm$(a_1,\dots,a_{n-1}),a_n$) (si vous avez le moindre doute, explicitez ce que je viens d'écrire avec la définition de "diviser"). Soit $c \in \mathbb{N}$ tel que $a_1$ divise $c, \dots, a_n$ divise $c$. $a_1$ divise $c, \dots, a_{n-1}$ divise $c$ donc ppcm$(a_1,\dots,a_{n-1})$ divise $c$ (cf. la définition du pgcd). De plus, $a_n$ divise $c$, donc ppcm(ppcm$(a_1,\dots,a_{n-1}),a_n$) divise $c$ (cf. la définition du pgcd).  

Le troisième exercice de l'article d'Arithmétique est de démontrer le lemme suivant :  

Lemme : Soit $p$ un nombre premier. Soit $n \in \mathbb{N} \setminus {0}$. Soient $a_1,\dots,a_n \in \mathbb{N}$. Si $p$ divise $a_1 \times \dots \times a_n$ alors $p$ divise $a_1$ ou $\dots \ $ ou $p$ divise $a_n$.  

On fait un raisonnement par récurrence sur $n$.  

Le cas $n = 1$ est évident (c'est $p$ divise $a_1$ implique $p$ divise $a_1$).  

On démontre aussi le cas $n = 2$ parce qu'on va en avoir besoin dans la phase d'hérédité.  
Commençons par remarquer que comme $p$ est premier, pour tout $a \in \mathbb{N}$ pgcd$(p,a) = 1$ ou $p$ (en effet les seuls diviseurs de $p$ sont $1$ et $p$).  
Soient $a_1,a_2 \in \mathbb{N}$ tels que $p$ divise $a_1 \times a_2$.  
Si $p$ ne divise pas $a_1$ alors pgcd$(p,a_1) = 1$ (car ce ne peut pas être $p$ puisque $p$ ne divise pas $a_1$) donc, par le lemme de Gauss, $p$ divise $a_2$.  
Ainsi, $p$ divise $a_1$ ou $p$ divise $a_2$.  

Supposons que pour tous nombres naturels $b_1,\dots,b_{n-1}$ on a $p$ divise $b_1 \times \dots \times b_{n-1}$ implique $p$ divise $b_1$ ou $\dots \ $ ou $p$ divise $b_{n-1}$.  
Soient $a_1,\dots,a_n \in \mathbb{N}$ tels que $p$ divise $a_1 \times \dots \times a_n$.  
D'après la phase d'initialisation, si $p$ ne divise pas $a_n$ alors $p$ divise $a_1 \times \dots \times a_{n-1}$ donc, d'après l'hypothèse de récurrence, $p$ divise $a_1$ ou $\dots \ $ ou $p$ divise $a_{n-1}$.  
Ainsi, $p$ divise $a_1$ ou $\dots \ $ ou $p$ divise $a_n$.  

__Exo__ : Résolution de l'équation de Pythagore $x^2 + y^2 = z^2$ avec $x,y,z \in \mathbb{N} \setminus \{0\}$.  

1) Soit $c \in \mathbb{N} \setminus \{0\}$. Montrer que $(x,y,z)$ est un triplet pythagoricien si et seulement si $(cx,cy,cz)$ est un triplet pythagoricien.  

Si $(x,y,z)$ est un triplet pythagoricien on a : $x^2 + y^2 = z^2$ d'où $c^2 \times (x^2 + y^2) = c^2 \times z^2$ d'où $c^2 \times x^2 + c^2 \times y^2 = c^2 \times z^2$ d'où $(cx)^2 + (cy)^2 = (cz)^2$.  
Si $(cx,cy,cz)$ est un triplet pythagoricien on a : $(cx)^2 + (cy)^2 = (cz)^2$ d'où $c^2 \times x^2 + c^2 \times y^2 = c^2 \times z^2$ d'où $c^2 \times (x^2 + y^2) = c^2 \times z^2$ d'où, en simplifiant par $c^2$, $x^2 + y^2 = z^2$.  

2) Montrer, à l'aide de la question précédente, que les triplets pythagoriciens sont exactement les triplets de la forme $(cx,cy,cz)$ avec $(x,y,z)$ triplet pythagoricien de pgcd $1$ et $c \in \mathbb{N} \setminus \{0\}$.  

Soit $(s,t,u)$ un triplet pythagoricien. Posons $c =$ pgcd$(s,t,u)$. Il existe $x,y,z \in \mathbb{N} \setminus \{0\}$ tels que $s = cx, t = cy, u = cz$. $(cx,cy,cz)$ est un triplet pythagoricien donc, d'après la question précédente, $(x,y,z)$ est un triplet pythagoricien, or pgcd$(x,y,z) = \frac{\text{pgcd}(s,t,u)}{c} = 1$, donc on a bien que les triplets pythagoriciens sont de la forme voulue.  
Soit $(x,y,z)$ un triplet pythagoricien de pgcd $1$. Soit $c \in \mathbb{N} \setminus \{0\}$. D'après la question précédente, $(cx,cy,cz)$ est un triplet pythagoricien.  

3) Soit $m \in \mathbb{N} \setminus \{0\}$. Montrer que, dans la division euclidienne par $4$, $m^2$ a pour reste $0$ ou $1$.  

$m = 4q + r$ avec $r \in \{0,1,2,3\}$. $m^2 = (4q + r)(4q + r) = 4(4q^2 + 2qr) + r^2$, donc si $r = 0$ alors le reste de $m^2$ est $0$ (car $0^2 = 0$), si $r = 1$ alors le reste de $m^2$ est $1$ (car $1^2 = 1$), si $r = 2$ alors $m^2 = 4(4q^2 + 4q + 1)$ (car $2^2 = 4$) donc le reste de $m^2$ est $0$, si $r = 3$ alors $m^2 = 4(4q^2 + 6q + 2) + 1$ (car $3^2 = 9 = 4 \times 2 + 1$) donc le reste de $m^2$ est $1$.  

4) Soit $(x,y,z)$ un triplet pythagoricien de pgcd 1. Déterminer le reste dans la division euclidienne de $z^2$ par 4 et en déduire que $z$ est impair, puis que si $x$ est pair alors $y$ est impair et que si $x$ est impair alors $y$ est pair.  

Si $4$ divise $x^2$ et $y^2$ alors $4$ divise $x^2 + y^2 = z^2$, ce qui contredit pgcd$(x^2,y^2,z^2) = 1$ (qui découle de pgcd$(x,y,z) = 1$). Ainsi, $4$ ne divise pas à la fois $x^2$ et $y^2$ (n'hésitez pas à réviser le raisonnement par l'absurde (cf. l'article 3)).  
Le reste dans la division euclidienne de $z^2$ par $4$ ne peut donc pas être $0$ (car si $x^2 = 4q_1 + r_1$ et $y^2 = 4q_2 + r_2$ alors $z^2 = x^2 + y^2 = 4(q_1 + q_2) + r_1 + r_2$ or d'après la question précédente, $r_1, r_2 \in \{0,1\}$ et on vient de montrer qu'on n'a pas à la fois $r_1 = 0$ et $r_2 = 0$) donc, d'après la question précédente, le reste dans la division euclidienne de $z^2$ par $4$ est $1$.  
Il existe donc $q \in \mathbb{N}$ tel que $z^2 = 4q + 1 = 2 \times 2q + 1$ donc $z^2$ est impair (c'est-à-dire que $z^2$ n'est pas divisible par $2$) donc $z$ est impair (car si $2$ divise $z$ alors $2$ divise $z^2 = z \times z$).  
Si $x^2$ et $y^2$ sont pairs alors $z^2 = x^2 + y^2 = 2s_1 + 2s_2 = 2 \times (s_1 + s_2)$ est pair, ce qui contredit ce qui vient d'être démontré, donc on n'a pas à la fois $x^2$ et $y^2$ pairs.  
Si $x^2$ et $y^2$ sont impairs alors $z^2 = x^2 + y^2 = 2s_1 + 1 + 2s_2 + 1 = 2 \times (s_1 + s_2 + 1)$ est pair, ce qui contredit ce qui vient d'être démontré, donc on n'a pas à la fois $x^2$ et $y^2$ impairs.  
Il suffit de remarquer que pour tout $m \in \mathbb{N}$ $m^2$ est pair si et seulement si $m$ est pair pour conclure; ce dernier fait se démontre comme suit : $m^2$ impair implique $m$ pair se fait de la même manière que plus haut, et $m^2$ pair implique $m$ pair découle du lemme démontré plus haut (le troisième exercice), du fait que $2$ est premier et du fait que $m^2 = m \times m$.  

5) Soit $(x,y,z)$ un triplet pythagoricien de pgcd $1$ avec $x$ pair. Montrer que pgcd$(\frac{z-y}{2},\frac{z+y}{2}) = 1$. En déduire, puisque $(z-y)(z+y) = z^2 - y^2 = x^2$, que $\frac{z-y}{2}$ et $\frac{z+y}{2}$ sont des carrés d'entiers, puis une expression de $x$, $y$ et $z$.  

On remarque tout d'abord que d'après la question précédente $z$ et $y$ sont impairs (car $x$ est pair) donc $z - y$ et $z + y$ sont pairs (et $z - y \geq 0$ car $z^2 - y^2 = x^2 \geq 0$ et $z$ et $y$ sont des entiers naturels) donc $\frac{z-y}{2}$ et $\frac{z+y}{2}$ sont bien des entiers naturels.  
Si pgcd$(\frac{z-y}{2},\frac{z+y}{2}) > 1$ alors il existe un nombre premier $p$ qui divise $\frac{z-y}{2}$ et $\frac{z+y}{2}$ (il suffit de prendre $p$ un facteur premier de pgcd$(\frac{z-y}{2},\frac{z+y}{2})$).  
Il existe donc $a,b \in \mathbb{N}$ tels que $\frac{z-y}{2} = ap$ et $\frac{z+y}{2} = bp$, c'est-à-dire :  
$z-y = 2ap,\ z+y = 2bp.$
En additionnant ces deux égalités on a : $2z = 2p(a+b)$ c'est-à-dire :  
$z = p(a+b)$. En soustrayant la première égalité à la deuxième on a :  
$2y = 2p(b-a)$ c'est-à-dire $y = p(b-a)$.  
Ainsi, $p$ divise $y$ et $z$ donc divise $z^2-y^2 = x^2$ donc divise $x$ (car $p$ est premier), et $x,y,z$ ont un facteur premier en commun, ce qui contredit pgcd$(x,y,z) = 1$.  
Ainsi, pgcd$(\frac{z-y}{2},\frac{z+y}{2}) = 1$.    
$\left(\frac{z-y}{2}\right)\left(\frac{z+y}{2}\right) = \frac{1}{4} (z-y)(z+y) = \frac{1}{4} x^2 = \left(\frac{x}{2}\right)^2$
donc $\left(\frac{z-y}{2}\right)\left(\frac{z+y}{2}\right)$ est un carré d'entier ($x$ est pair donc $\frac{x}{2}$ est un entier).  
Or $\frac{z-y}{2}$ et $\frac{z+y}{2}$ sont premiers entre eux (on a montré plus haut que leur pgcd est $1$) donc ce sont des carrés d'entiers.  
En effet, $\left(\frac{z-y}{2}\right)\left(\frac{z+y}{2}\right)$ est un carré d'entier implique que pour tout nombre premier $p$ la valuation $p$-adique de $\left(\frac{z-y}{2}\right)\left(\frac{z+y}{2}\right)$ est paire, or $0 = v_p(1) = v_p($pgcd$(\frac{z-y}{2},\frac{z+y}{2})) =$ min$(v_p(\frac{z-y}{2}),v_p(\frac{z+y}{2}))$ et $v_p(\left(\frac{z-y}{2}\right)\left(\frac{z+y}{2}\right)) = v_p(\frac{z-y}{2}) + v_p(\frac{z+y}{2})$ donc $v_p(\frac{z-y}{2})$ ou $v_p(\frac{z+y}{2})$ est égale à $v_p(\left(\frac{z-y}{2}\right)\left(\frac{z+y}{2}\right))$ qui est paire et l'autre est nulle donc paire. On a montré que pour tout $p$ premier, $v_p(\frac{z-y}{2})$ et $v_p(\frac{z-y}{2})$ sont paires, donc $\frac{z-y}{2}$ et $\frac{z+y}{2}$ sont des carrés d'entiers  
(car $p_1^{2k_1} \times \dots \times p_r^{2k_r} = (p_1^{k_1})^2 \times \dots \times (p_r^{k_r})^2 = (p_1^{k_1} \times \dots \times p_r^{k_r})^2$).  
Il existe donc des entiers naturels $u$ et $v$ tels que $\frac{z-y}{2} = u^2$ et $\frac{z+y}{2} = v^2$.  
Ainsi $z-y = 2u^2$ et $z+y = 2v^2$ et on a, en sommant ces deux égalités et en soustrayant la première égalité à la deuxième égalité :  
$2z = 2(u^2+v^2)$ et $2y = 2(v^2-u^2)$. En simplifiant par $2$ on a :  
$z = u^2+v^2$ et $y = v^2-u^2$.  
De plus on a : $x^2 = z^2 - y^2 = (u^2+v^2)^2 - (v^2-u^2)^2$ donc :  
$x^2 = u^4 + v^4 + 2u^2v^2 - v^4 - u^4 + 2u^2v^2 = 4u^2v^2 = (2uv)^2$
or $x$ et $2uv$ sont positifs donc $x = 2uv$.  

6) Donner tous les triplets pythagoriciens.  

On a montré en répondant à la question précédente que si $(x,y,z)$ est un triplet pythagoricien de pgcd $1$ avec $x$ pair alors il existe $u,v \in \mathbb{N}$ tels que $x = 2uv, y = v^2 - u^2, z = v^2 + u^2$.  
Avec la question 4) on a que si $(x,y,z)$ est un triplet pythagoricien de pgcd $1$ avec $x$ pair alors $y$ est pair et, de même que précédemment, il existe $u,v \in \mathbb{N}$ tels que $y = 2uv, x = v^2 - u^2, z = v^2 + u^2$.  
On remarque que dans les deux cas $v \geq u$ (car $x$ et $y$ sont positifs).  
On remarque aussi que $u \neq 0$, $v \neq 0$ et $v \neq u$ (car $x \neq 0$ et $y \neq 0$).  
Avec la question 2) on a que tous les triplets pythagoriciens sont de la forme $(cx,cy,cz)$ avec $(x,y,z)$ un triplet pythagoricien de pgcd $1$ et $c \in \mathbb{N} \setminus \{0\}$ donc, avec ce qui précède, de la forme $(2cuv,c(v^2-u^2),c(v^2+u^2))$ ou $(c(v^2-u^2),2cuv,c(v^2+u^2))$ avec $c,u,v \in \mathbb{N} \setminus \{0\}$ et $v > u$.  
Il nous suffit maintenant de vérifier que si $c,u,v \in \mathbb{N} \setminus \{0\}$ vérifient $v > u$ alors $(2cuv,c(v^2-u^2),c(v^2+u^2))$ et $(c(v^2-u^2),2cuv,c(v^2+u^2))$ sont des triplets pythagoriciens.    
$(2cuv)^2 + (c(u^2-v^2))^2 = 4c^2u^2v^2 + c^2u^4 + c^2v^4 - 2c^2u^2v^2 = c^2u^4 + c^2v^4 + 2c^2u^2v^2 = (c(u^2+v^2))^2$
et $2cuv, c(v^2-u^2), c(v^2+u^2) \in \mathbb{N} \setminus \{0\}$ donc $(2cuv,c(v^2-u^2),c(v^2+u^2))$ et $(c(v^2-u^2),2cuv,c(v^2+u^2))$ sont bien des triplets pythagoriciens.  

__Exo__ : Si $x,y,z \in \mathbb{Z} \setminus \{0\}$ vérifient $x^2 + y^2 = z^2$, en remplaçant $x$ par $-x$ ou $y$ par $-y$ ou $z$ par $-z$ on a encore $x^2 + y^2 = z^2$ et $x,y,z \in \mathbb{Z} \setminus \{0\}$. En changeant les signes qu'il faut, on se ramène à $x,y,z \in \mathbb{N} \setminus \{0\}$, et l'exercice précédent nous donne donc tous les $x,y,z \in \mathbb{Z} \setminus \{0\}$ qui vérifient $x^2 + y^2 = z^2$ en changeant des signes (explicitez ces solutions).  

Les $x,y,z \in \mathbb{Z} \setminus \{0\}$ tels que $x^2 + y^2 = z^2$ sont exactement les $(2cuv,c(v^2-u^2),c(v^2+u^2))$, $(-2cuv,c(v^2-u^2),c(v^2+u^2))$, $(2cuv,-c(v^2-u^2),c(v^2+u^2))$, $(2cuv,c(v^2-u^2),-c(v^2+u^2))$,$(2cuv,-c(v^2-u^2),-c(v^2+u^2))$, $(-2cuv,c(v^2-u^2),-c(v^2+u^2))$, $(-2cuv,-c(v^2-u^2),c(v^2+u^2))$,$(-2cuv,-c(v^2-u^2),-c(v^2+u^2))$ et $(c(v^2-u^2),2cuv,c(v^2+u^2))$, $(c(v^2-u^2),-2cuv,c(v^2+u^2))$, $(-c(v^2-u^2),2cuv,c(v^2+u^2))$, $(c(v^2-u^2),2cuv,-c(v^2+u^2))$,$(-c(v^2-u^2),2cuv,-c(v^2+u^2))$, $(c(v^2-u^2),-2cuv,-c(v^2+u^2))$, $(-c(v^2-u^2),-2cuv,c(v^2+u^2))$,$(-c(v^2-u^2),-2cuv,-c(v^2+u^2))$ avec $c,u,v \in \mathbb{N} \setminus \{0\}$ et $v > u$.  

__Exo__ : Pour prouver que pour tout $n \geq 3$ il n'existe pas $x,y,z \in \mathbb{Z} \setminus \{0\}$ tels que $x^n + y^n = z^n$ il suffit de le montrer pour $n = 3, n = 4$ et $n \geq 5$ premier.  

Soit $n \geq 5$. Décomposons $n$ en facteurs premiers : $n = p_1^{a_1} \times \dots \times p_m^{a_m}$ où $p_1, \dots, p_m$ sont des nombres premiers distincts et $a_1,\dots, a_m \in \mathbb{N} \setminus \{0\}$.  
Si $n$ n'est pas une puissance de $2$ : $m > 1$ ou $p_1 \neq 2$ (et dans le premier cas quitte à échanger $p_1$ et $p_2$ on peut supposer $p_1 \neq 2$), si $x^n + y^n = z^n$ avec $x,y,z \in \mathbb{Z} \setminus \{0\}$ alors $(x^{\frac{n}{p_1}})^{p_1} + (y^{\frac{n}{p_1}})^{p_1} = (z^{\frac{n}{p_1}})^{p_1}$ et $x^{\frac{n}{p_1}} ,y^{\frac{n}{p_1}} ,z^{\frac{n}{p_1}}  \in \mathbb{Z} \setminus \{0\}$. Or $p_1 \neq 2$ donc $p_1 = 3$ ou $p_1 \geq 5$ premier : on est bien ramené aux cas voulus (si on a une solution pour $n$ alors on a une solution pour $p_1$, donc si on a déjà montré qu'il n'y a pas de solution pour $p_1$ alors on a aussi qu'il n'y a pas de solution pour $n$).  
Sinon, $n = 2^a$ avec $a \in \mathbb{N} \setminus \{0\}$. Si $a = 1$ alors $n = 2$ ce qui contredit $n \geq 5$, donc $a \geq 2$, or $2^2 = 4$ donc $4$ divise $n$ : $n = 4q$. Si $x^n + y^n = z^n$ avec $x,y,z \in \mathbb{Z} \setminus \{0\}$ alors $(x^q)^4 + (y^q)^4 = (z^q)^4$ et $x^q,y^q,z^q \in \mathbb{Z} \setminus \{0\}$ : on est bien ramené aux cas voulus (si on a une solution pour $n$ alors on a une solution pour $4$, donc si on a déjà montré qu'il n'y a pas de solution pour $4$ alors on a aussi qu'il n'y a pas de solution pour $n$).  

Pour le cas $n = 4$ on montre même qu'il n'y a pas de solution dans $\mathbb{N} \setminus \{0\}$ à $x^4+y^4=z^2$ (ce qui implique le cas $n = 4$ en prenant $z$ un carré d'entier).  
En effet, si on avait $x^4 + y^4 = c^4$ avec $x,y,c \in \mathbb{Z} \setminus \{0\}$ alors on aurait $x^4 + y^4 = (c^2)^2$ avec $x,y,c^2 \in \mathbb{N} \setminus \{0\}$ (quitte à changer les signes de $x$ et $y$).  

__Exo__ : Il n'y a pas de solution dans $\mathbb{N} \setminus \{0\}$ à $x^4+y^4=z^2$.  

Je mets à jour cet article dès que j'ai fini de taper le corrigé de cet exercice.  

__Exo__ : Il n'y a pas de solution dans $\mathbb{Z} \setminus \{0\}$ à $x^3+y^3=z^3$.  

Je mets à jour cet article dès que j'ai fini de taper le corrigé de cet exercice.  

Clémentine Lemarié--Rieusset
