from pathlib import Path
import platform
from invoke import task
from dotenv import load_dotenv

# http://docs.pyinvoke.org/en/stable/getting-started.html


@task
def test(c):
    """
    Execute tests
    """
    # adds the environment variables like PYTHONPATH for tests ect.
    load_dotenv(override=True, verbose=True)
    c.run("pytest --cov-report=html --cov-report=term .")


@task
def format(c):
    """
    Sort imports and format the code.
    """
    c.run("isort python_tooling_enterpy_2021")
    c.run("black python_tooling_enterpy_2021 tests")


@task
def check(c):
    """
    Check code with pylint, bandit and safety.
    """
    c.run("mypy python_tooling_enterpy_2021")
    c.run(f"pylint {Path('python_tooling_enterpy_2021') / '*'}")
    c.run("poetry export -f requirements.txt | safety check --stdin")
    c.run("bandit -r python_tooling_enterpy_2021")


@task
def docs(c):
    """
    Generate documentation and serve it.
    """
    load_dotenv(override=True, verbose=True)
    c.run("mkdocs serve")


@task
def build(c):
    """
    Build the docker image
    """
    p = Path("build")
    p.mkdir(parents=True, exist_ok=True)
    c.run(f"poetry export -f requirements.txt --output {p / 'requirements.txt'}")
    c.run("docker build --tag python_tooling_enterpy_2021-app .")


@task
def run(c):
    """
    RUN the docker image
    """
    c.run("docker run -it --rm --name python_tooling_enterpy_2021-app python_tooling_enterpy_2021-app /bin/bash", pty=True)


@task
def install_hooks(c):
    """
    Install the git hooks
    """

    script_directory = Path(__file__).resolve().parent
    current_platform = platform.system()
    if current_platform in ['Linux', 'Darwin']:
        c.run(f"rm {script_directory / '.git' / 'hooks' / 'pre-commit'} || true", hide=True)
        c.run(f"rm {script_directory / '.git' / 'hooks' / 'post-commit'} || true", hide=True)
        c.run(f"ln -s {script_directory / 'tools' / 'pre-commit.sh'} {script_directory / '.git' / 'hooks' / 'pre-commit'}", hide=True)
        c.run(f"ln -s {script_directory / 'tools' / 'post-commit.sh'} {script_directory / '.git' / 'hooks' / 'post-commit'}", hide=True)
        c.run(f"chmod +x {script_directory / '.git' / 'hooks' / 'pre-commit'}", hide=True)
        c.run(f"chmod +x {script_directory / '.git' / 'hooks' / 'post-commit'}", hide=True)
    elif current_platform == 'Windows':
        print("Try at your own risk")
        c.run(f"del {script_directory / '.git' / 'hooks' / 'pre-commit'}", warn=True, hide=True)
        c.run(f"del {script_directory / '.git' / 'hooks' / 'post-commit'}", warn=True, hide=True)
        c.run(f"mklink {script_directory / '.git' / 'hooks' / 'pre-commit'} {script_directory / 'tools' / 'pre-commit.bat'}", hide=True)
        c.run(f"mklink {script_directory / '.git' / 'hooks' / 'post-commit'} {script_directory / 'tools' / 'post-commit.bat'}", hide=True)
    else:
        print("[ERROR] Platform not supported")
