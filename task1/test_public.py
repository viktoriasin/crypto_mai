import io
import pathlib
import sys

import pytest

from .task1 import get_k_bit


def test_get_ks_bit(capsys, monkeypatch):  # type: ignore
    monkeypatch.setattr(sys, 'stdin', io.StringIO('1011001\n2\n'))
    get_k_bit()
    captured = capsys.readouterr()
    assert captured.out == bin(0)
    assert captured.err == ''

