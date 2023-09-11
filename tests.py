from hypothesis import given, strategies as st
from algebra.cycles import str_to_perm, perm_to_str

@st.composite
def gen_perm(draw):
    n = 6
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
