from itertools import permutations
l= list(map(int,input().split(",")))
k=int(input())
perm = permutations(l,k)
for i in list(perm):
	print (i)
