#!/usr/bin/env python3
from invoke import Collection, task
from invoke.executor import Executor
from invoke.exceptions import UnexpectedExit
from dotenv import load_dotenv

from tasks import format, check, test


# This is a simple pre commit hok leveraging the invoke tasks
# For a more advanced solution have a look at https://pre-commit.com/
# To use tasks:
# 1. Import the task
# 2. Add the task to the namespace
# 3. Execute the task


# adds the environment variables like PYTHONPATH for tests ect.
load_dotenv(override=True, verbose=True)


@task
def stash_changes(c):  # , stash_name: str):
    """
    Backup uncommited chnages before pre-commit is run.
    Only works in a pre-commit context.
    """
    c.run(f"git stash push -q --keep-index")


@task
def stage_changes(c):
    """
    Stage the newly changed files only.
    Only works in a pre-commit context.
    """
    c.run(f"git add -u")


# Until invoke has proper support for prgramatic accsess
# see https://github.com/pyinvoke/invoke/issues/170 for details
namespace = Collection(stash_changes, stage_changes, format, check, test)
namespace.configure({"root_namespace": namespace})
executor = Executor(namespace)

try:
    executor.execute("stash_changes")  # will be deleted in post-commit on success
    executor.execute("format")
    executor.execute("check")
    executor.execute("test")
    executor.execute("stage_changes")
except UnexpectedExit:
    print("\n\n[ERROR]] Pre-commit hook failed, commit aborted!")
    print("[ERROR]] Working directory contains files potentially changed by pre-commit hook")
    print("[ERROR]] Unaltered changes can be found in latest stash: 'git stash list'")
    print("[ERROR]] Cleanup of he stashes may be needed after failure")
    exit(1)
