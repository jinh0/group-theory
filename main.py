from algebra.perms import Perm, s

sigma = [Perm('(1 2)(3 4)'), Perm('(1 3)(2 4)'), Perm('(1 4)(2 3)')]

image = set()
for perm in s(4):
    res = []
    for x in sigma:
        res.append(perm * x)

    print(res)
