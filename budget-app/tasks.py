"""Defines different command-line automation tasks using Invoke."""

from invoke import task
from sys import platform

@task
def start(ctx):
    """Used for starting the application"""
    ctx.run("python -m src.index", env={"PYTHONPATH": "src"})


@task
def format(c):
    """Formats the code"""
    c.run("autopep8 --in-place --recursive src")


@task
def test(ctx):
    """Used for testing the application."""
    ctx.run("pytest src")


@task
def lint(ctx):
    """Used for pylint checks."""
    ctx.run("pylint src")


@task
def coverage(ctx):
    """Used for coverage testing"""
    ctx.run("coverage run --branch -m pytest")


@task(coverage)
def coverage_report(ctx):
    """Used for covering reports"""
    ctx.run("coverage html")
