import sys

try:
    import sqlparse
except ImportError:
    sqlparse = None


def ppsql(query, chartype=str, file=sys.stdout, **overrides):
    """Pretty print SQL statements.

    query       - A string of SQL or SQLAlchemy Selectable object
    chartype    - unicode, str, or ...
    file        - Anything that exposes a .write() method
    overrides   - Override the options passed to sqlparse.format()
    """
    if not sqlparse:
        print("Requires sqlparse module to be installed.", file=sys.stderr)
        return

    options = dict(reindent=True, keyword_case="upper")
    options.update(**overrides)
    try:
        # TODO: Come back and support both Selectable and Query object
        # statement = query.statement.compile(compile_kwargs={'literal_binds': True})
        statement = query.compile(compile_kwargs={"literal_binds": True})
        formatted_statement = sqlparse.format(chartype(statement), **options)
    except Exception as ex:
        msg = "Failed to bind literals; "
        print(msg, ex, file=sys.stderr)
        formatted_statement = sqlparse.format(chartype(query), **options)

    print(formatted_statement, file=file)
