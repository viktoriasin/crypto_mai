import io
import sys

import pytest

from .task2 import link_bits, get_bits_between


def test_link_bits(capsys, monkeypatch):  # type: ignore
    monkeypatch.setattr(sys, 'stdin', io.StringIO(f'100011101101\n3\n3'))
    link_bits()
    captured = capsys.readouterr()
    assert int(captured.out.replace('\n', '')) == int('100101', 2)
    assert captured.err == ''


def test_get_bits_between(capsys, monkeypatch):  # type: ignore
    monkeypatch.setattr(sys, 'stdin', io.StringIO(f'100011101101\n5\n3'))
    get_bits_between()
    captured = capsys.readouterr()
    assert int(captured.out.replace('\n', '')) == int('1101', 2)
    assert captured.err == ''

