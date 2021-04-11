import pytest
from python_tooling_enterpy_2021.branch_coverage import my_partial_fn


@pytest.mark.parametrize(
    "x, response",
    [
        (1, 10),
        (True, 10),
    ],
)
def test_main(x, response):
    response = my_partial_fn(x)
    assert type(response) == int
    assert response == response


@pytest.mark.parametrize(
    "x, raise_error",
    [
        (False, UnboundLocalError),
        (None, UnboundLocalError),
    ],
)
def test_set_raw_datum_negative(x, raise_error):
    with pytest.raises(raise_error):
        my_partial_fn(x)
