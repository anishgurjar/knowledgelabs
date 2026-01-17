import pytest
import vcr

from main import get_articles

my_vcr = vcr.VCR(
    cassette_library_dir="tests/cassettes",
    record_mode="once",  # first run hits the real API; later runs replay the cassette
    match_on=["method", "uri", "body"],
)


@my_vcr.use_cassette("get_articles.yaml")
def test_get_articles_with_vcr():
    """
    This test will:
    - On the first run: call the real API and save the HTTP interaction
      to tests/cassettes/get_articles.yaml
    - On later runs: replay the saved interaction from the cassette,
      without doing a real HTTP request.
    """
    data = get_articles()

    # Very light assertions because this is just for learning.
    # The point is to see that the same response is replayed from the cassette.
    assert data is not None
    assert isinstance(data, (dict, list))
