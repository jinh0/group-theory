import itertools
from functools import reduce

class Perm:
    perm: dict[int, int]

    def __init__(self, perm: 'dict[int, int] | str' = None):
        if not perm:
            self.perm = {}
        elif isinstance(perm, str):
            self.perm = Perm.fromstr(perm)
        else:
            self.perm = perm

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Perm):
            return False

        return self.norm() == other.norm()

    # Without the number of elements, in order to compare permutations,
    # we must "normalize" them, i.e., get rid of 1-cycles
    def norm(self):
        return {k: self.perm[k] for k in self.perm if self.perm[k] != k}

    @classmethod
    def fromstr(cls, perm_str: str):
        cycles = [cls.parse_cycle(x) for x in perm_str[1:-1].split(')(')]
        return reduce(compose, cycles, {})

    @classmethod
    def parse_cycle(cls, cycle_str: str):
        elems = list(map(int, cycle_str.split(' ')))

        perm = {
            elems[i]: elems[i + 1]
            for i in range(len(elems) - 1)
        }
        perm[elems[-1]] = elems[0]

        return perm

    def __len__(self) -> int:
        return len(self.norm())

    def __repr__(self) -> str:
        cycles: list[list[int]] = []
        visited = set()

        # Detect disjoint cycles by DFS
        def dfs(x, cycle):
            if x in visited:
                cycles.append(cycle)
                return

            visited.add(x)
            dfs(self.perm[x], cycle + [x])

        # Note: we sort the permutation; e.g, (1 2 3) not (3 1 2)
        for x in dict(sorted(self.perm.items())):
            if x not in visited:
                dfs(x, [])

        n_cycles = [c for c in cycles if len(c) > 1]
        
        if not n_cycles:
            return '(1)'

        stringify = lambda l : ' '.join(map(str, l))
        return '(' + ')('.join(map(stringify, n_cycles)) + ')'

    def __str__(self) -> str:
        return self.__repr__()

    def __mul__(self, other: object) -> 'Perm':
        if not isinstance(other, Perm):
            raise Exception('Not allowed')

        return Perm(compose(self.perm, other.perm))

# Return the symmetric group S_n
def s(n: int) -> list[Perm]:
    res: list[Perm] = []
    for perm in itertools.permutations(range(1, n + 1)):
        res.append(Perm({i + 1: perm[i] for i in range(n)}))

    return res

def compose(g: dict[int, int], f: dict[int, int]) -> dict[int, int]:
    res = {}
    for x in f:
        if f[x] in g:
            res[x] = g[f[x]]
        else:
            res[x] = f[x]

    for x in set(g.keys()) - set(f.keys()):
        res[x] = g[x]

    return res
