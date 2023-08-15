from invoke import Collection, task


@task
def release(c):
    c.run("")


@task
def build_dev(c):
    c.run("")


@task
def format_black(c):
    c.run("black app db tests utils")


@task
def format_isort(c):
    c.run("isort app db tests utils")


@task
def format_autopep(c):
    c.run("autopep8 --in-place --recursive app db tests utils")


@task
def format_yapf(c):
    c.run("yapf --recursive --in-place app db tests utils")


@task(format_black, format_isort, format_autopep, format_yapf)
def format_all(c):
    pass


@task
def lint_black(c):
    c.run("black app db tests utils --check")


@task
def lint_mypy(c):
    c.run("mypy app db tests utils")


@task
def lint_flake8(c):
    c.run("flake8 app db tests utils")


@task(lint_black, lint_mypy, lint_flake8)
def lint_all(c):
    pass


@task
def test_unit(c):
    c.run("")


@task(test_unit)
def test_all(c):
    c.run("")


# Root collection namespace
ns = Collection()
ns.add_task(release)

# Collections
build = Collection("build")
test = Collection("test")
format = Collection("format")
lint = Collection("lint")
ns.add_collection(build)
ns.add_collection(test)
ns.add_collection(format)
ns.add_collection(lint)

# Tasks
build.add_task(build_dev, "dev")

format.add_task(format_black, "black")
format.add_task(format_isort, "isort")
format.add_task(format_autopep, "autopep")
format.add_task(format_yapf, "yapf")
format.add_task(format_all, "all")

lint.add_task(lint_black, "black")
lint.add_task(lint_mypy, "mypy")
lint.add_task(lint_flake8, "flake8")
lint.add_task(lint_all, "all")

test.add_task(test_all, "test_all")
test.add_task(test_unit, "unit")
