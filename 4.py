def getSortedString(s, n):
    v1=[]
    v2=[]
    v3=[]
    for i in range(n):
        if (s[i] >= 'a' and s[i] <= 'z'):
            v1.append(s[i])
        if (s[i] >= 'A' and s[i] <= 'Z'):
			v2.append(s[i])
        if (s[i] >= '0' and s[i] <= '9'):
			v3.append(s[i])

	v1=sorted(v1)
	v2=sorted(v2)
    v3=sorted(v3)
	i = 0
	j = 0
    p = 0
	for k in range(n):
		if (s[k] >= 'a' and s[k] <= 'z'):
			s[k] = v1[i]
			i+=1

		elif (s[k] >= 'A' and s[k] <= 'Z'):
			s[k] = v2[j]
			j+=1

        elif (s[k] >= '0' and s[k] <= '9'):
			s[k] = v3[i]
			p+=1

	return "".join(s)

s = "cC3bB2aA1"
ss=[i for i in s]
n = len(ss)

print(getSortedString(ss, n))

# This code is contributed by mohit kumar 29
