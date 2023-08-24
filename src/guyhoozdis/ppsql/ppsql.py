from __future__ import annotations

import sys

from typing import Any, AnyStr

from sqlalchemy import Selectable
from sqlalchemy.orm import Query

try:
    import sqlparse
except ImportError:
    sqlparse = None

# !!!: These are the possible values for overrides.
#
#   keyword_case                  : [None], upper, lower, or capitalize
#   identifier_case               : [None], upper, lower, or capitalize
#   output_format                 : [None], sql, python, php
#   strip_comments                : [False], True
#   use_space_around_operators    : [False], True
#   strip_whitespace              : [False], True
#   truncate_strings              : [None], 1 <= n
#   truncate_char                 : ["[...]"], AnyStr
#   indent_columns                : [False], True
#   reindent                      : [False], True
#   reindent_aligned              : [False], True
#   indent_after_first            : [False], True
#   indent_tabs                   : [False], True
#   indent_width                  : [2], 1 < n
#   wrap_after                    : [0], 1 <= n
#   comma_first                   : [False], True
#   right_margin                  : [None], 10 < n
#################################################################################
# These modules/functions might be of interest.
#
#   sqlparse.keywords
#   sqlparse.filters
#   sqlparse.formatter.validate_options()
#   sqlparse.cli.create_parser()
#
#################################################################################

def ppsql(query: Selectable | Query | AnyStr, encoding=None, **overrides: Any) -> str:
    """Pretty print SQL statements.

    query       - A string of SQL, SQLAlchemy Selectable object, or SQLAlchemy Query object
    overrides   - Override the options passed to sqlparse.format()
    """
    if not sqlparse:
        raise ImportError("Requires sqlparse module to be installed.")

    if not isinstance(query, (Selectable, Query, str)):
        query_type = type(query)
        raise TypeError(f"Cannot process query of type {query_type}.")

    # Combine defaults with overrides to get the requested options.
    options = dict(reindent=True, keyword_case="upper", indent_columns=True, indent_after_first=True)
    options.update(**overrides)

    if isinstance(query, Query):
        # !!!: See the code comments in the statement method body.  This approach will not work if
        # the Query was constructed using from_self(), with_polymorphic(), select_entity_from(), etc.
        query = query.statement

    if isinstance(query, str):
        formatted_statement = sqlparse.format(query, encoding=encoding, **options)
    else:
        statement = query.compile(compile_kwargs={"literal_binds": True})
        formatted_statement = sqlparse.format(f"{statement}", **options)

    return formatted_statement


def cli(query: Selectable | AnyStr, encoding=None, file=sys.stdout, **overrides) -> None:
    """Pretty print SQL statements.

    query       - A string of SQL or SQLAlchemy Selectable object
    file        - Anything that exposes a .write() method
    overrides   - Override the options passed to sqlparse.format()
    """
    try:
        formatted_statement = ppsql(query, encoding=encoding, **overrides)
    except ImportError:
        print("Requires sqlparse module to be installed.", file=sys.stderr)
        return

    print(formatted_statement, file=file)
