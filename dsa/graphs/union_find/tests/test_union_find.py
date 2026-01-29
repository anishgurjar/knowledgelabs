from union_find.union_find import UnionFind
import pytest

@pytest.mark.parametrize(
    "identity",
    [
        "email:anish@gmail.com",
        "phone:+1-614-555-0199",
        "github:anish123",
    ],
)
def test_single_element(identity):
    uf = UnionFind()
    assert uf.find(identity) == identity
    assert uf.connected(identity, identity) is True

def test_simple_union():
    uf = UnionFind()

    uf.union("email:anish@gmail.com", "phone:+1-614-555-0199")

    assert uf.connected(
        "email:anish@gmail.com",
        "phone:+1-614-555-0199"
    )

def test_transitive_union():
    uf = UnionFind()

    uf.union("email:anish@gmail.com", "google:anish123")
    uf.union("google:anish123", "phone:+1-614-555-0199")

    assert uf.connected(
        "email:anish@gmail.com",
        "phone:+1-614-555-0199"
    )

def test_disjoint_groups():
    uf = UnionFind()

    uf.union("email:a@gmail.com", "phone:111")
    uf.union("email:b@gmail.com", "phone:222")

    assert not uf.connected("email:a@gmail.com", "email:b@gmail.com")
    assert not uf.connected("phone:111", "phone:222")

def test_redundant_union():
    uf = UnionFind()

    uf.union("email:anish@gmail.com", "google:anish123")
    result = uf.union("google:anish123", "email:anish@gmail.com")

    assert result is False  # already connected

def test_non_string_keys():
    uf = UnionFind()

    uf.union(1, 2)
    uf.union(2, (3, 4))

    assert uf.connected(1, (3, 4))
