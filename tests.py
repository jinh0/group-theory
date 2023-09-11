from hypothesis import given, strategies as st
from algebra.cycles import str_to_perm, perm_to_str, simplify

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

@given(gen_perm())
def test_inversion(perm):
    assert str_to_perm(perm_to_str(perm), 6) == perm

test_inversion()

assert simplify('(1 2 3 4)', 4) == '(1 2 3 4)'
assert simplify('(1 3 4)(1 2)(3 4)', 4) == '(1 2 3)'
assert simplify('(1 3)(1 2)(3 4)', 4) == '(1 2 3 4)'
