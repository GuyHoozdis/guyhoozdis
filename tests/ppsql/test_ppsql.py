import pytest
from sqlalchemy import select
from sqlalchemy.orm import Query

from guyhoozdis.ppsql import ppsql

from .conftest import Address, User, does_not_raise

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


def test_ppsql_formats_sql_as_string():
    param_value = "Kourtni"
    stmt = (
        "SELECT users.user_id, users.name, users.fullname "
        "FROM users JOIN addresses ON users.user_id = addresses.user_id "
        f"WHERE users.name = {param_value}"
    )

    with does_not_raise():
        output = ppsql(stmt)

    assert output
    assert param_value in output


def test_ppsql_formats_sqlalchemy_seletable():
    param_value = "Kourtni"
    stmt = select(User).join(Address).where(User.name == param_value)

    with does_not_raise():
        output = ppsql(stmt)

    assert output
    assert param_value in output


def test_ppsql_formats_sqlalchemy_query():
    param_value = "Kourtni"
    stmt = Query(User).join(Address).where(User.name == param_value)

    with does_not_raise():
        output = ppsql(stmt)

    assert output
    assert param_value in output
