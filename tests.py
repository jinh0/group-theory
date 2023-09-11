from hypothesis import given, strategies as st
from algebra.perms import Perm

@st.composite
def gen_perm(draw):
    n = draw(st.integers(min_value=1, max_value=10))
    xs = draw(
        st.lists(
            st.integers(min_value=1, max_value=n),
            unique=True, min_size=n, max_size=n
        )
    )

    return Perm(dict(zip(range(1, n + 1), xs)))

@given(gen_perm())
def test_inversion(perm: Perm):
    assert Perm(str(perm)) == perm

test_inversion()

assert Perm('(1 2 3 4)') == Perm('(1 2 3 4)')
assert Perm('(1 3 4)(1 2)(3 4)') == Perm('(1 2 3)')
assert Perm('(1 3)(1 2)(3 4)') == Perm('(1 2 3 4)')
