li = [1,2,3,4,5,1,2,3,4,5]
d = {}
for _ in li:
	if _ in d:
		d[_].append(1)
	else:
		d[_] = [1]

print(d)