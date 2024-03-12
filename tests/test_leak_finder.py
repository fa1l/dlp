from typing import Optional
import pytest
import re
from leak_finder.regexp import RegexpLeakFinder
from models.leakage import Leakage
from regexp_holder.in_memory_holder import InMemoryRegexpHolder


@pytest.mark.parametrize(
    "pattern, data, expected_result",
    [
        (
            re.compile("aab"),
            "aabb",
            [
                Leakage(
                    matched_pattern="aab", original_message="aabb", pattern="aab"
                ).model_dump_json()
            ],
        ),
        (re.compile("dog"), "cat", []),
    ],
)
def test_regexp_verificator(
    pattern: re.Pattern, data: str, expected_result: Optional[Leakage]
):
    regexp_holder = InMemoryRegexpHolder(storage=[pattern])
    verificator = RegexpLeakFinder(regexp_holder=regexp_holder)
    result = verificator.check_for_leaks(data)
    assert result == expected_result
