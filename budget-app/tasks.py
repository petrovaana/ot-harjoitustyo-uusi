from invoke import task
from sys import platform

@task
def foo(ctx):
    print("bar")

@task
def start(ctx):
    ctx.run("python -m src.index", env={"PYTHONPATH": "src"})


@task
def format(c):
    c.run("autopep8 --in-place --recursive src")


@task
def test(ctx):
    ctx.run("pytest src")


@task
def lint(ctx):
    ctx.run("pylint src")


@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest")


@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html")