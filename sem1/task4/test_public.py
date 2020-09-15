import io
import sys

import pytest

from .task4 import left_rotate, right_rotate

def test_left_rotate(capsys, monkeypatch):  # type: ignore
    monkeypatch.setattr(sys, 'stdin', io.StringIO(f'100011101101\n3'))
    left_rotate()
    captured = capsys.readouterr()
    assert int(captured.out.replace('\n', '')) == int('011101101100', 2)
    assert captured.err == ''


def test_right_rotate(capsys, monkeypatch):  # type: ignore
    monkeypatch.setattr(sys, 'stdin', io.StringIO(f'100011101101\n3'))
    right_rotate()
    captured = capsys.readouterr()
    assert int(captured.out.replace('\n', '')) == int('101100011101', 2)
    assert captured.err == ''

