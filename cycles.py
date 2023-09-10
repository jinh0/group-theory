import itertools

Perm = dict[int, int]

def str_to_perm(perm_str: str, n: int) -> Perm:
    cycles = perm_str[1:-1].split(')(')
    return prod(
        [parse_cycle(cycle, n) for cycle in cycles], n
    )

def parse_cycle(cycle_str: str, n: int) -> Perm:
    elems = list(map(int, cycle_str.split(' ')))
    perm = {i: i for i in range(1, n + 1)}
    for i in range(len(elems) - 1):
        perm[elems[i]] = elems[i + 1]

    perm[elems[-1]] = elems[0]

    return perm

def prod(cycles: list[Perm], n: int):
    res = {i: i for i in range(1, n + 1)}
    for cycle in reversed(cycles):
        for x in res:
            res[x] = cycle[res[x]]

    return res

def perm_to_str(perm: Perm):
    # Cycle detection DFS
    cycles: list[list[int]] = []
    visited = set()

    def dfs(x, cycle):
        if x in visited:
            cycles.append(cycle)
            return

        visited.add(x)
        dfs(perm[x], cycle + [x])

    for x in perm:
        if x not in visited:
            dfs(x, [])

    n_cycles = [c for c in cycles if len(c) > 1]
    
    if not n_cycles:
        return '(1)'

    stringify = lambda l : ' '.join(map(str, l))
    return '(' + ')('.join(map(stringify, n_cycles)) + ')'

def simplify(perm_str: str, n: int) -> str:
    return perm_to_str(str_to_perm(perm_str, n))

def s(n: int) -> list[str]:
    res = []
    for perm in itertools.permutations(range(1, n + 1)):
        res.append({i + 1: perm[i] for i in range(n)})

    return list(map(perm_to_str, res))

print(simplify('(1 3 4)(1 2)(3 4)', 4))
# print(s(4))
