#!/usr/bin/env python
import re
from muskrat.client import Client
from muskrat.client import Banner


class TestClient():
    def test_creation(self):
        client = Client("sshscan.rubidus.com", 22)
        assert isinstance(client, Client)
        assert isinstance(client.banner, Banner)
