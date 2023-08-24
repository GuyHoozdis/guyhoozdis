import pytest

from sqlalchemy import select

from guyhoozdis.ppsql import ppsql

from .conftest import Parent, Child, Address, User


# XXX: Not actually needed.  I was just playing around.
# @pytest.fixture(autouse=True)
# def create_family(family, session):
#     dad, mom, children = family
#     dad.children = children
#     mom.children = children

#     session.add_all([dad, mom] + [c for c in children])
#     session.commit()

#     yield family


@pytest.mark.xfail(strict=True, reason="Not yet implemented.")
def test_ppsql_requires_sqlparse():
    assert False


@pytest.mark.xfail(strict=True, reason="Not yet implemented.")
def test_ppsql_formats_sql_as_string():
    assert False


@pytest.mark.xfail(strict=True, reason="Not yet implemented.")
def test_ppsql_formats_sqlalchemy_seletable():
    stmt = (
        select(User)
        .join(Address)
        .where(User.name == 'Kourtni')
    )

    # !!!: The way I wrote ppsql it will write to stdout.  I probably want a wrapper that does that
    # and right here I'd be testing the logic that takes a Select-able, renders arguments, and returns
    # a string.
    assert False


def test_sully(family, session):
    # Start this with...
    # $ poetry run pytest --pdbcls=IPython.terminal.debugger:TerminalPdb tests/ppsql/test_ppsql.py::test_sully
    # ... and you'll get exactly what
    #
    # The test body is dumb.  It is just to demonstrate the fixtures being used.

    stmt = (
        select(User)
        .join(Address)
        .where(User.name == 'Kourtni')
    )
    breakpoint()
    # dad, mom, children = family
    # dad.children = children
    # mom.children = children
    # session.add_all([dad, mom] + [c for c in children])
    # session.commit()

    # kourtni, jacob, lauren = children
    # assert kourtni in dad.children
    # assert mom in kourtni.parents
    assert False
