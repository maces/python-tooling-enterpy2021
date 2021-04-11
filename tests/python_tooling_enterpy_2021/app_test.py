from python_tooling_enterpy_2021.app import main


def test_main():
    response = main()
    assert type(response) == str
    assert response == "Hello World!"
