from algebra.cycles import perm_to_str, s, prod, str_to_perm

sigma = ['(1 2)(3 4)', '(1 3)(2 4)', '(1 4)(2 3)']
sigma_perms = list(map(lambda x : str_to_perm(x, 4), sigma))

image = set()
for perm in s(4):
    res = []
    for x in sigma_perms:
        res.append(perm_to_str(prod([perm, x], 4)))

    if all(x.count('(') == 2 for x in res):
        print(res)

print(image)
