from hypothesis import given, strategies as st
from algebra.cycles import str_to_perm, perm_to_str, evaluate

@st.composite
def gen_perm(draw):
    n = draw(st.integers(min_value=1, max_value=10))
    xs = draw(
        st.lists(
            st.integers(min_value=1, max_value=n),
            unique=True, min_size=n, max_size=n
        )
    )

    return dict(zip(range(1, n + 1), xs))

# Without the number of elements, in order to compare permutations,
# we must "normalize" them, i.e., get rid of 1-cycles
def norm(perm: dict[int, int]):
    return {k: perm[k] for k in perm if perm[k] != k}

@given(gen_perm())
def test_inversion(perm):
    assert norm(str_to_perm(perm_to_str(perm))) == norm(perm)

test_inversion()

assert evaluate('(1 2 3 4)') == '(1 2 3 4)'
assert evaluate('(1 3 4)(1 2)(3 4)') == '(1 2 3)'
assert evaluate('(1 3)(1 2)(3 4)') == '(1 2 3 4)'
