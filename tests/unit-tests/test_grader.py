#!/usr/bin/env python
import re
from muskrat.grader import Grader


class TestGrader():
    def test_creation(self):
        grader = Grader({"compliance_recommendations": ["foo", "bar", "baz"]})
        assert isinstance(grader, Grader)
        assert grader.grade() == "C"
