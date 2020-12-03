from py_win_bash.command import Command
import pytest
from typing import Dict, List


class TestCommand:
    schema = {
        "flags": [
            {"title": "dev", "short": "d"},
        ],
        "kwargs": [
            {"title": "name", "short": "n"},
        ],
    }

    def test_basic_input(self):
        """
        Tests that parsing works with simple input
        """
        result = TestCommand._parse("hello world")
        assert ["hello", "world"] == result["args"]
        assert 0 == len(result["flags"])
        assert 0 == len(result["kwargs"])

    def test_flag_short_input(self):
        """
        Tests that parsing works with simple input and short flags
        """
        result = TestCommand._parse("hello world -d")
        assert ["hello", "world"] == result["args"]
        assert ["dev"] == result["flags"]
        assert 0 == len(result["kwargs"])

    def test_flag_title_input(self):
        """
        Tests that parsing works with simple input and title flags
        """
        result = TestCommand._parse("hello world --dev")
        assert ["hello", "world"] == result["args"]
        assert ["dev"] == result["flags"]
        assert 0 == len(result["kwargs"])

    def test_kwarg_short_input(self):
        """
        Tests that parsing works with simple input and short kwargs
        """
        result = TestCommand._parse("hello world -n James")
        assert ["hello", "world"] == result["args"]
        assert 0 == len(result["flags"])
        assert {"name": "James"} == result["kwargs"]

    def test_kwarg_title_input(self):
        """
        Tests that parsing works with simple input and title kwargs
        """
        result = TestCommand._parse("hello world --name James")
        assert ["hello", "world"] == result["args"]
        assert 0 == len(result["flags"])
        assert {"name": "James"} == result["kwargs"]

    def test_mixed_input(self):
        """
        Tests that parsing works with mixed input
        """
        result = TestCommand._parse("hello -n James world --dev")
        assert ["hello", "world"] == result["args"]
        assert ["dev"] == result["flags"]
        assert {"name": "James"} == result["kwargs"]

    def test_no_input(self):
        """
        Tests that parsing works with no input
        """
        result = TestCommand._parse("")
        assert 0 == len(result["args"])
        assert 0 == len(result["flags"])
        assert 0 == len(result["kwargs"])

    @staticmethod
    def _parse(value: str) -> Dict:
        """
        Parses command resulting in empty list when value was empty
        :param value: the input string to parse
        :return: Dict of parse results
        """
        value_list: List[str] = list(filter(None, value.split(" ")))
        return Command.parse(TestCommand.schema, value_list)
