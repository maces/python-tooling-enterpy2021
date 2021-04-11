from fastapi.testclient import TestClient
import pytest

from python_tooling_enterpy_2021.main import app

client = TestClient(app)


@pytest.mark.parametrize(
    "id, code, resp",
    [
        ("foo", 200, "foobar"),
        ("bar", 200, "barfoo"),
        ("notfound", 404, {"detail": "Item not found"}),
    ],
)
def test_read_db(id, code, resp):
    response = client.get(f"/{id}")
    assert response.status_code == code
    assert response.json() == resp
