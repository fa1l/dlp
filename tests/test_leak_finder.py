from typing import Optional
import pytest
import re
from leak_finder.regexp import RegexpLeakFinder
from models.leakage import Leakage


@pytest.mark.parametrize(
    "pattern, data, expected_result",
    [
        (
            re.compile("aab"),
            "aabb",
            Leakage(message="aab", content="aabb", pattern="aab"),
        ),
        (re.compile("dog"), "cat", None),
    ],
)
def test_regexp_verificator(
    pattern: re.Pattern, data: str, expected_result: Optional[Leakage]
):
    verificator = RegexpLeakFinder(regexp_storage=[pattern])
    result = verificator.check_for_leaks(data)
    assert result == expected_result
