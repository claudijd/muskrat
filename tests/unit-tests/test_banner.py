#!/usr/bin/env python
import re
from muskrat.banner import Banner


class TestBanner():
    def test_creation(self):
        banner = Banner("SSH-2.0-server")
        assert isinstance(banner, Banner)
        assert banner.ssh_version() == 2.0
