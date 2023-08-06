"""
Rewrite django.utils.timezone.FixedOffset to datetime.timezone.
https://docs.djangoproject.com/en/2.2/releases/2.2/#features-deprecated-in-2-2
"""
import ast
from functools import partial
from typing import Iterable, Tuple

from tokenize_rt import Offset

from django_upgrade._ast_helpers import ast_end_offset, ast_start_offset
from django_upgrade._data import Plugin, State, TokenFunc
from django_upgrade._token_helpers import (
    OP,
    insert,
    insert_after,
    replace,
    update_imports,
)

plugin = Plugin(
    __name__,
    min_version=(2, 2),
)

MODULE = "django.utils.timezone"
OLD_NAME = "FixedOffset"


@plugin.register(ast.ImportFrom)
def visit_ImportFrom(
    state: State,
    node: ast.ImportFrom,
    parent: ast.AST,
) -> Iterable[Tuple[Offset, TokenFunc]]:
    if node.level != 0 or node.module != MODULE:
        return

    if any(alias.name == OLD_NAME for alias in node.names):
        yield ast_start_offset(node), partial(
            update_imports, node=node, name_map={"FixedOffset": ""}
        )
        yield ast_start_offset(node), partial(
            insert,
            new_src="from datetime import timedelta, timezone\n",
        )


@plugin.register(ast.Call)
def visit_Call(
    state: State,
    node: ast.Call,
    parent: ast.AST,
) -> Iterable[Tuple[Offset, TokenFunc]]:
    if (
        OLD_NAME in state.from_imports[MODULE]
        and isinstance(node.func, ast.Name)
        and node.func.id == OLD_NAME
    ):

        rewriting_offset_arg = False
        if len(node.args) >= 1 and not isinstance(node.args[0], ast.Starred):
            yield ast_start_offset(node.args[0]), partial(
                insert, new_src="timedelta(minutes="
            )
            yield ast_end_offset(node.args[0]), partial(insert, new_src=")")
            rewriting_offset_arg = True
        else:
            for keyword in node.keywords:
                if keyword.arg == "offset":
                    yield ast_start_offset(keyword), partial(
                        insert_after,
                        name=OP,
                        src="=",
                        new_src="timedelta(minutes=",
                    )
                    yield ast_end_offset(keyword), partial(insert, new_src=")")
                    rewriting_offset_arg = True

        if rewriting_offset_arg:
            yield ast_start_offset(node), partial(replace, src="timezone")
