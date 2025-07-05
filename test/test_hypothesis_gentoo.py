import pytest


TEST_CASE = """
from hypothesis import assume
from hypothesis import given
from hypothesis import settings
import hypothesis.strategies as st


@given(i=st.integers(min_value=0, max_value=1000))
@settings(max_examples=1000)
def test_reject_most(i: int) -> None:
    assume(i >= 950)
"""


def test_disabled(pytester: pytest.Pytester) -> None:
    pytester.makepyfile(TEST_CASE)
    result = pytester.runpytest()
    result.assert_outcomes(failed=1)


def test_enabled(pytester: pytest.Pytester) -> None:
    pytester.makepyfile(TEST_CASE)
    result = pytester.runpytest("--hypothesis-profile=gentoo")
    result.assert_outcomes(passed=1)
