import pytest
from flake8_plugin_utils import assert_error, assert_not_error

from flake8_breakpoint.errors import BreakpointFound, DebugModuleImportFound
from flake8_breakpoint.visitors import BreakpointVisitor


@pytest.mark.parametrize('src', ('breakpoint()',))
def test_breakpoint(src):
    assert_error(BreakpointVisitor, src, BreakpointFound)


@pytest.mark.parametrize(
    'src',
    (
        'import pdb',
        'from pdb import set_trace',
        'import ipdb',
        'from ipdb import set_trace',
        'import pudb',
        'from pudb import set_trace',
    ),
)
def test_debug_module_import(src):
    assert_error(BreakpointVisitor, src, DebugModuleImportFound)


@pytest.mark.parametrize(
    'src',
    (
        'import module',
        'from package import module',
        'func()',
        """
        class X:
            def method(self):
                pass

        x = X()
        x.method()
        """,
    ),
)
def test_error_not_exists(src):
    assert_not_error(BreakpointVisitor, src)
