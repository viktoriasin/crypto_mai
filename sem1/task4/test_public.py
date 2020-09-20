import io
import sys

import pytest

from .task4 import left_rotate, right_rotate


def test_left_rotate(capsys, monkeypatch):  # type: ignore
    monkeypatch.setattr(sys, 'stdin', io.StringIO(f'10000\n2'))
    left_rotate()
    captured = capsys.readouterr()
    assert int(captured.out.replace('\n', '')) == int('1000000', 2)
    assert captured.err == ''


def test_right_rotate(capsys, monkeypatch):  # type: ignore
    monkeypatch.setattr(sys, 'stdin', io.StringIO(f'10000\n2'))
    right_rotate()
    captured = capsys.readouterr()
    assert int(captured.out.replace('\n', '')) == int('100', 2)
    assert captured.err == ''

