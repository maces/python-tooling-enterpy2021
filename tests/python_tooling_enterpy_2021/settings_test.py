def test_decouple():
    from python_tooling_enterpy_2021.settings_decouple import PORT, DOMAIN, ROOT_URL, DEBUG

    assert type(PORT) == int
    assert type(DOMAIN) == str
    assert type(ROOT_URL) == str
    assert type(DEBUG) == bool

    assert PORT == 8080
    assert DOMAIN == "example.org"
    assert ROOT_URL == "example.org/app"  # Set by invoke task
    assert DEBUG == False


def test_dotenv():
    from python_tooling_enterpy_2021.settings_dotenv import PORT, DOMAIN, ROOT_URL, DEBUG

    assert type(PORT) == int
    assert type(DOMAIN) == str
    assert type(ROOT_URL) == str
    assert type(DEBUG) == bool

    assert PORT == 8080
    assert DOMAIN == "example.org"
    assert ROOT_URL == "example.org/app"
    assert DEBUG == True  # is it? ;)
