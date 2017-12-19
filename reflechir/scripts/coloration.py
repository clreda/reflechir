# -*- coding: utf-8 -*-

def trouver_coloration(S,A):
	if (len(S)==0):
		return(0)
	col=[None]*len(S)
	m = 1
	if (len(A)==0):
		return(m)
	i = 0
	while (any([v==None for v in col]) and i < len(S)):
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

S=["Mathématiques", "Français", "Histoire", "SVT", "Physique"]
A=[["Mathématiques", "Français"], ["Histoire", "SVT"], ["SVT", "Physique"]]
print(trouver_coloration(S, A))


