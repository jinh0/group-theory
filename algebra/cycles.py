import itertools

Perm = dict[int, int]

def str_to_perm(perm_str: str) -> Perm:
    cycles = [parse_cycle(x) for x in perm_str[1:-1].split(')(')]
    return prod(cycles)

def parse_cycle(cycle_str: str) -> Perm:
    elems = list(map(int, cycle_str.split(' ')))

    perm = {}
    for i in range(len(elems) - 1):
        perm[elems[i]] = elems[i + 1]

    perm[elems[-1]] = elems[0]

    return perm

def prod(cycles: list[Perm]):
    res = {}
    for cycle in reversed(cycles):
        for x in res:
            if res[x] in cycle:
                res[x] = cycle[res[x]]

        for x in set(cycle.keys()) - set(res.keys()):
            res[x] = cycle[x]

    return res

# NOTE: The cycles in the string are sorted!!!
def perm_to_str(perm: Perm):
    # Cycle detection DFS
    cycles: list[list[int]] = []
    visited = set()

    perm = dict(sorted(perm.items()))

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

def evaluate(perm_str: str) -> str:
    return perm_to_str(str_to_perm(perm_str))

def s(n: int) -> list[Perm]:
    res = []
    for perm in itertools.permutations(range(1, n + 1)):
        res.append({i + 1: perm[i] for i in range(n)})

    return res
